from fastapi import APIRouter

from app.api.endpoints import auth, users, render, pay

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(render.router, tags=["render"])
api_router.include_router(pay.router, prefix="/pay", tags=["pay"])