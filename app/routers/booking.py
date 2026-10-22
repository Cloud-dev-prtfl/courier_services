from fastapi import APIRouter, HTTPException, status
from app.models.booking import OrderCreate
import uuid
import datetime

router = APIRouter(prefix="/api/booking", tags=["booking"])

services_data = {
    "Scheduled": {"base_rate": 45, "eta": "Selected time"},
    "Next Day": {"base_rate": 60, "eta": "Tomorrow"},
    "Same Day": {"base_rate": 80, "eta": "Today by 9PM"},
    "Express": {"base_rate": 120, "eta": "Within 4 hours"},
    "Instant": {"base_rate": 150, "eta": "Within 1 hour"}
}

orders_db = {}

@router.get("/services")
async def get_services(city: str = "Pune"):
    # Mocking city-based variations for base rate if needed, here returning constant
    return services_data

@router.post("/calculate-cost")
async def calculate_cost(order: OrderCreate):
    base_rate = services_data.get(order.service_type, {}).get("base_rate", 45)
    # Basic dummy calculation
    weight_fee = float(order.package.weight) * 2
    taxes = (base_rate + weight_fee) * 0.18
    total = base_rate + weight_fee + taxes
    return {
        "service_fee": base_rate + weight_fee,
        "taxes": taxes,
        "insurance_cost": 0,
        "total": total
    }

@router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    order_id = f"BRZ-{uuid.uuid4().hex[:8].upper()}"
    orders_db[order_id] = {
        "status": "Order Placed",
        "details": order.model_dump(),
        "created_at": datetime.datetime.now().isoformat()
    }
    return {"message": "Order created successfully", "order_id": order_id}
