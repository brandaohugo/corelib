import uuid
from sqlmodel import Field, SQLModel
from sqlalchemy.ext.declarative import declared_attr
from .types import BaseType
from .utils import camel_to_snake


class BaseModel(SQLModel, table=False):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:
        return camel_to_snake(cls.__name__)

class Base(BaseType, BaseModel, table=False):
    pass


class BaseField(Base, table=False):
    key: str = Field(max_length=255)
    type: str = Field(max_length=255)

# Generic message
class Message(SQLModel):
    message: str


# JSON payload containing access token
class Token(SQLModel):
    access_token: str
    token_type: str = "bearer"


# Contents of JWT token
class TokenPayload(SQLModel):
    sub: str | None = None


class NewPassword(SQLModel):
    token: str
    new_password: str = Field(min_length=8, max_length=40)
