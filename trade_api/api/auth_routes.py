from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from auth.jwt_handler import create_jwt_token
from utils.user_store import create_user, authenticate_user

router = APIRouter()

class AuthRequest(BaseModel):
    username: str
    password: str

@router.post("/register")
def register(auth: AuthRequest):
    try:
        create_user(auth.username, auth.password)
        return {"message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(auth: AuthRequest):
    user = authenticate_user(auth.username, auth.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_jwt_token({"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
