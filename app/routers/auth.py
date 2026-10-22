from fastapi import APIRouter, HTTPException, status
from app.models.auth import UserSignup, UserLogin

router = APIRouter(prefix="/api/auth", tags=["auth"])

# In-memory storage for simplicity (not for production)
users_db = {}

@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def signup(user: UserSignup):
    if user.email in users_db or user.phone in users_db:
        raise HTTPException(status_code=400, detail="Email or phone already registered")

    users_db[user.email] = {"name": user.name, "phone": user.phone, "password": user.password}
    users_db[user.phone] = {"name": user.name, "email": user.email, "password": user.password}
    return {"message": "User registered successfully"}

@router.post("/login")
async def login(user: UserLogin):
    user_record = users_db.get(user.username)
    if not user_record or user_record["password"] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    return {"message": "Login successful", "user": {"name": user_record["name"]}}
