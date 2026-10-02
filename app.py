# app.py — run with: streamlit run app.py  (NOT from the notebook)
import streamlit as st
import cv2, subprocess, time
from datetime import datetime
import pandas as pd
from ultralytics import YOLO

st.set_page_config(page_title="Sign Language Detector", layout="wide")
st.title("🤟 Sign Language Detection")

@st.cache_resource
def load_model():
    return YOLO("runs/detect/train-4/weights/best.pt")

model = load_model()

if "log" not in st.session_state:
    st.session_state.log = []

col1, col2 = st.columns([2, 1])

with col2:
    run = st.checkbox("Start Camera")
    audio_on = st.checkbox("Enable Audio", value=True)
    current_sign = st.empty()
    st.subheader("Detection Log")
    log_table = st.empty()
    if st.session_state.log:
        df = pd.DataFrame(st.session_state.log)
        st.download_button("Download Log (CSV)", df.to_csv(index=False), "detection_log.csv")

with col1:
    frame_window = st.image([])

camera = cv2.VideoCapture(0)
last_spoken, last_time, cooldown = None, 0, 2  # seconds before repeating same word

while run:
    ret, frame = camera.read()
    if not ret:
        st.error("Could not access webcam.")
        break

    results = model.predict(frame, conf=0.25, verbose=False)
    annotated = results[0].plot()
    annotated_rgb = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)

    boxes = results[0].boxes
    if len(boxes) > 0:
        best = boxes[boxes.conf.argmax()]
        label = model.names[int(best.cls[0])]
        conf = float(best.conf[0])

        current_sign.markdown(f"## Detected: **{label}** ({conf:.0%})")

        now = time.time()
        if label != last_spoken or now - last_time > cooldown:
            if audio_on:
                subprocess.Popen(["say", label])
            st.session_state.log.append({
                "timestamp": datetime.now().strftime("%H:%M:%S"),
                "sign": label,
                "confidence": f"{conf:.2f}"
            })
            log_table.dataframe(pd.DataFrame(st.session_state.log[-10:]), use_container_width=True)
            last_spoken, last_time = label, now
    else:
        current_sign.markdown("## Detected: —")

    frame_window.image(annotated_rgb)

camera.release()