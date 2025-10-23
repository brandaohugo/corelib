from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.contact_public import ContactPublic


T = TypeVar("T", bound="JSONResponseModelContactPublic")


@_attrs_define
class JSONResponseModelContactPublic:
    """
    Attributes:
        data (Union[Unset, list['ContactPublic']]):
        count (Union[None, Unset, int]):
        success (Union[Unset, bool]):  Default: True.
        error (Union[None, Unset, str]):
    """

    data: Union[Unset, list["ContactPublic"]] = UNSET
    count: Union[None, Unset, int] = UNSET
    success: Union[Unset, bool] = True
    error: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()
                data.append(data_item)

        count: Union[None, Unset, int]
        if isinstance(self.count, Unset):
            count = UNSET
        else:
            count = self.count

        success = self.success

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if count is not UNSET:
            field_dict["count"] = count
        if success is not UNSET:
            field_dict["success"] = success
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.contact_public import ContactPublic

        d = dict(src_dict)
        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ContactPublic.from_dict(data_item_data)

            data.append(data_item)

        def _parse_count(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        count = _parse_count(d.pop("count", UNSET))

        success = d.pop("success", UNSET)

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        json_response_model_contact_public = cls(
            data=data,
            count=count,
            success=success,
            error=error,
        )

        json_response_model_contact_public.additional_properties = d
        return json_response_model_contact_public

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
