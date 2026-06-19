# 📚 KitaabShala

A modern, lightweight web application for buying, selling, and exchanging used books. Built with Python and Flask, **KitaabShala** helps book lovers share their collection, find affordable books, and connect with other readers.

---

## ✨ Features

- **🔒 User Authentication:** Secure signup, login, and session management using `Flask-Login` and password hashing with `Bcrypt`.
- **📖 Book Listings:** Users can list their books for **Sale** or **Exchange**, specifying condition, publication date, ISBN, and price.
- **🛒 Book Marketplace:** Browse all listed books, view details, and initiate purchases/exchanges.
- **📧 Password Reset:** Secure password recovery system utilizing signed tokens (`itsdangerous`) and email integration (`Flask-Mail`).
- **👤 User Dashboard:** View and update account information, managed listed books, and track orders.

---

## 🛠️ Tech Stack

- **Backend:** [Flask](https://flask.palletsprojects.com/) (Python Web Framework)
- **Database & ORM:** [SQLite](https://sqlite.org/) with [Flask-SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/)
- **Security:** [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/) (Password hashing)
- **Forms & Validation:** [Flask-WTF](https://flask-wtf.readthedocs.io/) & [WTForms](https://wtforms.readthedocs.io/)
- **Session Management:** [Flask-Login](https://flask-login.readthedocs.io/)
- **Mailing System:** Flask-Mail

---

## 🚀 Getting Started

Follow these steps to run the application locally on your machine.

### Prerequisites

- Python 3.8 or higher installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manavgarg06/KitaabShala.git
   cd KitaabShala
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   * **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```
   * **Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure Environment Variables:**
   Open `BookShala/__init__.py` and configure your email credentials for the password reset functionality:
   ```python
   app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
   app.config['MAIL_PASSWORD'] = 'your-app-password'
   ```

6. **Run the application:**
   ```bash
   python3 main.py
   ```

The application will start running at `http://127.0.0.1:5000/`.

---

## 📂 Project Structure

```text
KitaabShala/
│
├── BookShala/              # Main application package
│   ├── templates/          # HTML templates (Jinja2)
│   ├── __init__.py         # App configuration & package init
│   ├── forms.py            # Form classes (WTForms)
│   ├── models.py           # Database models (SQLAlchemy)
│   └── routes.py           # Application routes/controllers
│
├── instance/               # Instance-specific files
│   └── bookshala.db        # SQLite database file
│
├── .gitignore              # Files to ignore in Git
├── main.py                 # Application entry point
├── Procfile                # Heroku deployment file
└── requirements.txt        # Project dependencies
```

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve KitaabShala, please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.
