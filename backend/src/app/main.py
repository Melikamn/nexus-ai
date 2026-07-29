from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title="Nexus AI API",
    description="Backend API for Nexus AI",
    version="0.1.0",
)

app.include_router(router)
