import cv2
import dlib
import numpy as np
import tensorflow as tf
from src.config import SHAPE_PREDICTOR, FACE_REC_MODEL, NEURAL_NET_MODEL, LABEL_ENCODER, CONFIDENCE_THRESHOLD

shape_predictor = dlib.shape_predictor(SHAPE_PREDICTOR)
face_rec_model = dlib.face_recognition_model_v1(FACE_REC_MODEL)
detector = dlib.get_frontal_face_detector()

model = None
label_encoder = None

def load_models():
    global model, label_encoder
    model = tf.keras.models.load_model(NEURAL_NET_MODEL)
    label_encoder = np.load(LABEL_ENCODER, allow_pickle=True)

def recognize_face(frame):
    if model is None or label_encoder is None:
        load_models()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)
    
    if len(faces) == 0:
        return None, 0.0, None
    
    rect = faces[0]
    shape = shape_predictor(frame, rect)
    embedding = np.array(face_rec_model.compute_face_descriptor(frame, shape)).reshape(1, -1)
    
    preds = model.predict(embedding, verbose=0)
    confidence = np.max(preds)
    label_idx = np.argmax(preds)
    label = label_encoder[label_idx]
    
    x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
    bbox = (x, y, w, h)
    
    return label, confidence, bbox