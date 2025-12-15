import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from app.utils.network_utils import get_local_ip
from app.utils.attendance_db import create_session, get_attendance_list

st.set_page_config(page_title="Lecturer Dashboard", layout="wide")
st.title("👨‍🏫 Lecturer Dashboard")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Session Control")
    
    session_name = st.text_input("Session Name", value="DL-Class")
    
    if 'session_active' not in st.session_state:
        st.session_state.session_active = False
    
    if not st.session_state.session_active:
        if st.button("🟢 Start Session", type="primary", use_container_width=True):
            lecturer_ip = get_local_ip()
            session_file = create_session(session_name, lecturer_ip)
            
            st.session_state.session_active = True
            st.session_state.session_file = session_file
            st.session_state.lecturer_ip = lecturer_ip
            st.session_state.session_name = session_name
            
            st.success(f"Session started!")
            st.rerun()
    else:
        if st.button("🔴 Stop Session", type="secondary", use_container_width=True):
            st.session_state.session_active = False
            st.warning("Session stopped.")
            st.rerun()
    
    st.divider()
    
    if st.session_state.session_active:
        st.info(f"**Session:** {st.session_state.session_name}")
        st.info(f"**Your IP:** {st.session_state.lecturer_ip}")

with col2:
    st.subheader("Live Attendance")
    
    if st.session_state.session_active:
        records = get_attendance_list(st.session_state.session_file)
        
        if records:
            df = pd.DataFrame(records)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            st.divider()
            
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Export to Excel (CSV)",
                data=csv,
                file_name=f"{st.session_state.session_name}_attendance.csv",
                mime="text/csv",
                use_container_width=True
            )
        else:
            st.info("No attendance records yet.")
        
        if st.button("🔄 Refresh", use_container_width=True):
            st.rerun()
    else:
        st.warning("No active session. Please start a session first.")