from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_models import UserModel
from app.schemas.user_schemas import UserCreate


async def get_users(session: AsyncSession) -> list[UserModel]:
    stmt = select(UserModel).order_by(UserModel.id)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return list(users)


async def get_user(session: AsyncSession, user_id: int) -> UserModel | None:
    return await session.get(UserModel, user_id)


async def create_user(session: AsyncSession, user_in: UserCreate) -> UserModel:
    user = UserModel(**user_in.model_dump())
    session.add(user)
    await session.commit()
    return user
