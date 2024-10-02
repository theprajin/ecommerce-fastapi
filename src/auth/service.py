from fastapi import Depends
from sqlalchemy.orm import Session
from src.auth.models import User
from src.auth.schemas import UserCreate, UserLogin
from src.auth.utils import hash_password, verify_password, create_jwt_token
from src.auth.exceptions import InvalidCredentialsException
from src.common.database import get_db
from fastapi import HTTPException, status


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


class AuthService:

    @staticmethod
    async def register_user(user_data: UserCreate, db: Session):
        hashed_password = hash_password(user_data.password)
        new_user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return create_jwt_token(user_data=new_user)

    @staticmethod
    async def authenticate_user(user_data: UserLogin, db: Session):
        user = db.query(User).filter(User.email == user_data.email).first()
        if not user or not verify_password(user_data.password, user.hashed_password):
            raise InvalidCredentialsException()
        return create_jwt_token(user_data=user)
