# 🔐 Bruteforce Login Simulator

This is a simple ethical **brute force attack simulator** built in Python. It mimics how attackers try different username-password combinations on a login form — used for **educational and testing purposes only**.

---

## 🚀 Features

- Attempts login using POST requests to a local Flask app
- Reads usernames and passwords from text files
- Designed for safe, offline testing
- Logs successful login attempts

---

## 🛠️ Tech Stack

- Python 3
- Requests library
- Flask (for hosting fake login form)

---

## 📂 Files Included

| File | Description |
|------|-------------|
| `bruteforce.py` | Brute force attack script |
| `usernames.txt` | List of usernames to try |
| `passwords.txt` | List of passwords to try |
| `app.py` *(not in this repo)* | Flask server (in separate phishing simulator repo) |

---

## ⚙️ How to Use

1. Make sure your fake login page is running (`python3 app.py`)
2. Run the script:
   ```bash
   python3 bruteforce.py

