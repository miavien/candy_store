from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class UserModel(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)