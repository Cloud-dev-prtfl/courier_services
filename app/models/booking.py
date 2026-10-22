from pydantic import BaseModel, confloat, constr, conint
from typing import Literal

class Address(BaseModel):
    address_line_1: str
    city: str
    state: str
    pin_code: str
    latitude: float
    longitude: float

class Package(BaseModel):
    weight: confloat(ge=0.1, le=25.0)
    length: confloat(ge=1.0)
    width: confloat(ge=1.0)
    height: confloat(ge=1.0)

class OrderCreate(BaseModel):
    pickup_address: Address
    dropoff_address: Address
    package: Package
    item_type: Literal['Food & Groceries', 'Pharmaceuticals', 'E-commerce & retail', 'Electronics', 'Office supplies', 'Flowers & gifts']
    service_type: Literal['Scheduled', 'Next Day', 'Same Day', 'Express', 'Instant']
    recipient_name: str
    recipient_phone: constr(pattern=r'^\d{10}$')
