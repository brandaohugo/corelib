from enum import Enum
from typing import Optional, Dict, Any
from datetime import datetime
import uuid
from sqlmodel import SQLModel

class FieldTypes(Enum):
    string = "string"
    float = "float"
    integer = "integer"
    boolean = "boolean"
    date = "date"
    datetime = "datetime"
    time = "time"
    enum = "enum"
    json = "json"
    uuid = "uuid"


class BaseType(SQLModel, table=False):
    ext_id: Optional[str] = None
    ext_source_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    created_by: uuid.UUID
    updated_by: uuid.UUID


class FieldBase(BaseType):
    key: Optional[str] = None
    ext_key: Optional[str] = None
    name: Optional[str] = None
    type: FieldTypes


class ContactBase(BaseType):
    customer_id: Optional[uuid.UUID] = None
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
    customer_id: Optional[uuid.UUID] = None
    status: Optional[str] = None
    user_id: uuid.UUID
    price: float = 0
    fields: Dict[str, Any] = {}