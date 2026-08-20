# 🤟 Sign Language Detection using YOLO

A real-time **Sign Language Detection** system built using **Ultralytics YOLO** and Python. The model detects and classifies sign-language gestures from images and a live webcam feed.

The project uses YOLO object detection to recognize six sign-language gestures:

* 👋 Hello
* ❤️ I Love You
* ❌ No
* 🙏 Please
* 🙌 Thanks
* ✅ Yes

---

## 🚀 Features

* Real-time sign-language detection
* Webcam-based inference
* Image-based inference
* YOLO object detection
* Custom-trained dataset
* Six sign-language classes
* Confidence-based predictions
* Jupyter Notebook workflow
* Easily extendable with additional gestures

---

## 🧠 Model

This project uses **Ultralytics YOLO** for object detection.

### Training Configuration

| Parameter              | Value            |
| ---------------------- | ---------------- |
| Model                  | YOLO26n          |
| Task                   | Object Detection |
| Epochs                 | 25               |
| Image Size             | 640 × 640        |
| Batch Size             | 16               |
| Number of Classes      | 6                |
| Dataset Images         | 150              |
| Training Images        | 120              |
| Test/Validation Images | 30               |

The training configuration is taken from the project notebook.

### Classes

```text
0 - Hello
1 - IloveYou
2 - No
3 - Please
4 - Thanks
5 - Yes
```

---

## 📊 Model Performance

The trained model achieved the following validation results:

| Metric    | Score |
| --------- | ----: |
| Precision | 89.7% |
| Recall    | 89.9% |
| mAP@50    | 96.2% |
| mAP@50-95 | 80.2% |

Per-class mAP@50:

| Class    | mAP@50 |
| -------- | -----: |
| Hello    |  89.8% |
| IloveYou |  99.5% |
| No       |  92.8% |
| Please   |  96.2% |
| Thanks   |  99.5% |
| Yes      |  99.5% |

These values are from the final validation output of the notebook.

---

# 📁 Project Structure

```text
Sign_language_detection/
│
├── Sign_language_data/
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   │
│   ├── test/
│   │   ├── images/
│   │   └── labels/
│   │
│   └── data.yaml
│
├── runs/
│   └── detect/
│       └── train/
│           ├── weights/
│           │   ├── best.pt
│           │   └── last.pt
│           ├── results.png
│           ├── confusion_matrix.png
│           └── labels.jpg
│
├── main.ipynb
├── requirements.txt
└── README.md
```

> **Important:** `best.pt` is required if you want to run inference without training the model again.

---

# ⚙️ Setup on Another Machine

Follow these steps to run the project on another computer.

## 1. Install Python

Install **Python 3.10.x**.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

Python 3.10 was used for the original training environment.

---

## 2. Clone the Repository

Open Terminal / Command Prompt and run:

```bash
git clone https://github.com/mohitrohda/Sign_language_detection.git
```

Go inside the project:

```bash
cd Sign_language_detection
```

---

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

After activation, you should see something similar to:

```text
(venv)
```

in your terminal.

---

## 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 5. Install Dependencies

Install the required libraries:

```bash
pip install ultralytics==8.4.123
pip install jupyter
pip install ipykernel
pip install opencv-python
```

Or, if the repository contains `requirements.txt`:

```bash
pip install -r requirements.txt
```

The original notebook used **Ultralytics 8.4.123** with Python 3.10.11.

---

# 📦 6. Check the Dataset

Make sure the project contains:

```text
Sign_language_data/
```

Inside it:

```text
Sign_language_data/
├── train/
│   ├── images/
│   └── labels/
│
├── test/
│   ├── images/
│   └── labels/
│
└── data.yaml
```

The notebook uses:

```text
Sign_language_data/data.yaml
```

as the dataset configuration file.

---

# 🏋️ 7. Train the Model

If you want to train the model from scratch, run:

```bash
yolo task=detect mode=train data="Sign_language_data/data.yaml" model="yolo26n.pt" epochs=25 imgsz=640
```

Ultralytics will download the pretrained `yolo26n.pt` model automatically if it is not already available.

The trained model will be saved inside something similar to:

```text
runs/detect/train/weights/
```

The important file is:

```text
best.pt
```

---

# 🔍 8. Run Prediction on Test Images

After training, run:

```bash
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" conf=0.25 source="Sign_language_data/test/images" save=True
```

The prediction results will be saved under:

```text
runs/detect/predict/
```

---

# 📷 9. Run Real-Time Webcam Detection

Connect your webcam and run:

```bash
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" conf=0.25 source=0 show=True
```

### What does `source=0` mean?

```text
source=0
```

means the default webcam/camera.

If you have multiple cameras, try:

```bash
source=1
```

or:

```bash
source=2
```

---

# 🖥️ 10. If Webcam Opens but You Cannot See the Video

If the camera opens but the video window does not appear correctly, try running the command directly from **Terminal/Command Prompt** instead of only running it inside Jupyter Notebook:

```bash
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" conf=0.25 source=0 show=True
```

Also make sure your operating system has given Python/Terminal permission to access the camera.

### macOS

Go to:

```text
System Settings
→ Privacy & Security
→ Camera
```

Enable camera access for the application you are using.

---

# 📓 11. Run the Jupyter Notebook

Start Jupyter:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

Open:

```text
main.ipynb
```

Then run the cells in order.

---

# 🔄 Complete Setup — Quick Version

If you just want the shortest setup:

```bash
git clone https://github.com/mohitrohda/Sign_language_detection.git

cd Sign_language_detection

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

Then:

```bash
python -m pip install --upgrade pip

pip install ultralytics==8.4.123
pip install jupyter
pip install ipykernel
pip install opencv-python
```

Run webcam detection:

```bash
yolo task=detect mode=predict model="runs/detect/train/weights/best.pt" conf=0.25 source=0 show=True
```

---

# 🧪 Training vs Inference

You **do not need to train the model again** if the repository already contains:

```text
runs/detect/train/weights/best.pt
```

For simply testing the project:

```text
Clone repository
      ↓
Create virtual environment
      ↓
Install dependencies
      ↓
Make sure best.pt exists
      ↓
Run YOLO prediction
      ↓
Use webcam
```

Training is only required if:

* `best.pt` is not included
* You modify the dataset
* You add new sign classes
* You want to improve the model

---

# 🛠️ Technologies Used

* Python
* Ultralytics YOLO
* PyTorch
* OpenCV
* Jupyter Notebook
* Computer Vision
* Object Detection

---

# 🎯 Future Improvements

* Add more sign-language gestures
* Increase dataset size
* Improve real-time inference speed
* Add text-to-speech output
* Build a web application using Streamlit
* Deploy the model as an API
* Support multiple signs in a sentence
* Improve performance under different lighting conditions

---

# ⚠️ Limitations

The current model is trained on a relatively small dataset containing 150 images, so performance may vary with:

* Different backgrounds
* Different lighting conditions
* Different hand positions
* Different camera angles
* Different users
* Signs that are significantly different from the training examples

For a production-level sign-language system, a considerably larger and more diverse dataset would be recommended.

---

# 👨‍💻 Author

**Mohit Rohda**

GitHub:
https://github.com/mohitrohda

Project:
https://github.com/mohitrohda/Sign_language_detection

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
