from fastapi import FastAPI
from app.routers import auth, booking, tracking, forms, views

app = FastAPI(title="Courier Services Web Application")

app.include_router(views.router)
app.include_router(auth.router)
app.include_router(booking.router)
app.include_router(tracking.router)
app.include_router(forms.router)
