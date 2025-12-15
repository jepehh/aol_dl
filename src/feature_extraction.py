import os
import dlib
import numpy as np
from src.config import DATA_PREPROCESSED, SHAPE_PREDICTOR, FACE_REC_MODEL

shape_predictor = None
face_rec_model = None

def load_dlib_models():
    global shape_predictor, face_rec_model
    if shape_predictor is None:
        shape_predictor = dlib.shape_predictor(SHAPE_PREDICTOR)
        face_rec_model = dlib.face_recognition_model_v1(FACE_REC_MODEL)

def extract_embeddings():
    load_dlib_models()
    
    embeddings = []
    labels = []
    
    for person_name in os.listdir(DATA_PREPROCESSED):
        person_path = os.path.join(DATA_PREPROCESSED, person_name)
        if not os.path.isdir(person_path):
            continue
        
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            img = dlib.load_rgb_image(img_path)
            
            dets = [dlib.rectangle(0, 0, img.shape[1], img.shape[0])]
            
            if len(dets) == 0:
                continue
            
            shape = shape_predictor(img, dets[0])
            embedding = np.array(face_rec_model.compute_face_descriptor(img, shape))
            
            embeddings.append(embedding)
            labels.append(person_name)
    
    return np.array(embeddings), np.array(labels)