from pydantic import BaseModel, EmailStr, field_validator
import re

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not re.match(r'^\d{10}$', v):
            raise ValueError('Phone number must be exactly 10 digits')
        return v

    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain at least one numeric character')
        return v

class UserLogin(BaseModel):
    username: str # Can be email or phone
    password: str
