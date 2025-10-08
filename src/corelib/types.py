from typing import Optional
from datetime import datetime
import uuid
from sqlmodel import SQLModel



class BaseType(SQLModel, table=False):
    ext_id: Optional[str] = None
    ext_source_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    created_by: uuid.UUID
    updated_by: uuid.UUID


class ContactBase(BaseType):
    customer_id: uuid.UUID
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[str] = None


class CustomerBase(BaseType):
    name: str
    registration: Optional[str] = None
    address: Optional[str] = None


class DealBase(BaseType):
    title: str
    object: str
    customer_id: uuid.UUID
    status: Optional[str] = None
    user_id: uuid.UUID
    price: float = 0