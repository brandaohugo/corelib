import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.deal_public_fields import DealPublicFields


T = TypeVar("T", bound="DealPublic")


@_attrs_define
class DealPublic:
    """
    Attributes:
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        created_by (UUID):
        updated_by (UUID):
        title (str):
        object_ (str):
        user_id (UUID):
        id (UUID):
        ext_id (Union[None, Unset, str]):
        ext_source_id (Union[None, Unset, str]):
        customer_id (Union[None, UUID, Unset]):
        status (Union[None, Unset, str]):
        price (Union[Unset, float]):  Default: 0.0.
        fields (Union[Unset, DealPublicFields]):
    """

    created_at: datetime.datetime
    updated_at: datetime.datetime
    created_by: UUID
    updated_by: UUID
    title: str
    object_: str
    user_id: UUID
    id: UUID
    ext_id: Union[None, Unset, str] = UNSET
    ext_source_id: Union[None, Unset, str] = UNSET
    customer_id: Union[None, UUID, Unset] = UNSET
    status: Union[None, Unset, str] = UNSET
    price: Union[Unset, float] = 0.0
    fields: Union[Unset, "DealPublicFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        created_by = str(self.created_by)

        updated_by = str(self.updated_by)

        title = self.title

        object_ = self.object_

        user_id = str(self.user_id)

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

        customer_id: Union[None, Unset, str]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        elif isinstance(self.customer_id, UUID):
            customer_id = str(self.customer_id)
        else:
            customer_id = self.customer_id

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        price = self.price

        fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "updated_at": updated_at,
                "created_by": created_by,
                "updated_by": updated_by,
                "title": title,
                "object": object_,
                "user_id": user_id,
                "id": id,
            }
        )
        if ext_id is not UNSET:
            field_dict["ext_id"] = ext_id
        if ext_source_id is not UNSET:
            field_dict["ext_source_id"] = ext_source_id
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if status is not UNSET:
            field_dict["status"] = status
        if price is not UNSET:
            field_dict["price"] = price
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deal_public_fields import DealPublicFields

        d = dict(src_dict)
        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        created_by = UUID(d.pop("created_by"))

        updated_by = UUID(d.pop("updated_by"))

        title = d.pop("title")

        object_ = d.pop("object")

        user_id = UUID(d.pop("user_id"))

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

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        price = d.pop("price", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: Union[Unset, DealPublicFields]
        if isinstance(_fields, Unset):
            fields = UNSET
        else:
            fields = DealPublicFields.from_dict(_fields)

        deal_public = cls(
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            title=title,
            object_=object_,
            user_id=user_id,
            id=id,
            ext_id=ext_id,
            ext_source_id=ext_source_id,
            customer_id=customer_id,
            status=status,
            price=price,
            fields=fields,
        )

        deal_public.additional_properties = d
        return deal_public

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
