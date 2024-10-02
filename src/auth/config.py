import os

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret_key_here")
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour
