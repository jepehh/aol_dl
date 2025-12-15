import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PREPROCESSED = os.path.join(BASE_DIR, "data", "preprocessed")

MODELS_DIR = os.path.join(BASE_DIR, "models")
SHAPE_PREDICTOR = os.path.join(MODELS_DIR, "shape_predictor_68_face_landmarks.dat")
FACE_REC_MODEL = os.path.join(MODELS_DIR, "dlib_face_recognition_resnet_model_v1.dat")
NEURAL_NET_MODEL = os.path.join(MODELS_DIR, "neural_net_model.h5")
LABEL_ENCODER = os.path.join(MODELS_DIR, "classes.npy")

OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
PLOTS_DIR = os.path.join(OUTPUTS_DIR, "plots")
LOGS_DIR = os.path.join(OUTPUTS_DIR, "logs")

ATTENDANCE_DIR = os.path.join(BASE_DIR, "attendance_records")

CONFIDENCE_THRESHOLD = 0.6
TEST_SIZE = 0.2
RANDOM_STATE = 42
EPOCHS = 100
BATCH_SIZE = 16