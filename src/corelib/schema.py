from .types import DealBase, CustomerBase, ContactBase, FieldBase
import uuid

from sqlmodel import SQLModel
from typing import Generic, TypeVar, Optional, List
from pydantic.generics import GenericModel


T = TypeVar("T")

class JSONResponseModel(GenericModel, Generic[T]):
    data: List[T] = None
    count: Optional[int] = None
    success: bool = True
    error: Optional[str] = None


# DEAL SCHEMA
class DealPublic(DealBase, SQLModel):
    id: uuid.UUID


class DealUpdate(DealBase, SQLModel):
    pass


class DealCreate(DealBase, SQLModel):
    title: str
    object: str


class DealDelete(SQLModel):
    id: uuid.UUID


# CUSTOMER SCHEMA
class CustomerPublic(CustomerBase, SQLModel):
    id: uuid.UUID


class CustomerUpdate(CustomerBase, SQLModel):
    pass


class CustomerCreate(CustomerBase, SQLModel):
    pass


class CustomerDelete(SQLModel):
    id: uuid.UUID


# CONTACT SCHEMA
class ContactPublic(ContactBase, SQLModel):
    id: uuid.UUID


class ContactUpdate(ContactBase, SQLModel):
    pass


class ContactCreate(ContactBase, SQLModel):
    pass


class ContactDelete(SQLModel):
    id: uuid.UUID



# FIELD SCHEMA
class FieldPublic(FieldBase, SQLModel):
    id: uuid.UUID


class FieldUpdate(FieldBase, SQLModel):
    pass


class FieldCreate(FieldBase, SQLModel):
    pass


class ContactDelete(SQLModel):
    id: uuid.UUID