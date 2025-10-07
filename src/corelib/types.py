import uuid
from typing import Optional, List, Dict, Any
from datetime import datetime


class BaseType:
    id: Optional[uuid.UUID] = None
    ext_id: Optional[str] = None
    ext_source_id: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    created_by: uuid.UUID
    updated_by: uuid.UUID


class ContactBase(BaseType):
    customer: "CustomerBase"
    first_name: str
    last_name: str
    email: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[str] = None


class CustomerBase(BaseType):
    name: str
    registration: Optional[str] = None
    website: Optional[str] = None
    address: Optional[str] = None
    contacts: List["ContactBase"] = None
    deals: List["DealBase"] = None


class DealBase(BaseType):
    title: Optional[str] = None
    object: Optional[str] = None
    customer: Optional[CustomerBase] = None
    contacts: List[ContactBase] = None
    active: bool = None
    stage_id: Optional[int] = None
    status: Optional[str] = None
    lost_reason: Optional[str] = None
    user_id: Optional[int] = None
    price: Optional[float] = None
    expected_close_date: Optional[datetime] = None
    custom_fields: Optional[Dict[str, Any]] = None
