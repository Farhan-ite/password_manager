Password Manager (Tkinter + JSON)

A simple GUI-based Password Manager built with Python and Tkinter.
It can generate secure passwords, save them to a JSON file, and search stored credentials.

Features

Generate random strong passwords

Copy generated password to clipboard

Save website, email, and password to Data.json

Search saved credentials by website name

Simple Tkinter GUI interface

Project Structure
password-manager/
│
├── main.py          # Main Python file (your code)
├── Data.json         # Stores saved passwords
├── logo.png           # App logo image
└── README.md          # Project documentation

Requirements

Make sure you have Python installed (3.8+ recommended).

Install required packages:

pip install pyperclip


Tkinter comes pre-installed with Python on most systems.

How to Run
python main.py

How It Works
Save Password

Enter website, email, and password

Click Add

Data is saved in Data.json

Generate Password

Click Generate Password

Password is auto-filled and copied to clipboard

Search Password

Enter website name

Click Search

Email and password will show in a popup

Example Data.json Format
{
    "google.com": {
        "email": "example@gmail.com",
        "password": "abc123!@#"
    }
}

Notes

Website name is used as the unique key

If Data.json does not exist, the app will create it automatically

Tkinter messagebox titles may not show properly on macOS

Future Improvements

Encrypt stored passwords

Add delete/edit functionality

Use a database instead of JSON

Add password strength checker

Author

Abu Hurayra Farhan
