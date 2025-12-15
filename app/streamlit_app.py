import streamlit as st

st.set_page_config(
    page_title="Face Recognition Attendance System - Demo",
    page_icon="📸",
    layout="wide"
)

st.title("📸 Face Recognition Attendance System - Demo Version")
st.markdown("---")

st.warning("⚠️ This is a DEMO version deployed on Streamlit Cloud. Network verification is disabled.")

st.markdown("""
## Welcome to the Attendance System Demo

### Features in this demo:
- ✅ Face recognition using trained model
- ✅ Real-time webcam detection
- ✅ Attendance marking simulation
- ❌ Network verification (disabled for cloud deployment)

### For Students:
Navigate to **Student Attendance** page to mark your attendance.

### For Lecturers:
Navigate to **Lecturer Dashboard** to manage sessions and view attendance.

---

**Note:** For production use with network verification, run the app locally on your campus network.

### Local Setup Instructions:
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/face-recognition-attendance.git

# Install dependencies
pip install -r requirements.txt

# Run locally
streamlit run app/streamlit_app.py

# Or with ngrok for remote access:
python run_with_ngrok.py
```
""")

st.info("Use the sidebar to navigate between pages.")