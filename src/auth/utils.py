from jose import JWTError, jwt
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta, timezone
from src.auth.config import JWT_SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from src.auth.exceptions import TokenExpiredException

# Create a password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Secret key for encoding JWT tokens (use a secure, random key)
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # token expiration time


# Function to hash passwords
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# Function to verify hashed password with the plain password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt_token(user_data):
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode = {
        "exp": expire,
        "email": user_data.email,
        "username": user_data.username,
        "is_active": user_data.is_active,
    }
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
        return payload
    except JWTError:
        raise TokenExpiredException()
