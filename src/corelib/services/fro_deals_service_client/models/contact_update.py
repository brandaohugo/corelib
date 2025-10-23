import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ContactUpdate")


@_attrs_define
class ContactUpdate:
    """
    Attributes:
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (UUID):
        updated_by (UUID):
        first_name (str):
        last_name (str):
        ext_id (Union[None, Unset, str]):
        ext_source_id (Union[None, Unset, str]):
        customer_id (Union[None, UUID, Unset]):
        email (Union[None, Unset, str]):
        phone (Union[None, Unset, str]):
        role (Union[None, Unset, str]):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: UUID
    updated_by: UUID
    first_name: str
    last_name: str
    ext_id: Union[None, Unset, str] = UNSET
    ext_source_id: Union[None, Unset, str] = UNSET
    customer_id: Union[None, UUID, Unset] = UNSET
    email: Union[None, Unset, str] = UNSET
    phone: Union[None, Unset, str] = UNSET
    role: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by = str(self.created_by)

        updated_by = str(self.updated_by)

        first_name = self.first_name

        last_name = self.last_name

        ext_id: Union[None, Unset, str]
        if isinstance(self.ext_id, Unset):
            ext_id = UNSET
        else:
            ext_id = self.ext_id

        ext_source_id: Union[None, Unset, str]
        if isinstance(self.ext_source_id, Unset):
            ext_source_id = UNSET
        else:
            ext_source_id = self.ext_source_id

        customer_id: Union[None, Unset, str]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        elif isinstance(self.customer_id, UUID):
            customer_id = str(self.customer_id)
        else:
            customer_id = self.customer_id

        email: Union[None, Unset, str]
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        phone: Union[None, Unset, str]
        if isinstance(self.phone, Unset):
            phone = UNSET
        else:
            phone = self.phone

        role: Union[None, Unset, str]
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "first_name": first_name,
                "last_name": last_name,
            }
        )
        if ext_id is not UNSET:
            field_dict["ext_id"] = ext_id
        if ext_source_id is not UNSET:
            field_dict["ext_source_id"] = ext_source_id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        created_by = UUID(d.pop("created_by"))

        updated_by = UUID(d.pop("updated_by"))

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        def _parse_ext_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ext_id = _parse_ext_id(d.pop("ext_id", UNSET))

        def _parse_ext_source_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ext_source_id = _parse_ext_source_id(d.pop("ext_source_id", UNSET))

        def _parse_customer_id(data: object) -> Union[None, UUID, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                customer_id_type_0 = UUID(data)

                return customer_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, UUID, Unset], data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_email(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        email = _parse_email(d.pop("email", UNSET))

        def _parse_phone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone = _parse_phone(d.pop("phone", UNSET))

        def _parse_role(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        role = _parse_role(d.pop("role", UNSET))

        contact_update = cls(
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            first_name=first_name,
            last_name=last_name,
            ext_id=ext_id,
            ext_source_id=ext_source_id,
            customer_id=customer_id,
            email=email,
            phone=phone,
            role=role,
        )

        contact_update.additional_properties = d
        return contact_update

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
