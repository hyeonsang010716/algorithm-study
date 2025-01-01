from fastapi import APIRouter
from api.util import handle

api_router = APIRouter()
api_router.include_router(handle.router,prefix="/chat")