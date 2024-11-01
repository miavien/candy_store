from enum import Enum
from typing import Optional, Annotated

from annotated_types import MaxLen
from pydantic import BaseModel, Field, ConfigDict


class ProductType(str, Enum):
    CAKE = 'cake'
    PASTRY = 'pastry'


class PastryType(Enum):
    CROISSANT = 'croissant'
    BUN = 'bun'
    COOKIES = 'cookies'
    PIE = 'pie'


class ProductBase(BaseModel):
    title: Annotated[str, MaxLen(100)]
    description: Annotated[Optional[str], MaxLen(300), Field(None)]
    price: int

    model_config = ConfigDict(from_attributes=True, use_enum_values=True)


class CakeCreate(ProductBase):
    weight: Annotated[Optional[float], Field(None)]


class PastryCreate(ProductBase):
    pastry_type: PastryType


# для возврата товара
class Product(ProductBase):
    id: int
    type: ProductType

    model_config = ConfigDict(from_attributes=True)
