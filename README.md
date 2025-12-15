# README.md

# Face Recognition Attendance System

Face recognition-based attendance system using ResNet + DLIB with network verification.

## Project Structure
```
face-recognition-attendance/
├── data/
│   ├── raw/                    # Put your 22 people × 10 images here
│   └── preprocessed/           # Auto-generated cropped faces
├── models/
│   ├── shape_predictor_68_face_landmarks.dat
│   ├── dlib_face_recognition_resnet_model_v1.dat
│   ├── neural_net_model.h5    # Trained model
│   └── classes.npy             # Label encoder
├── src/
│   ├── config.py
│   ├── data_preprocessing.py
│   ├── feature_extraction.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── face_recognition.py
├── app/
│   ├── streamlit_app.py        # Main page
│   ├── utils/
│   │   ├── network_utils.py
│   │   ├── camera_utils.py
│   │   └── attendance_db.py
│   └── pages/
│       ├── 1_Student_Attendance.py
│       └── 2_Lecturer_Dashboard.py
├── scripts/
│   ├── 1_preprocess_dataset.py
│   ├── 2_train_model.py
│   └── 3_evaluate_model.py
├── outputs/plots/
├── attendance_records/
└── requirements.txt
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Download DLIB models:
- shape_predictor_68_face_landmarks.dat
- dlib_face_recognition_resnet_model_v1.dat

Place them in `models/` folder.

3. Prepare dataset:
```
data/raw/
├── Person1/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
├── Person2/
└── ...
```

## Training
```bash
python scripts/1_preprocess_dataset.py
python scripts/2_train_model.py
```

## Running Streamlit App
```bash
streamlit run app/streamlit_app.py
```

## Usage

**Lecturer:**
1. Open Lecturer Dashboard
2. Start session
3. Share your IP with students
4. Monitor live attendance
5. Export to CSV

**Student:**
1. Connect to same WiFi as lecturer
2. Open Student Attendance page
3. Take photo
4. Click "Verify Attendance"

## Features

- Multi-class face recognition (22 people)
- Network verification (same WiFi required)
- Duplicate attendance prevention
- Live attendance dashboard
- Export to Excel/CSV
- Confidence threshold filtering