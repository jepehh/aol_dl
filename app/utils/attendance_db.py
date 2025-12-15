import os
import csv
from datetime import datetime
from src.config import ATTENDANCE_DIR

def create_session(session_name, lecturer_ip):
    os.makedirs(ATTENDANCE_DIR, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}_{session_name}.csv"
    filepath = os.path.join(ATTENDANCE_DIR, filename)
    
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Name', 'Confidence', 'Student_IP', 'Lecturer_IP'])
    
    return filepath

def mark_attendance(filepath, name, confidence, student_ip, lecturer_ip):
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, name, f"{confidence:.2f}", student_ip, lecturer_ip])

def check_already_marked(filepath, name):
    if not os.path.exists(filepath):
        return False
    
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Name'] == name:
                return True
    return False

def get_attendance_list(filepath):
    if not os.path.exists(filepath):
        return []
    
    records = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records