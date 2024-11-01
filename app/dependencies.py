from typing import Annotated
from fastapi import HTTPException, status, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import db_helper
from app import crud


async def user_by_id(
        user_id: Annotated[int, Path],
        session: AsyncSession = Depends(db_helper.session_dependency),
):
    user = await crud.get_user(session=session, user_id=user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with ID = {user_id} is not found',
    )
