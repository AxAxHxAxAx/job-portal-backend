import hashlib
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    print("Original length:", len(password))  # debug
    password = hashlib.sha256(password.encode()).hexdigest()
    print("After SHA256 length:", len(password))  # should be 64
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(hashlib.sha256(plain_password.encode()).hexdigest(), hashed_password)