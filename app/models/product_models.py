import enum
from enum import Enum
from sqlalchemy import Enum as SQLEnum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class ProductType(str, enum.Enum):
    CAKE = 'cake'
    PASTRY = 'pastry'


class PastryType(Enum):
    CROISSANT = 'croissant'
    BUN = 'bun'
    COOKIES = 'cookies'
    PIE = 'pie'


class ProductBase(Base):
    __abstract__ = True

    title: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(300), nullable=True)
    price: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[ProductType] = mapped_column(SQLEnum(ProductType), nullable=False)

    __mapper_args__ = {
        'polymorphic_on': type,
    }


class CakeModel(ProductBase):
    __tablename__ = 'product_cakes'

    weight: Mapped[float] = mapped_column(nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'cake',
    }


class PastryModel(ProductBase):
    __tablename__ = 'product_pastry'

    pastry_type: Mapped[PastryType] = mapped_column(SQLEnum(PastryType), nullable=True, default=PastryType.PIE)

    __mapper_args__ = {
        'polymorphic_identity': 'product_pastry',
    }
