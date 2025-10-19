# 🔒 Password Strength Checker (Python)

A simple Python program that checks the strength of a password based on common security rules such as length, uppercase, lowercase, digits, and special characters.

---

## 📘 Features

✅ Checks if the password:
- Has **at least 8 characters**
- Contains **uppercase letters (A–Z)**
- Contains **lowercase letters (a–z)**
- Includes **at least one number (0–9)**
- Includes **at least one special character** (`@ $ ! % * ? &`)

✅ Gives clear feedback on what’s missing  
✅ Easy to run — no external libraries required  

---

## 🧠 How It Works

The program uses **regular expressions (regex)** to test your password for each rule.  
If any condition fails, it immediately tells you what’s missing.  
Otherwise, it returns:  
> **Strong Password ✅**

---

## 🚀 How to Run

1. Make sure **Python 3** is installed.  
2. Save the script as `password_strength_checker.py`.  
3. Open a terminal (or command prompt) in the same folder.
4. Run the program:

```bash
python password_strength_checker.py
