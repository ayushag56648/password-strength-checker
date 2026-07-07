import pytest
from hashing import hash_password, verify_password, sha1_hex

def test_hashing_cycle():
    """Test that a password can be hashed and then correctly verified."""
    password = "SuperSecretPassword123!"
    hashed = hash_password(password)
    
    # It should verify correctly
    assert verify_password(password, hashed) is True
    # It should fail on a wrong password
    assert verify_password("WrongPassword!", hashed) is False

def test_sha1_hex_formatting():
    """Test that the SHA-1 function returns an uppercase hex string."""
    password = "hello"
    # The SHA-1 for "hello" is known
    expected_hash = "AAF4C61DDCC5E8A2DABEDE0F3B482CD9AEA9434D"
    assert sha1_hex(password) == expected_hash