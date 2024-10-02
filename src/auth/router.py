from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.auth.schemas import UserCreate, UserLogin, Token, UserResponse
from src.auth.service import AuthService
from src.auth.dependencies import get_current_user
from src.common.database import get_db

router = APIRouter()


@router.post("/register")
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    # Pass both user_data and db to the service method
    return await AuthService.register_user(user_data, db)


@router.post("/login")
async def login(user_data: UserLogin, db: Session = Depends(get_db)):
    return await AuthService.authenticate_user(user_data, db)


@router.get("/me", response_model=UserResponse)
async def get_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
