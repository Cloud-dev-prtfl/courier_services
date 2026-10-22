from fastapi import APIRouter, UploadFile, File, Form, HTTPException, status
from app.models.forms import SalesInquiry

router = APIRouter(prefix="/api/forms", tags=["forms"])

@router.post("/courier/apply")
async def courier_apply(
    full_name: str = Form(...),
    dob: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    city: str = Form(...),
    vehicle_type: str = Form(...),
    vehicle_registration: str = Form(...),
    consent: bool = Form(...),
    proof_of_identity: UploadFile = File(...)
):
    if not consent:
        raise HTTPException(status_code=400, detail="Consent is required")

    if proof_of_identity.size and proof_of_identity.size > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size must be less than 5MB")

    content_type = proof_of_identity.content_type
    if content_type not in ["application/pdf", "image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF/JPG/PNG allowed.")

    # Process and store the application (mocked)
    return {"message": "Application submitted successfully"}

@router.post("/sales/inquiry")
async def sales_inquiry(inquiry: SalesInquiry):
    # Process and store inquiry (mocked)
    return {"message": "Thank you, we will contact you shortly"}
