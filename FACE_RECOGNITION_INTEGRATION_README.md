# Face Recognition System Integration with EduConnect

This document explains how the face recognition system is integrated with EduConnect to provide automated attendance tracking.

## How It Works

1. When a teacher clicks the "Take Attendance" button in the EduConnect teacher dashboard:
   - The frontend sends a request to the EduConnect backend
   - The backend triggers the face recognition system via a Python script
   - Existing face recognition data is cleared to start fresh
   - The face recognition system runs and captures attendance
   - Attendance data is synchronized with the EduConnect MongoDB database

## Integration Components

### 1. Frontend (teacher-dashboard.html & teacher.js)
- The "Take Attendance" button triggers the face recognition process
- JavaScript sends a request to the backend API endpoint

### 2. Backend API (faceRecognition.routes.js & faceRecognition.controller.js)
- New endpoint `/api/face-recognition/take-attendance` handles the process
- Controller clears existing data and runs the Python script
- Uses utility functions to execute Python commands

### 3. Python Face Recognition System (face folder)
- Contains the face recognition application with SQLite database
- `take_attendance.py` is the main script that runs when triggered
- `educonnect_client.py` handles synchronization with EduConnect
- Clears existing data before each session

### 4. Utility Functions (faceRecognition.utils.js)
- Node.js utilities to execute Python scripts
- Handles process spawning and error management

## Data Flow

```
Teacher clicks "Take Attendance"
        ↓
EduConnect frontend sends request
        ↓
EduConnect backend receives request
        ↓
Backend clears existing face data
        ↓
Backend runs Python face recognition script
        ↓
Python system captures attendance via camera
        ↓
Python system syncs data with EduConnect MongoDB
        ↓
Response sent back to frontend
```

## Database Synchronization

The system maintains a single source of truth in the EduConnect MongoDB database:
- Local SQLite data is temporary and cleared before each session
- All attendance records are stored permanently in EduConnect MongoDB
- Student mappings are maintained between systems

## Security

- Only authenticated teachers can trigger the face recognition system
- API tokens are passed securely to Python scripts
- All operations are logged for audit purposes

## Setup Requirements

1. Python 3.7+ must be installed on the system
2. Required Python packages must be installed:
   ```
   pip install -r requirements.txt
   ```
3. Camera device must be accessible to the system
4. Proper file permissions for executing scripts