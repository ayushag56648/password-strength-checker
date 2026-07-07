from hashing import hash_password
from breach_check import is_pwned
from zxcvbn import zxcvbn

def check_password_strength(password: str) -> dict:
    result = zxcvbn(password)
    return {
        "score": result["score"],
        "crack_time": result["crack_times_display"]["offline_slow_hashing_1e4_per_second"],
        "feedback": result["feedback"]
    }

def main():
    password = input("Enter your password: ")

    strength = check_password_strength(password)
    print(f"Strength score: {strength['score']}/4 (crack time: {strength['crack_time']})")

    pwned_count = is_pwned(password)
    if pwned_count:
        print(f"⚠️ This password has appeared in {pwned_count:,} known data breaches.")
    else:
        print("✅ Not found in known breach databases.")

    hashed = hash_password(password)
    print(f"Stored hash (bcrypt): {hashed.decode()}")

if __name__ == "__main__":
    main()