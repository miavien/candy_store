from fastapi import APIRouter

from api_v1.views.user_views import router as users_router
from api_v1.views.product_views import router as products_router

router = APIRouter()
router.include_router(router=users_router, prefix='/users')
router.include_router(router=products_router, prefix='/products')