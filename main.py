import argparse
import json
import sys
import getpass  # ADD THIS
from hashing import hash_password
from breach_check import is_pwned
from zxcvbn import zxcvbn

def load_policy():
    """Load enterprise security policies from the JSON configuration file."""
    try:
        with open("policy.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Error: policy.json not found. Please create it.")
        sys.exit(1)

def check_password_strength(password: str) -> dict:
    result = zxcvbn(password)
    return {
        "score": result["score"],
        "crack_time": result["crack_times_display"]["offline_slow_hashing_1e4_per_second"],
        "feedback": result["feedback"]
    }

def main():
    # We keep argparse so the user can still use -h or --help to see instructions
    parser = argparse.ArgumentParser(description="Enterprise Security Policy Enforcement CLI")
    args = parser.parse_args()

    # USE GETPASS INSTEAD OF COMMAND LINE ARGUMENTS
    password = getpass.getpass("🔒 Enter password to securely audit (typing will be hidden): ")
    
    policy = load_policy()

    # ... (The rest of your code remains exactly the same below this line)
    # 1. Evaluate Password Entropy (Strength)
    strength = check_password_strength(password)
    print(f"Strength score: {strength['score']}/4 (crack time: {strength['crack_time']})")
    
    if strength['score'] < policy['minimum_zxcvbn_score']:
        print("❌ POLICY VIOLATION: Password entropy score is too low.")
        # Exit with an error code (standard CLI behavior for failures)
        sys.exit(1) 
    else:
        print("✅ Score meets policy requirements.")

    # 2. Check HaveIBeenPwned API
    pwned_count = is_pwned(password)
    if pwned_count is not None:
        if pwned_count > policy['max_pwned_count_allowed'] and not policy['allow_pwned_passwords']:
            print(f"❌ POLICY VIOLATION: Password found in {pwned_count:,} known data breaches.")
            sys.exit(1)
        elif pwned_count > 0:
            print(f"⚠️ Warning: Password appeared in {pwned_count:,} breaches, but policy allows it.")
        else:
            print("✅ Not found in known breach databases.")
    
    # 3. Securely Hash for Storage
    hashed = hash_password(password)
    print(f"✅ Stored hash (bcrypt): {hashed.decode()}")

if __name__ == "__main__":
    main()