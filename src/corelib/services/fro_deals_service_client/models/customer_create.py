import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomerCreate")


@_attrs_define
class CustomerCreate:
    """
    Attributes:
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (UUID):
        updated_by (UUID):
        name (str):
        ext_id (Union[None, Unset, str]):
        ext_source_id (Union[None, Unset, str]):
        registration (Union[None, Unset, str]):
        address (Union[None, Unset, str]):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: UUID
    updated_by: UUID
    name: str
    ext_id: Union[None, Unset, str] = UNSET
    ext_source_id: Union[None, Unset, str] = UNSET
    registration: Union[None, Unset, str] = UNSET
    address: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by = str(self.created_by)

        updated_by = str(self.updated_by)

        name = self.name

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

        registration: Union[None, Unset, str]
        if isinstance(self.registration, Unset):
            registration = UNSET
        else:
            registration = self.registration

        address: Union[None, Unset, str]
        if isinstance(self.address, Unset):
            address = UNSET
        else:
            address = self.address

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "name": name,
            }
        )
        if ext_id is not UNSET:
            field_dict["ext_id"] = ext_id
        if ext_source_id is not UNSET:
            field_dict["ext_source_id"] = ext_source_id
        if registration is not UNSET:
            field_dict["registration"] = registration
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        created_by = UUID(d.pop("created_by"))

        updated_by = UUID(d.pop("updated_by"))

        name = d.pop("name")

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

        def _parse_registration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        registration = _parse_registration(d.pop("registration", UNSET))

        def _parse_address(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        address = _parse_address(d.pop("address", UNSET))

        customer_create = cls(
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            name=name,
            ext_id=ext_id,
            ext_source_id=ext_source_id,
            registration=registration,
            address=address,
        )

        customer_create.additional_properties = d
        return customer_create

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
