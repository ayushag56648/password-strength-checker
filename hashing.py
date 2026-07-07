import bcrypt
import hashlib

def hash_password(password: str) -> bytes:
    """Hash a password for storage using bcrypt (includes automatic salting)."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    """Check a password against a stored bcrypt hash."""
    return bcrypt.checkpw(password.encode(), hashed)

def sha1_hex(password: str) -> str:
    """Used only for the HIBP k-anonymity check below — not for storage."""
    return hashlib.sha1(password.encode()).hexdigest().upper()