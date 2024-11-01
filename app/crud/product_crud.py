from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product_models import CakeModel
from app.schemas.product_schemas import CakeCreate, PastryCreate, Product, ProductType


async def get_cakes(session: AsyncSession) -> list[CakeModel]:
    stmt = select(CakeModel).order_by(CakeModel.id)
    result = await session.execute(stmt)
    cakes = result.scalars().all()
    return list(cakes)


async def create_cake(session: AsyncSession, cake_in: CakeCreate) -> CakeModel:
    cake = CakeModel(**cake_in.model_dump())
    cake.type = ProductType.CAKE
    session.add(cake)
    await session.commit()
    return cake
