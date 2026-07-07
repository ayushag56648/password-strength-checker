# Password Security Tool

Checks password strength using entropy-based scoring (zxcvbn), verifies
against known data breaches via the HaveIBeenPwned API using k-anonymity
(passwords are never sent in full), and demonstrates secure password
storage using bcrypt hashing.

## How to run
1. `python3 -m venv venv`
2. Activate it: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
3. `pip install -r requirements.txt`
4. `python main.py`