from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["views"])
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/booking", response_class=HTMLResponse)
async def booking(request: Request):
    return templates.TemplateResponse(request=request, name="booking.html")

@router.get("/tracking", response_class=HTMLResponse)
async def tracking(request: Request):
    return templates.TemplateResponse(request=request, name="tracking.html")

@router.get("/courier-apply", response_class=HTMLResponse)
async def courier_apply(request: Request):
    return templates.TemplateResponse(request=request, name="courier_apply.html")

@router.get("/sales-inquiry", response_class=HTMLResponse)
async def sales_inquiry(request: Request):
    return templates.TemplateResponse(request=request, name="sales_inquiry.html")
