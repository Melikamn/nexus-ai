from fastapi import APIRouter

from app.api.routes.health import router as health_router
from app.api.routes.root import router as root_router

router = APIRouter()

router.include_router(root_router)
router.include_router(health_router)
