from fastapi import APIRouter, HTTPException, Path
import re
from app.routers.booking import orders_db

router = APIRouter(prefix="/api/tracking", tags=["tracking"])

@router.get("/{tracking_id}")
async def track_order(tracking_id: str = Path(..., description="The ID of the order to track")):
    if not re.match(r'^BRZ-[A-Z0-9]{8}$', tracking_id):
        raise HTTPException(status_code=400, detail="Invalid Tracking ID format or ID not found")

    order = orders_db.get(tracking_id)
    if not order:
        raise HTTPException(status_code=404, detail="Invalid Tracking ID format or ID not found")

    # Return mock tracking data
    return {
        "tracking_id": tracking_id,
        "status": order["status"],
        "historical_activity": [
            {"status": "Order Placed", "time": order["created_at"]}
        ],
        "eta": "15 mins",
        "last_updated": order["created_at"]
    }
