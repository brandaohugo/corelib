from .types import DealBase, CustomerBase, ContactBase
import uuid

from sqlmodel import SQLModel


# DEAL SCHEMA
class DealPublic(DealBase, SQLModel):
    id: uuid.UUID


class DealInListPublic(DealPublic):
    pass


class DealsPublic(SQLModel):
    data: list[DealInListPublic]
    count: int

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


class CustomerInListPublic(CustomerPublic):
    pass

class CustomersPublic(CustomerBase, SQLModel):
    data: list[CustomerInListPublic]
    count: int

class CustomerUpdate(CustomerBase, SQLModel):
    pass


# CONTACT SCHEMA
class ContactPublic(ContactBase, SQLModel):
    id: uuid.UUID


class ContactInListPublic(ContactPublic):
    pass

class ContactsPublic(ContactBase, SQLModel):
    data: list[ContactInListPublic]
    count: int

class ContactUpdate(ContactBase, SQLModel):
    pass