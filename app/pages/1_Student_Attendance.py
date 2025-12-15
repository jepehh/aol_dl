import streamlit as st
import cv2
import numpy as np
from PIL import Image
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from src.face_recognition import recognize_face
from app.utils.network_utils import get_local_ip, is_same_network
from app.utils.camera_utils import draw_bbox_and_label
from app.utils.attendance_db import mark_attendance, check_already_marked

st.set_page_config(page_title="Student Attendance", layout="wide")
st.title("📸 Mark Your Attendance")

if 'session_active' not in st.session_state or not st.session_state.session_active:
    st.error("No active session. Please wait for lecturer to start the session.")
    st.stop()

session_file = st.session_state.get('session_file')
lecturer_ip = st.session_state.get('lecturer_ip')

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Camera Feed")
    camera = st.camera_input("Take a photo")
    
    if camera is not None:
        bytes_data = camera.getvalue()
        cv_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        label, confidence, bbox = recognize_face(cv_img)
        
        if label and confidence > 0.5:
            cv_img = draw_bbox_and_label(cv_img, bbox, label, confidence)
            st.session_state['current_name'] = label
            st.session_state['current_confidence'] = confidence
        else:
            st.session_state['current_name'] = None
            st.session_state['current_confidence'] = 0.0
        
        st.image(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB), channels="RGB", use_column_width=True)

with col2:
    st.subheader("Attendance Status")
    
    if 'current_name' in st.session_state and st.session_state.current_name:
        st.success(f"Detected: **{st.session_state.current_name}**")
        st.info(f"Confidence: {st.session_state.current_confidence:.2%}")
        
        if st.button("✅ Verify Attendance", type="primary", use_container_width=True):
            student_ip = get_local_ip()
            
            if not is_same_network(student_ip, lecturer_ip):
                st.error("❌ You must be on the same network as the lecturer!")
            elif check_already_marked(session_file, st.session_state.current_name):
                st.warning("⚠️ You have already marked attendance!")
            elif st.session_state.current_confidence < 0.6:
                st.error("❌ Face not clearly recognized. Please retake photo.")
            else:
                mark_attendance(
                    session_file, 
                    st.session_state.current_name, 
                    st.session_state.current_confidence, 
                    student_ip, 
                    lecturer_ip
                )
                st.success("✅ Attendance marked successfully!")
                st.balloons()
    else:
        st.warning("No face detected. Please take a photo.")

st.divider()
st.caption(f"Your IP: {get_local_ip()} | Lecturer IP: {lecturer_ip}")