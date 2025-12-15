# Face Recognition Attendance System

AI-powered attendance system using face recognition with network verification to prevent remote attendance fraud.

## Project Overview

This system enables lecturers to take attendance automatically using face recognition technology. Students mark their attendance by taking a photo, and the system verifies they are on the same WiFi network as the lecturer to prevent remote fraud.

## Project Structure

```
face-recognition-attendance/
├── data/                           # Dataset folder
│   ├── raw/                        # Original images (23 people × 10 images)
│   ├── processed/                  # Preprocessed face crops
│   └── README.md                   # Dataset documentation
│
├── models/                         # Pre-trained models (dlib)
│   ├── shape_predictor_68_face_landmarks.dat
│   └── dlib_face_recognition_resnet_model_v1.dat
│
├── src/                            # Source code
│   ├── __init__.py
│   ├── config.py                   # Configuration loader
│   ├── data_preprocessing.py       # Face detection & cropping
│   ├── feature_extraction.py       # Embedding extraction
│   ├── model_training.py           # Neural network training
│   ├── model_evaluation.py         # Metrics & visualization
│   └── face_recognition.py         # Real-time recognition
│
├── config/                         # Configuration files
│   └── config.yaml                 # Centralized settings
│
├── outputs/                        # Generated outputs
│   ├── models/                     # Trained models
│   │   ├── neural_net_model.h5     # Our trained classifier
│   │   └── classes.npy             # Label encoder
│   ├── plots/                      # Training visualizations
│   │   ├── accuracy_metrics.jpg
│   │   ├── loss_metrics.jpg
│   │   └── confusion_matrix.jpg
│   └── attendance/                 # Attendance records (CSV)
│
├── app/                            # Streamlit web application
│   ├── streamlit_app.py            # Main page
│   ├── pages/
│   │   ├── 1_Student_Attendance.py # Student interface
│   │   └── 2_Lecturer_Dashboard.py # Lecturer interface
│   └── utils/
│       ├── network_utils.py        # WiFi verification
│       ├── camera_utils.py         # Camera handling
│       └── attendance_db.py        # CSV operations
│
├── scripts/                        # Utility scripts
│   ├── 1_preprocess_dataset.py     # Preprocess images
│   ├── 2_train_model.py            # Train model
│   └── 3_evaluate_model.py         # Evaluate model
│
├── run_with_ngrok.py              # Deploy with ngrok tunnel
├── requirements.txt               # Python dependencies
├── .gitignore
└── README.md
```

## 🔧 Technology Stack

- **Face Detection:** dlib HOG + CNN
- **Face Recognition:** dlib ResNet (128D embeddings)
- **Classification:** TensorFlow/Keras Neural Network
- **Web Interface:** Streamlit
- **Network Verification:** Socket programming
- **Data Processing:** OpenCV, NumPy, Pandas

## 📋 Requirements

- Python 3.11+
- Windows/Linux/MacOS
- Webcam
- WiFi network (for network verification)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/face-recognition-attendance.git
cd face-recognition-attendance
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download dlib models
Download these files and place in `models/` folder:
- [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)
- [dlib_face_recognition_resnet_model_v1.dat](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)

Extract the `.bz2` files to get the `.dat` files.

### 4. Prepare dataset
Place your dataset in `data/raw/` following this structure:
```
data/raw/
├── Person1/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
├── Person2/
└── ...
```

### 5. Preprocess and train
```bash
# Preprocess images
python scripts/1_preprocess_dataset.py

# Train model
python scripts/2_train_model.py

# Evaluate (optional)
python scripts/3_evaluate_model.py
```

## 🎮 Usage

### Local Deployment (Same WiFi)

```bash
streamlit run app/streamlit_app.py
```

Access at: `http://localhost:8501`

### Remote Deployment (ngrok)

```bash
# Sign up at ngrok.com and get authtoken
# Update run_with_ngrok.py with your token

python run_with_ngrok.py
```

Students access via ngrok URL (e.g., `https://abc123.ngrok.io`)

## 📱 How to Use

### For Lecturers:
1. Open **Lecturer Dashboard**
2. Click **Start Session**
3. Share your IP with students (displayed on dashboard)
4. Monitor live attendance
5. Export attendance to CSV when done

### For Students:
1. Connect to same WiFi as lecturer
2. Open **Student Attendance** page
3. Take a photo using webcam
4. System detects face and shows confidence
5. Click **Verify Attendance** button
6. System checks:
   - ✅ Face recognized?
   - ✅ Confidence > 60%?
   - ✅ Same WiFi as lecturer?
   - ✅ Not already marked?

## 🔒 Security Features

- **Network Verification:** Checks if student is on same WiFi
- **Duplicate Prevention:** Can't mark attendance twice
- **Confidence Threshold:** Requires 60%+ confidence
- **Live Detection:** Must capture photo during session

## 📊 Model Performance

After training, check `outputs/plots/` for:
- Training/validation accuracy curves
- Loss curves
- Confusion matrix
- Classification report

## 🛠️ Configuration

Edit `config/config.yaml` to customize:
- Model paths
- Training hyperparameters
- Confidence threshold
- Output directories

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is for educational purposes. Please ensure proper consent for using personal images.

## 👥 Team

- Jason Patrick W. H. - 2602163494

## 📚 References

1. FaceNet: A Unified Embedding for Face Recognition and Clustering (2015)
2. Analysis of Face Recognition Algorithm: Dlib and OpenCV (2020)
3. Face Recognition Application for Office Attendance (2020)

## 🐛 Troubleshooting

**dlib installation fails:**
- Windows: Use pre-built wheel from [here](https://github.com/z-mahmud22/Dlib_Windows_Python3.x)
- Linux: Install cmake and build-essential first

**Model files too large:**
- Don't commit `.dat` files to GitHub
- Use Git LFS or download separately

**Network verification not working:**
- Ensure firewall allows local network discovery
- Check if all devices on same subnet

## 📧 Contact

For questions or issues, please open an issue on GitHub or contact via email.