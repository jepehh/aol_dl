import cv2
import numpy as np

def get_frame_from_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        return frame
    return None

def draw_bbox_and_label(frame, bbox, label, confidence):
    if bbox is None:
        return frame
    
    x, y, w, h = bbox
    color = (0, 255, 0) if confidence > 0.6 else (0, 165, 255)
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    text = f"{label} ({confidence:.2f})"
    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
    
    return frame