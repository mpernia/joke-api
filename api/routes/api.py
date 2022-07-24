from fastapi import APIRouter
from .joke import router as joke_router
from .math import router as math_router

from api.config.api import API_PREFIX

router = APIRouter(prefix=API_PREFIX)
router.include_router(joke_router)
router.include_router(math_router)
