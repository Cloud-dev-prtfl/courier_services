from pydantic import BaseModel, EmailStr, constr, field_validator
from typing import Literal

class SalesInquiry(BaseModel):
    business_name: str
    contact_person: str
    email: EmailStr
    phone: str
    needs_description: str

    @field_validator('phone')
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not __import__('re').match(r'^\d{10}$', v):
            raise ValueError('Phone number must be exactly 10 digits')
        return v

    @field_validator('needs_description')
    @classmethod
    def validate_needs(cls, v: str) -> str:
        if len(v) < 50 or len(v) > 500:
            raise ValueError('Needs description must be between 50 and 500 characters')
        return v
