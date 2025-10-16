# password_strength_checker.py

import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Too short (must be 8+ characters)"
    if not re.search(r"[A-Z]", password):
        return "Weak: Must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Weak: Must contain at least one lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Weak: Must contain at least one digit"
    if not re.search(r"[@$!%*?&]", password):
        return "Weak: Must contain at least one special character"
    return "Strong Password ✅"

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))
