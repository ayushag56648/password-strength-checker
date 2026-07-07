import requests
from hashing import sha1_hex

def is_pwned(password: str) -> int:
    """Returns the number of times this password appeared in breaches, 0 if none, None on error."""
    sha1 = sha1_hex(password)
    prefix, suffix = sha1[:5], sha1[5:]
    
    try:
        resp = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}", timeout=5)
        resp.raise_for_status()
        
        for line in resp.text.splitlines():
            hash_suffix, count = line.split(":")
            if hash_suffix == suffix:
                return int(count)
        return 0
        
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error checking breach database: {e}")
        return None