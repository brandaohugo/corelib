import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.field_types import FieldTypes
from ..types import UNSET, Unset

T = TypeVar("T", bound="FieldPublic")


@_attrs_define
class FieldPublic:
    """
    Attributes:
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (UUID):
        updated_by (UUID):
        type_ (FieldTypes):
        id (UUID):
        ext_id (Union[None, Unset, str]):
        ext_source_id (Union[None, Unset, str]):
        key (Union[None, Unset, str]):
        ext_key (Union[None, Unset, str]):
        name (Union[None, Unset, str]):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: UUID
    updated_by: UUID
    type_: FieldTypes
    id: UUID
    ext_id: Union[None, Unset, str] = UNSET
    ext_source_id: Union[None, Unset, str] = UNSET
    key: Union[None, Unset, str] = UNSET
    ext_key: Union[None, Unset, str] = UNSET
    name: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by = str(self.created_by)

        updated_by = str(self.updated_by)

        type_ = self.type_.value

        id = str(self.id)

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

        key: Union[None, Unset, str]
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        ext_key: Union[None, Unset, str]
        if isinstance(self.ext_key, Unset):
            ext_key = UNSET
        else:
            ext_key = self.ext_key

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "type": type_,
                "id": id,
            }
        )
        if ext_id is not UNSET:
            field_dict["ext_id"] = ext_id
        if ext_source_id is not UNSET:
            field_dict["ext_source_id"] = ext_source_id
        if key is not UNSET:
            field_dict["key"] = key
        if ext_key is not UNSET:
            field_dict["ext_key"] = ext_key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        created_by = UUID(d.pop("created_by"))

        updated_by = UUID(d.pop("updated_by"))

        type_ = FieldTypes(d.pop("type"))

        id = UUID(d.pop("id"))

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

        def _parse_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_ext_key(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ext_key = _parse_ext_key(d.pop("ext_key", UNSET))

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        field_public = cls(
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            type_=type_,
            id=id,
            ext_id=ext_id,
            ext_source_id=ext_source_id,
            key=key,
            ext_key=ext_key,
            name=name,
        )

        field_public.additional_properties = d
        return field_public

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
