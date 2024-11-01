from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user_models import UserModel
from app.schemas.user_schemas import UserCreate, UserUpdate, UserUpdatePartial


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


async def update_user(
        session: AsyncSession,
        user: UserModel,
        user_update: UserUpdate
) -> UserModel:
    for name, value in user_update.model_dump().items():
        setattr(user, name, value)
    await session.commit()
    return user


async def update_user_partial(
        session: AsyncSession,
        user: UserModel,
        user_update: UserUpdatePartial
) -> UserModel:
    for name, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, name, value)
    await session.commit()
    return user


async def delete_user(session: AsyncSession, user: UserModel) -> None:
    await session.delete(user)
    await session.commit()