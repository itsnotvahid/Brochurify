from fastapi import APIRouter
from .service_routes import router as service_router
from .socket import socket_router
router = APIRouter()
router.include_router(service_router, prefix="/service")
router.include_router(socket_router, prefix="/socket")
