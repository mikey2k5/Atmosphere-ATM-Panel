# ATM Panel Using Flask

A simple and secure ATM Management System built with Flask, SQLite, and Docker. This project simulates core ATM banking operations through a clean web interface, allowing users to manage their accounts and perform transactions efficiently.

## Features

- User Authentication
- Account Management
- Balance Inquiry
- Cash Deposit
- Cash Withdrawal
- Transaction History
- Session-Based Access Control
- SQLite Database Integration
- Docker Support

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | Web Framework |
| SQLite | Database |
| HTML/CSS | User Interface |
| Jinja2 | Template Rendering |
| Docker | Containerization |

## Project Structure

```text
.
├── static/
├── templates/
├── instance/
│   └── atm.db
├── main.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/<your-username>/atm-panel-using-flask.git
cd atm-panel-using-flask
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python main.py
```

Open:

```text
http://localhost:5000
```

## Running with Docker

### Build Image

```bash
docker build -t atm-panel .
```

### Run Container

```bash
docker run -p 5000:5000 atm-panel
```

Visit:

```text
http://localhost:5000
```

## Core Functionalities

- Secure User Login
- View Account Balance
- Deposit Funds
- Withdraw Funds
- Track Transaction History
- Manage Account Information

## Database

The application uses SQLite for lightweight and efficient data storage.

```text
instance/atm.db
```

## Future Improvements

- Password Hashing
- Admin Dashboard
- REST API Integration
- Email Notifications
- Role-Based Access Control
- Cloud Deployment Support

## License

This project is intended for educational and learning purposes.
