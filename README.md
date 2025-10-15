# 🏥 MediSched Connect

**MediSched Connect** is a Django-based medical appointment scheduling system designed to simplify the interaction between **patients** and **doctors**.  
It provides a secure and efficient platform for booking, managing, and tracking medical appointments.

---

## ✨ Features

### 👩‍⚕️ Doctors
- Create and manage availability schedules.
- View appointments booked by patients.
- Manage patient information securely.

### 👨‍💻 Patients
- Register and log in securely using **JWT authentication**.
- Browse available doctors and book appointments.
- View, reschedule, or cancel appointments.

### 🔐 Authentication & Authorization
- Secure authentication using **Django REST Framework (DRF)** and **JWT tokens**.
- Role-based access control (**Patient / Doctor / Admin**).

### ⚙️ Admin Panel
- Manage users (Doctors, Patients, Admins).
- View system data in one place.
- Control permissions and roles.

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django 5.2 |
| **API Layer** | Django REST Framework |
| **Authentication** | JWT (via `rest_framework_simplejwt`) |
| **Database** | SQLite3 (default) |
| **Frontend (Admin)** | Django Admin Interface |
| **Version Control** | Git & GitHub |

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/MediSched-Connect.git
cd MediSched-Connect
