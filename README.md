#📋 TABLE OF CONTENTS

Project Overview

.Working Flow — All Dashboards
.Student Dashboard Flow
.Teacher Dashboard Flow
.HOD Dashboard Flow
.Principal Dashboard Flow
.Admin Dashboard Flow
.Meeting Room Flow
Q&A — Frontend
Q&A — Backend
Q&A — Student Dashboard
Q&A — Teacher Dashboard
Q&A — HOD Dashboard
Q&A — Meeting Room & Jitsi
Q&A — Grade Prediction & ML
Q&A — Security & Authentication

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

## 🎓 Student Dashboard Flow
The student dashboard is the learning hub for every enrolled student. Here is the complete step-by-step flow:

Step 1 — Login

.Student goes to the login page, enters email, password, and selects role "Student"

.Backend checks the email and password, matches the role from MongoDB

.If valid, a JWT token is generated and stored in localStorage

.Student is redirected to student-dashboard.html

Step 2 — Dashboard Overview (Stats)

.On page load, frontend sends API calls to backend with the JWT token

.4 stat boxes are loaded: Enrolled Courses, Attendance Rate, Pending Assignments, Average Grade
 Pending assignments count is calculated by checking if a submission exists for each assignment
 
Step 3 — Upcoming Classes

.Frontend polls the backend every 5 seconds for class data

.If teacher has started a meeting (meetingLink exists in database), a "Join" button appears automatically — no page refresh needed

.If class is scheduled but teacher hasn't started, it shows "Waiting for teacher" (gray, disabled)

.If meeting has ended, it shows "Class Completed" (green, disabled)

Step 4 — Assignments

"Pending" tab: Shows assignments that have no submission in database

"Completed" tab: Shows assignments where a submission record exists

Student clicks "Submit" → file upload modal opens → file sent to backend → submission saved

Pending count updates automatically after submission

Step 5 — Grades

.Student enters semester CGPA values (0–10 scale) in input boxes

.Backend calculates overall GPA as average of all filled semesters

.Chart.js draws an animated line graph showing CGPA trend

.A predicted next semester CGPA is shown (dashed purple line) using linear regression

Step 6 — Resources

.Teacher-uploaded files appear here

.PDFs open with PDF.js (full page viewer), Word files with Mammoth.js, Excel with SheetJS

.Student can also download any file

Step 7 — Messages

.Student sees inbox messages from teachers, HODs, and the system

.Can reply to messages

.Meeting notifications also arrive here when teacher starts a class

Step 8 — Attendance

.Shows overall attendance percentage

Per-class breakdown with status (Excellent / Good / Needs Improvement)
---

## 👨‍🏫 Teacher Dashboard Flow

The teacher dashboard gives faculty full control over classes, students, assignments, and resources.

Step 1 — Login

Teacher logs in with role "Teacher"
JWT token is stored with the teacher's ID and role
Step 2 — Overview

4 stat cards: Classes Teaching, Total Students, Pending Assignments, Class Attendance
"My Assigned Subjects" list shows all subjects HOD has assigned to this teacher
Step 3 — Schedule a Class

Teacher clicks "Update Mode" on a subject card
A modal opens to select Virtual (with Date & Time) or Physical (with Room number)
On saving, the class record in MongoDB is updated with mode, date, and time
Students enrolled in that class receive a notification: "Your class is scheduled for [date] at [time]"
Student dashboard immediately shows "Waiting for teacher" status
Step 4 — Start a Meeting

Teacher clicks "Start Class" button
Backend creates a Meeting record in MongoDB with a unique room code (e.g., abc-defg-hij)
A meeting link is saved to the Class record so student dashboard can detect it
All students get a message notification with the meeting link
Within 5 seconds, the "Join" button appears on every enrolled student's dashboard
Step 5 — Inside the Meeting

Teacher's Jitsi iframe loads automatically (no extra click needed)
Students who click "Join" go to a lobby, then submit a join request
Teacher sees a red badge on the Participants panel showing how many students are waiting
Teacher clicks "Accept" → student automatically joins (no rejoin needed)
Step 6 — End Meeting

Teacher clicks "End" button → confirms in modal
Backend sets meeting status to "ended"
Meeting link is cleared from database (3 layers of clearing)
All students' dashboards show "Class Completed" within 5–10 seconds
Step 7 — Assignments & Grading

Teacher creates assignments with title, description, deadline, max marks, and optional file
Students submit files, teacher sees all submissions
Teacher gives marks → grade saved to Submission record → student's "Completed" tab updates
Step 8 — Student Analytics

Teacher views student performance cards with year-wise CGPA
At-risk students (CGPA < 7.5) are highlighted in red
Safe students (CGPA > 8.0) are highlighted in green
Prediction model shows expected performance
---

🏛️ HOD Dashboard Flow

The HOD (Head of Department) has all the teacher's powers plus department-level management.

Step 1 — Login

HOD logs in with role "HOD"
HOD has both teacher-level access and department-level access
Step 2 — Department Overview

4 stat cards: Faculty Members, Active Courses, Department Students, Avg Department CGPA
"My Assigned Subjects" — HOD can also teach classes directly (same flow as teacher)
Department activity feed shows recent actions
Step 3 — Faculty Management

HOD views all teachers in the department
Can assign subjects to specific teachers
Can view teacher performance and workload
Step 4 — Student Performance Monitoring

HOD sees all department students with year-wise CGPA
Color-coded: red = at-risk (CGPA < 7.5), green = safe (CGPA > 8.0)
Clicking "View" opens a beautiful purple gradient student detail card with:
Year 1 CGPA (average of Sem 1 + Sem 2)
Year 2 CGPA (average of Sem 3 + Sem 4)
Year 3 CGPA (average of Sem 5 + Sem 6)
Year 4 CGPA (average of Sem 7 + Sem 8)
Animated prediction line (next year's expected CGPA)
Step 5 — Hosting Department Meetings

HOD can start meetings and invite all department teachers
HOD can also approve student join requests (same as teacher)
HOD can end meetings for the entire department
Step 6 — Assignments

HOD creates department-wide assignments visible to all enrolled students
Can view and grade all student submissions
Step 7 — Announcements from Principal

HOD receives and can view all Principal announcements
Filter by priority (High / Medium / Low)
Step 8 — Event Requests

HOD submits event requests to Principal
Principal approves/declines
HOD gets a notification about the decision
---
👨‍💼 Principal Dashboard Flow

The Principal (Managing Authority) has full oversight of the entire institution.

Step 1 — Login

Principal logs in with role "managing_authority"
Has the highest access level (except system config which is admin-only)
Step 2 — Institutional Overview

4 stat cards: Total Students, Total Teachers, Total Departments, Average CGPA
College Performance Overview: table showing each department's average CGPA
Recent Activity feed: latest actions happening across the college
Step 3 — Department Management

View all departments with HOD name, faculty count, student count, status
Add new department: enters name, selects program (B.Tech / BCA etc.), creates HOD account
HOD account is auto-created with login credentials instantly
Edit department: can change HOD, update details
Step 4 — Faculty Management

View all faculty (teachers + HODs) college-wide with department info
Add new teacher: name, department, email, password — account created instantly
Direct message any teacher from this panel
Step 5 — Student Monitoring

Students grouped by department in colored collapsible boxes
Each student row: Roll No., Name, Year 1–4 CGPA, Average CGPA, Status
Export Report button downloads a CSV file of all student data
Step 6 — Announcements

Principal creates announcements that appear on ALL dashboards (students, teachers, HODs)
Sets priority: High (red) / Medium (orange) / Low (green)
Can edit and delete announcements anytime
Step 7 — Meeting Room

Principal hosts meetings with all HODs simultaneously
Meeting notification sent to every HOD in the system
Step 8 — Event Approvals

HODs submit event requests
Principal sees all pending requests with Approve/Decline buttons
On approval, HOD gets a notification automatically
---
🔧 Admin Dashboard Flow

The Admin is the technical system manager — they set up the structure that everyone else uses.

Step 1 — Login

Admin logs in with role "admin"
Has complete system access including all collections
Step 2 — Programs Management

Admin creates academic programs (e.g., B.Tech, BCA, MCA)
Sets program name, code, duration (years), total semesters
Programs appear in all dropdowns across the system (e.g., Add Department, Add Student)
Step 3 — Department Management

Admin can create and manage all departments
Links each department to a program
Assigns HOD to each department
Step 4 — User Management

Complete user table with filters by role and department
Add User form: enters name, selects role, program, department, email, password
Auto Roll Number: system automatically picks the next available roll number per program
Example: If last B.Tech student is Roll 43, next one gets Roll 44
Delete user with confirmation dialog
Step 5 — Subjects Catalog

Admin creates the master subject list
Links subjects to departments, programs, and semesters
These subjects are then assigned to teachers by HODs
Step 6 — Activity Logs

Full system audit trail: every login, assignment creation, grade update, meeting start — all logged
Filter by date range to track specific days
Each log shows: User Name, Action, Description, IP Address, Status (success/failed)
Step 7 — Reports

System-wide performance reports
Export functionality for data analysis
---
🎥 Meeting Room Flow

The meeting room is EduConnect's built-in virtual classroom — designed to work exactly like Google Meet.

Why Jitsi was chosen — explained simply: Jitsi Meet is a free, open-source video conferencing platform. Instead of building video/audio from scratch (which requires complex WebRTC servers, STUN/TURN infrastructure, and months of development), we embed Jitsi's public server inside our own meeting room page. This gives us:

Free HD video/audio with zero cost
Global infrastructure that works from any country
WebRTC peer-to-peer connections (no server bottleneck)
Built-in screen share, raise hand, mic/camera controls
We only had to build the custom approval system and UI around it
Step 1 — Teacher Creates Meeting

Teacher clicks "Start Class" on the subject card
Backend generates a unique room code like abc-defg-hij
A full meeting link is built: https://educonnect-2025.netlify.app/meeting-room.html?room=abc-defg-hij
This link is saved to the Class record in MongoDB
All enrolled students get a message notification
Step 2 — Student Dashboard Detects Meeting

Student dashboard polls the backend every 5 seconds
When meetingLink is found in the class record, "Join" button appears automatically
No page refresh needed — it's completely automatic
Step 3 — Student Goes to Lobby

Student clicks "Join" → redirected to meeting-room.html?room=abc-defg-hij
A lobby screen shows: camera preview, mic/camera toggle, "Join Now" button
Student sees themselves before entering
Step 4 — Student Sends Join Request

Student clicks "Join Now" → backend API call adds student to pendingApprovals[]
Student sees "Waiting for Teacher Approval" screen
Frontend polls every 3 seconds to check if approval status changed
Step 5 — Teacher Approves

Teacher's meeting room shows a red badge on Participants icon (count of pending students)
Teacher opens Participants panel → sees student name with "Accept" / "Decline" buttons
Teacher clicks "Accept" → backend sets student status to "accepted"
Step 6 — Auto-Connect (The Key Fix)

After approving, teacher's Jitsi iframe automatically reloads after 1.5 seconds
This is the key fix for the "need to rejoin" problem — Jitsi uses WebRTC peer-to-peer connections. If host and student join at different times, they don't discover each other. By reloading the host's iframe at the same time as the student enters, both join the Jitsi room at the same moment, Jitsi detects both peers, and the video connection is established automatically.
Student enters the meeting room 2 seconds after approval
Total time from approval to video: ~4 seconds
Step 7 — Inside the Meeting

Jitsi handles video/audio/screen share — all built in
Chat is stored in MongoDB, polled every 3 seconds
Participants list is polled every 5 seconds
Any teacher/HOD in the meeting can approve new join requests
Step 8 — End Meeting

Teacher clicks "End" → confirmation dialog
Backend marks meeting as ended, sets isActive = false
3-Layer clearing system removes meeting link from all class records:
Layer 1: Clear by classId
Layer 2: Clear by matching meetingLink URL
Layer 3: Clear by room code pattern (regex)
All students' dashboards show "Class Completed" within 5–10 seconds
Old meeting link becomes invalid — cannot be used again


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
![Login page  ](https://github.com/user-attachments/assets/670e09f1-4740-4af6-8d1f-0e59976f5137)

```

### Registration Page
```md
![Registration page  ](https://github.com/user-attachments/assets/8cbf58df-70de-4ac8-951e-d24111e16363)

```

### Front page 
```md
![front side](https://github.com/user-attachments/assets/6001942c-8e68-45a2-9b1d-73128d08522e)

```

### Teacher Dashboard
```md
![Teacher](https://github.com/user-attachments/assets/f66637db-5e8e-4e24-a461-baaedcd164e1)

```

### Hod Dashboard
```md
![Hod](https://github.com/user-attachments/assets/b3890b44-04a2-46e3-98a5-48b00cc787c8)

```

### Admin Dashboard
```md
![Admin](https://github.com/user-attachments/assets/a366d523-c80a-4f44-91da-c7a2a177c451)

```

### Face Recognition Attendance
```md
![Attendance verification system ](https://github.com/user-attachments/assets/309157e6-ff62-4ac8-a318-cdc61401d2ce)
![Live Attendance](https://github.com/user-attachments/assets/ca4b937b-4858-49a1-b6ab-add023531bbe)

```

### Attendance Report
```md
![Take The Attendance And Update on Database](https://github.com/user-attachments/assets/e8ab349f-8756-4bb3-b333-616140325f55)

```

### Performance Prediction & suggestion
```md
![Prediction model  ](https://github.com/user-attachments/assets/423973f3-3ac6-43c2-8338-55618fa41927)

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
- GitHub: [your-github-link](https://github.com/soumen-gorai)
- LinkedIn: [your-linkedin-link](https://www.linkedin.com/in/soumen-gorai-a726a924a/)

---

## ⭐ Support

If you like this project, give it a **star ⭐** on GitHub.

---
