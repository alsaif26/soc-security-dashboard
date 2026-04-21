---
# 🛡️ SOC Security Dashboard

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-brightgreen.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Deployed on Render](https://img.shields.io/badge/Deployed-Render-orange.svg)](https://render.com)

A professional **Security Operations Center (SOC) Dashboard** web application built with Python Flask and SQLite. Designed to demonstrate cybersecurity monitoring concepts with real-time dashboards, incident reporting, and threat visualization.

## 📋 Table of Contents
- [Live Demo](#🌍-live-demo)
- [Features](#✨-features)
- [Tech Stack](#🛠️-tech-stack)
- [Screenshots](#📸-screenshots)
- [Project Structure](#📁-project-structure)
- [Quick Start](#🚀-quick-start)
- [Usage](#🎯-usage)
- [Contributing](#🤝-contributing)
- [Support](#🆘-support)
- [License](#📝-license)

## 🌍 Live Demo
🔗 [https://soc-security-dashboard.onrender.com](https://soc-security-dashboard.onrender.com)

**Demo Credentials:**
| Username | Password    |
|----------|-------------|
| admin    | password123 |
| safu     | 1234        |

## ✨ Features
- 🔐 Secure session-based authentication
- 📊 Real-time dashboard with statistics and interactive charts
- 🚨 Threat alert system (add/view/delete) with severity levels
- 📋 Incident reporting and management
- 📈 Visualizations: Weekly trends, threat distribution (Chart.js)
- 🕒 Live clock and dark theme UI
- 📱 Responsive design for modern browsers

## 🛠️ Tech Stack
| Layer      | Technology          |
|------------|---------------------|
| Backend    | Python Flask        |
| Database   | SQLite              |
| Frontend   | HTML, CSS, JS       |
| Charts     | Chart.js            |
| Deployment | Render              |
| Version Control | Git/GitHub     |

## 📸 Screenshots
Add screenshots here (recommended: place images in `/screenshots/` or root):

![Dashboard](/screenshots/dashboard.png)
![Incidents](/screenshots/incidents.png)
![Login](/screenshots/login.png)

## 📁 Project Structure
```
soc-security-dashboard/
├── app.py              # Flask application
├── requirements.txt    # Dependencies
├── render.yaml         # Render config
├── soc.db              # SQLite DB
├── templates/          # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   └── incidents.html
└── static/
    ├── style.css
    └── script.js
```

## 🚀 Quick Start
### Prerequisites
- Python 3.8+
- Git

### 1. Clone
```bash
git clone https://github.com/alsaif26/soc-security-dashboard.git
cd soc-security-dashboard
```

### 2. Virtual Environment (Windows)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install
```bash
pip install -r requirements.txt
```

### 4. Run
```bash
python app.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🎯 Usage
| Page      | Route     | Description                  |
|-----------|-----------|------------------------------|
| Home      | `/`       | Landing                      |
| Login     | `/login`  | Authentication               |
| Dashboard | `/dashboard` | Monitoring overview       |
| Incidents | `/incidents` | Report management         |

## 🤝 Contributing
1. Fork the repo
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add some AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Open Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## 🆘 Support
- Issues: [GitHub Issues](https://github.com/alsaif26/soc-security-dashboard/issues)
- Questions: Open a discussion

## 👨‍💻 About the Author
Developed by **Safu**, a Computer Science and Engineering (CSE) student. This project showcases full-stack web development skills applied to cybersecurity monitoring.

## 📝 License
MIT License - see [LICENSE](LICENSE) file (create if missing).

---

⭐ **Star the repo if helpful!** ⭐

