from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud
from app.schemas.product_schemas import Product, ProductBase, ProductType
from app.config import db_helper
from app.schemas.product_schemas import CakeCreate

router = APIRouter(tags=['Products'])


@router.get('/', response_model=list[Product])
async def get_cakes(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_cakes(session=session)


@router.post('/', response_model=Product)
async def create_cake(cake_in: CakeCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_cake(session=session, cake_in=cake_in)
