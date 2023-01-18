from fastapi import APIRouter

from .auth import router as auth_router
from .requests_options import router as request_options_router

router = APIRouter()
router.include_router(request_options_router)
router.include_router(auth_router)
