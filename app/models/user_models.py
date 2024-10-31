from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class UserModel(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)