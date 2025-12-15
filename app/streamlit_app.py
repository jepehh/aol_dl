import streamlit as st

st.set_page_config(
    page_title="Face Recognition Attendance System",
    page_icon="📸",
    layout="wide"
)

st.title("📸 Face Recognition Attendance System")
st.markdown("---")

st.markdown("""
## Welcome to the Attendance System

### For Students:
Navigate to **Student Attendance** page to mark your attendance.

### For Lecturers:
Navigate to **Lecturer Dashboard** to start/stop sessions and view attendance.

---

**Instructions:**
1. Lecturer starts a session from the Dashboard
2. Students take a photo and verify attendance
3. System checks face recognition + network verification
4. Lecturer can view live attendance and export to Excel
""")

st.info("Use the sidebar to navigate between pages.")