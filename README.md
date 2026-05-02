# 🛡️ SOC Security Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-brightgreen.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-orange.svg)](https://render.com)

<p align="center">
  <img src="https://img.shields.io/github/stars/alsaif26/soc-security-dashboard?style=social">
  <img src="https://img.shields.io/github/forks/alsaif26/soc-security-dashboard?style=social">
</p>

A professional **Security Operations Center (SOC) Dashboard** web application built with **Python Flask and SQLite**.  
Designed to demonstrate **cybersecurity monitoring concepts** with real-time dashboards, incident reporting, and threat visualization.

---

# 📋 Table of Contents
- [Live Demo](#live-demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Screenshots](#screenshots)
- [Project Structure](#project-structure)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Contributing](#contributing)
- [Support](#support)
- [About the Author](#about-the-author)
- [License](#license)

---

# 🌍 Live Demo
🔗 https://soc-security-dashboard.onrender.com

### Demo Credentials

| Username | Password |
|--------|--------|
| admin | password123 |
| cat | 1234 |

---

# ✨ Features

🔐 Secure session-based authentication  

📊 Real-time dashboard with statistics and charts  

🚨 Threat alert system (add / view / delete alerts)  

📋 Incident reporting and management  

📈 Security visualizations using Chart.js  

🕒 Live clock with modern dark UI  

📱 Responsive design for desktop and mobile browsers  

---

# 🛠️ Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Python Flask |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript |
| Charts | Chart.js |
| Deployment | Render |
| Version Control | Git + GitHub |

---

# 📸 Screenshots

Add screenshots in `/screenshots/` folder.

```
screenshots/
dashboard.png
incidents.png
login.png
```

Example:

```
![Dashboard](screenshots/dashboard.png)
![Incidents](screenshots/incidents.png)
![Login](screenshots/login.png)
```

---

# 📁 Project Structure

```
soc-security-dashboard/
│
├── app.py
├── requirements.txt
├── render.yaml
├── soc.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   └── incidents.html
│
└── static/
    ├── style.css
    └── script.js
```

---

# 🚀 Quick Start

## Prerequisites

- Python 3.8+
- Git

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/alsaif26/soc-security-dashboard.git
cd soc-security-dashboard
```

---

## 2️⃣ Create Virtual Environment (Windows)

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🎯 Usage

| Page | Route | Description |
|-----|------|-------------|
| Home | `/` | Landing page |
| Login | `/login` | User authentication |
| Dashboard | `/dashboard` | SOC monitoring overview |
| Incidents | `/incidents` | Security incident management |

---

# 🤝 Contributing

1. Fork the repository  
2. Create feature branch  

```
git checkout -b feature/AmazingFeature
```

3. Commit changes  

```
git commit -m "Add Amazing Feature"
```

4. Push branch  

```
git push origin feature/AmazingFeature
```

5. Open Pull Request

---

# 🆘 Support

If you face any issues:

GitHub Issues  
https://github.com/alsaif26/soc-security-dashboard/issues

You can also open a discussion in the repository.

---

# 👨‍💻 About the Author

Developed by **Mohammed Saif Al Sabah**  
Computer Science and Engineering (CSE) student from Bangladesh.

Interested in:

- Cybersecurity
- SOC Monitoring
- AI & Machine Learning
- Secure Software Development

This project is part of a **cybersecurity portfolio demonstrating SOC monitoring concepts**.

---

# 📝 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more details.

---
