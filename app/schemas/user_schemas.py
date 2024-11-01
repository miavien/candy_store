from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserUpdate(UserCreate):
    pass


class UserUpdatePartial(UserCreate):
    username: str | None = None
    email: EmailStr | None = None
    password: str | None = None


class User(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
