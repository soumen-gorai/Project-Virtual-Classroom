# 🎓 Virtual Classroom System with Face Recognition Attendance

A full-stack **Virtual Classroom / Learning Management System** integrated with **AI-based Face Recognition Attendance** to automate classroom operations, attendance tracking, and student performance monitoring.

This project combines **web development**, **backend APIs**, **database management**, and **computer vision** to build a smart classroom platform for modern educational institutions.

---

## 📌 Project Overview

The **Virtual Classroom System** is designed to help educational institutions manage:

- Teachers and students
- Classes and subjects
- Attendance records
- Automated face recognition attendance
- Student performance prediction
- Real-time classroom management

The main highlight of this project is the **Face Recognition Attendance Module**, which captures students' faces through a camera and automatically marks attendance in the system.

This makes the system more:
- efficient
- accurate
- time-saving
- modern and scalable

---

## 🚀 Main Features

### 👨‍🏫 Classroom Management
- Create and manage classes
- Assign teachers to classes
- Manage student enrollment
- Maintain classroom records

### 👨‍🎓 Student Management
- Add student details
- View student records
- Manage attendance history
- Store academic information

### 📸 Face Recognition Attendance
- Real-time face detection
- Student face recognition
- Automated attendance marking
- Confidence-based recognition
- Attendance synchronization with main system

### 📊 Attendance Tracking
- Daily attendance records
- Real-time updates
- Teacher-controlled attendance sessions
- Reduced manual attendance effort

### 🤖 Student Performance Prediction
- ML-based student performance prediction
- Attendance and academic score analysis
- Predictive insights using trained model

### 🔐 Authentication & Security
- Teacher login
- Admin access
- Role-based control
- Secure API-based communication

---

## 🧠 Face Recognition Integration

This project includes a **Face Recognition Attendance System** integrated with the main EduConnect classroom platform.

### How it works:
1. Teacher clicks **"Take Attendance"**
2. Backend triggers the face recognition system
3. Camera captures student faces
4. System identifies students using trained face data
5. Attendance is automatically marked
6. Attendance data is synced to the main database

This integration provides:
- automation
- better accuracy
- reduced paperwork
- faster classroom operations

The integration includes:
- student ID mapping
- API synchronization
- local attendance backup
- confidence-based marking

The system was built with a dedicated integration layer connecting the face recognition module and the EduConnect platform. :contentReference[oaicite:0]{index=0}

The overall merge and integration summary shows that the project includes dedicated backend routes, controller logic, student mapping, and real-time attendance synchronization. :contentReference[oaicite:1]{index=1}

The end-to-end attendance flow—starting from the teacher dashboard and ending in the database sync—is documented as part of the face recognition integration setup. :contentReference[oaicite:2]{index=2}

---

## 🧠 Machine Learning Integration

This project also includes a **Student Performance Prediction Module**.

### Model Used:
- **RandomForestRegressor**

### Model Configuration:
- `n_estimators = 100`
- `max_depth = 10`
- `random_state = 42`

This model is trained to predict student academic performance based on features such as:
- attendance rate
- assignment score
- exam score
- course load
- previous GPA
- study hours per week
- participation score

The included training pipeline creates and trains a predictive model for student outcomes, while the saved model metadata confirms the Random Forest setup used in the project. 

---

## 🏗️ System Architecture

```text
+-----------------------------+
|      Frontend (UI)          |
|  HTML, CSS, JavaScript      |
+-------------+---------------+
              |
              v
+-----------------------------+
|    Backend (API Server)     |
|  Node.js + Express.js       |
+-------------+---------------+
              |
              v
+-----------------------------+
|   Main Database (MongoDB)   |
+-------------+---------------+
              |
              v
+-----------------------------+
| Face Recognition Module     |
| Python + OpenCV + SQLite    |
+-------------+---------------+
              |
              v
+-----------------------------+
| ML Prediction Module        |
| Python + Scikit-learn       |
+-----------------------------+
```

---

## 🛠️ Technologies Used

### 🌐 Frontend
- HTML
- CSS
- JavaScript

### ⚙️ Backend
- Node.js
- Express.js

### 🗄️ Databases
- MongoDB
- SQLite

### 🤖 AI / Machine Learning
- Python
- OpenCV
- Scikit-learn
- NumPy
- Pandas

### 🔌 Integration
- REST API
- Python backend communication
- Student ID mapping system

---

## 📂 Project Modules

## 1. User Authentication Module
This module handles login and access control.

### Features:
- Teacher login
- Admin login
- Secure session handling
- Role-based authorization

---

## 2. Student Management Module
This module stores and manages student data.

### Features:
- Add new student
- Update student details
- View student records
- Manage student profiles

### Data Includes:
- Student ID
- Name
- Email
- Department
- Class
- Attendance records

---

## 3. Teacher Management Module
This module handles teacher-related information.

### Features:
- Add teacher
- Assign classes
- Manage teacher records

---

## 4. Class Management Module
This module handles class creation and assignment.

### Features:
- Create classroom
- Assign teacher
- Add students to class
- Manage class records

---

## 5. Attendance Management Module
This module manages attendance records.

### Features:
- Manual attendance
- Automated attendance
- Attendance report generation
- Date-wise attendance tracking

---

## 6. Face Recognition Attendance Module
This is the most advanced module in the project.

### Features:
- Face detection
- Face recognition
- Attendance marking
- Camera-based attendance session
- Student face dataset training

### Functionalities:
- Recognizes registered students
- Marks attendance only when confidence threshold is met
- Stores attendance locally and syncs to main system

The trained face recognition model uses an OpenCV LBPH face recognizer configuration saved as `trainer.yml`, confirming the project’s trained recognition pipeline. :contentReference[oaicite:4]{index=4}

---

## 7. Performance Prediction Module
This module predicts student performance.

### Features:
- Predict student score/performance
- Analyze attendance impact
- Generate insights for academic tracking

---

## 8. Reports & Analytics Module
This module generates useful reports.

### Reports:
- Student attendance report
- Class attendance report
- Performance analysis report
- Daily attendance summary

---

## 🎯 Project Objectives

The main objectives of this project are:

- To automate classroom management
- To reduce manual attendance workload
- To improve attendance accuracy using face recognition
- To build a smart classroom environment
- To integrate AI into education management
- To improve student monitoring and academic insights

---

## 💡 Advantages of the Project

- Saves teacher time
- Reduces attendance fraud
- Improves attendance accuracy
- Smart and modern solution
- Centralized student and class management
- Better student performance tracking
- Scalable for schools, colleges, and institutes

---

## ⚠️ Limitations

- Requires camera access
- Face recognition may be affected by:
  - poor lighting
  - low camera quality
  - face angle issues
- Requires proper training data
- Needs initial setup and configuration

---

## 🔮 Future Enhancements

You can mention these in viva / documentation:

- Live online video classes
- Zoom / Google Meet integration
- Student mobile app
- Parent dashboard
- Face mask detection support
- Cloud deployment
- Multi-camera classroom support
- Advanced AI analytics dashboard
- Attendance alerts via email / SMS
- Real-time student engagement tracking

---

## 🗄️ Database Design

This project uses **MongoDB** as the main database and **SQLite** for local face attendance storage.

### Main Collections / Tables:
- Users
- Students
- Teachers
- Classes
- Attendance
- Face Recognition Mappings
- Performance Data

### Possible Student Fields:
- student_id
- name
- email
- class_id
- department
- attendance_percentage

### Possible Attendance Fields:
- attendance_id
- student_id
- class_id
- date
- status
- recognition_confidence

---

## 📂 Suggested Folder Structure

```text
virtual-classroom-system/
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── teacher-dashboard.html
│   ├── student-dashboard.html
│   ├── assets/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│
├── backend/
│   ├── controllers/
│   ├── routes/
│   ├── models/
│   ├── middleware/
│   ├── utils/
│   └── server.js
│
├── face_recognition/
│   ├── main.py
│   ├── take_attendance.py
│   ├── trainer.yml
│   ├── attendance.db
│   ├── educonnect_client.py
│   └── datasets/
│
├── ml_model/
│   ├── train_prediction_model.py
│   ├── model_info.json
│   └── student_performance_model.pkl
│
├── README.md
├── requirements.txt
├── package.json
└── .gitignore
```

---

## ⚙️ Installation Guide

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/virtual-classroom-system.git
cd virtual-classroom-system
```

---

## 2. Install Backend Dependencies

```bash
npm install
```

---

## 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Setup MongoDB
Make sure MongoDB is installed and running.

You can configure your MongoDB connection in your backend environment settings.

Example:

```env
MONGO_URI=mongodb://localhost:27017/virtual_classroom
PORT=5000
JWT_SECRET=your_secret_key
```

---

## 5. Run Backend Server

```bash
node server.js
```

---

## 6. Run Face Recognition Module

```bash
python main.py
```

---

## 7. Run Student Performance Model (Optional)

```bash
python train_prediction_model.py
```

---

## ▶️ Usage Guide

### Teacher Workflow
- Login to teacher dashboard
- Select class
- Click **Take Attendance**
- Camera starts capturing student faces
- Attendance is automatically marked

### Admin Workflow
- Add teachers
- Add students
- Create classes
- Monitor reports
- Manage academic records

### Student Workflow
- Login to dashboard
- View attendance
- View performance details
- Access classroom records

---

## 📸 Screenshots

You can add screenshots here later.

Example sections:

### Login Page
```md
![Login Page](screenshots/login.png)
```

### Teacher Dashboard
```md
![Teacher Dashboard](screenshots/teacher-dashboard.png)
```

### Face Recognition Attendance
```md
![Face Recognition Attendance](screenshots/attendance.png)
```

### Attendance Report
```md
![Attendance Report](screenshots/report.png)
```

---

## 🧪 Testing

This project can be tested using:

- Backend API testing
- Face recognition module testing
- Student mapping verification
- Attendance synchronization checks
- Model prediction accuracy testing

---

## 🔐 Security Considerations

- Role-based access control
- Authenticated attendance triggers
- Secure API communication
- Controlled backend execution of Python scripts
- Proper data validation

---

## 📈 Real-World Use Case

This project can be used in:

- Schools
- Colleges
- Universities
- Coaching centers
- Online education platforms
- Training institutes

It is especially useful for institutions that want to modernize classroom operations using **AI and automation**.

---

## 📝 Resume / Interview Description

You can use this in your resume:

> **Developed a Virtual Classroom System integrated with Face Recognition Attendance using Node.js, MongoDB, Python, and OpenCV. Implemented automated attendance marking, student management, class handling, and machine learning-based student performance prediction.**

---

## 🎤 Viva Explanation (Short)

If someone asks **“Explain your project”**, say:

> **“My project is a Virtual Classroom System integrated with Face Recognition Attendance. It helps manage classes, students, and attendance digitally. The main feature is that attendance is automatically marked using face recognition, and the data is synced to the main classroom platform. I also included a machine learning module to predict student performance.”**

---

## 🤝 Contribution

Contributions are welcome!

If you would like to improve this project:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is developed for **educational and academic purposes**.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [your-github-link](https://github.com/your-username)
- LinkedIn: [your-linkedin-link](https://linkedin.com/in/your-profile)

---

## ⭐ Support

If you like this project, give it a **star ⭐** on GitHub.

---
