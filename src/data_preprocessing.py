import os
import cv2
import dlib
from src.config import DATA_RAW, DATA_PROCESSED

detector = dlib.get_frontal_face_detector()

def preprocess_dataset():
    os.makedirs(DATA_PROCESSED, exist_ok=True)
    
    for person_name in os.listdir(DATA_RAW):
        person_path = os.path.join(DATA_RAW, person_name)
        if not os.path.isdir(person_path):
            continue
        
        output_person_path = os.path.join(DATA_PROCESSED, person_name)
        os.makedirs(output_person_path, exist_ok=True)
        
        for img_name in os.listdir(person_path):
            img_path = os.path.join(person_path, img_name)
            img = cv2.imread(img_path)
            
            if img is None:
                continue
            
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)
            
            if len(faces) == 0:
                continue
            
            for i, rect in enumerate(faces):
                x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
                x, y = max(0, x), max(0, y)
                face_crop = img[y:y+h, x:x+w]
                
                output_path = os.path.join(output_person_path, f"{os.path.splitext(img_name)[0]}_{i}.jpg")
                cv2.imwrite(output_path, face_crop)
    
    print(f"Preprocessing complete. Saved to {DATA_PROCESSED}")