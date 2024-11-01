from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.config import db_helper
from app import crud
from app.schemas.user_schemas import User, UserCreate, UserUpdate, UserUpdatePartial
from app.dependencies import user_by_id
from app.models.user_models import UserModel

router = APIRouter(tags=['Users'])


@router.get('/', response_model=list[User])
async def get_users(session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.get_users(session=session)


@router.get('/{user_id}/', response_model=User)
async def get_user(user: User = Depends(user_by_id)):
    return user


@router.post('/', response_model=User)
async def create_user(user_in: UserCreate, session: AsyncSession = Depends(db_helper.session_dependency)):
    return await crud.create_user(session=session, user_in=user_in)


@router.put('/{user_id}/')
async def update_user(
        user_update: UserUpdate,
        user: UserModel = Depends(user_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.update_user(
        session=session,
        user=user,
        user_update=user_update
    )


@router.patch('/{user_id}/')
async def update_user_partial(
        user_update: UserUpdatePartial,
        user: UserModel = Depends(user_by_id),
        session: AsyncSession = Depends(db_helper.session_dependency)
):
    return await crud.update_user_partial(
        session=session,
        user=user,
        user_update=user_update
    )


@router.delete('/{user_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
        session: AsyncSession = Depends(db_helper.session_dependency),
        user: UserModel = Depends(user_by_id)
) -> None:
    await crud.delete_user(session=session, user=user)
