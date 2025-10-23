import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipedrive_deal_org_id_type_0 import PipedriveDealOrgIdType0
    from ..models.pipedrive_deal_person_id_type_0 import PipedriveDealPersonIdType0


T = TypeVar("T", bound="PipedriveDeal")


@_attrs_define
class PipedriveDeal:
    """
    Attributes:
        id (Union[None, Unset, int]):
        add_time (Union[None, Unset, datetime.datetime]):
        update_time (Union[None, Unset, datetime.datetime]):
        created_by_user_id (Union[None, Unset, int]):
        last_updated_by_user_id (Union[None, Unset, int]):
        title (Union[None, Unset, str]):
        value (Union[None, Unset, float]):
        status (Union[None, Unset, str]):
        stage_id (Union[None, Unset, int]):
        org_id (Union['PipedriveDealOrgIdType0', None, Unset]):
        person_id (Union['PipedriveDealPersonIdType0', None, Unset]):
    """

    id: Union[None, Unset, int] = UNSET
    add_time: Union[None, Unset, datetime.datetime] = UNSET
    update_time: Union[None, Unset, datetime.datetime] = UNSET
    created_by_user_id: Union[None, Unset, int] = UNSET
    last_updated_by_user_id: Union[None, Unset, int] = UNSET
    title: Union[None, Unset, str] = UNSET
    value: Union[None, Unset, float] = UNSET
    status: Union[None, Unset, str] = UNSET
    stage_id: Union[None, Unset, int] = UNSET
    org_id: Union["PipedriveDealOrgIdType0", None, Unset] = UNSET
    person_id: Union["PipedriveDealPersonIdType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pipedrive_deal_org_id_type_0 import PipedriveDealOrgIdType0
        from ..models.pipedrive_deal_person_id_type_0 import PipedriveDealPersonIdType0

        id: Union[None, Unset, int]
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        add_time: Union[None, Unset, str]
        if isinstance(self.add_time, Unset):
            add_time = UNSET
        elif isinstance(self.add_time, datetime.datetime):
            add_time = self.add_time.isoformat()
        else:
            add_time = self.add_time

        update_time: Union[None, Unset, str]
        if isinstance(self.update_time, Unset):
            update_time = UNSET
        elif isinstance(self.update_time, datetime.datetime):
            update_time = self.update_time.isoformat()
        else:
            update_time = self.update_time

        created_by_user_id: Union[None, Unset, int]
        if isinstance(self.created_by_user_id, Unset):
            created_by_user_id = UNSET
        else:
            created_by_user_id = self.created_by_user_id

        last_updated_by_user_id: Union[None, Unset, int]
        if isinstance(self.last_updated_by_user_id, Unset):
            last_updated_by_user_id = UNSET
        else:
            last_updated_by_user_id = self.last_updated_by_user_id

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        value: Union[None, Unset, float]
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        status: Union[None, Unset, str]
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        stage_id: Union[None, Unset, int]
        if isinstance(self.stage_id, Unset):
            stage_id = UNSET
        else:
            stage_id = self.stage_id

        org_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, PipedriveDealOrgIdType0):
            org_id = self.org_id.to_dict()
        else:
            org_id = self.org_id

        person_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.person_id, Unset):
            person_id = UNSET
        elif isinstance(self.person_id, PipedriveDealPersonIdType0):
            person_id = self.person_id.to_dict()
        else:
            person_id = self.person_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if add_time is not UNSET:
            field_dict["add_time"] = add_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if created_by_user_id is not UNSET:
            field_dict["created_by_user_id"] = created_by_user_id
        if last_updated_by_user_id is not UNSET:
            field_dict["last_updated_by_user_id"] = last_updated_by_user_id
        if title is not UNSET:
            field_dict["title"] = title
        if value is not UNSET:
            field_dict["value"] = value
        if status is not UNSET:
            field_dict["status"] = status
        if stage_id is not UNSET:
            field_dict["stage_id"] = stage_id
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if person_id is not UNSET:
            field_dict["person_id"] = person_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipedrive_deal_org_id_type_0 import PipedriveDealOrgIdType0
        from ..models.pipedrive_deal_person_id_type_0 import PipedriveDealPersonIdType0

        d = dict(src_dict)

        def _parse_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_add_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                add_time_type_0 = isoparse(data)

                return add_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        add_time = _parse_add_time(d.pop("add_time", UNSET))

        def _parse_update_time(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                update_time_type_0 = isoparse(data)

                return update_time_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        update_time = _parse_update_time(d.pop("update_time", UNSET))

        def _parse_created_by_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        created_by_user_id = _parse_created_by_user_id(d.pop("created_by_user_id", UNSET))

        def _parse_last_updated_by_user_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        last_updated_by_user_id = _parse_last_updated_by_user_id(d.pop("last_updated_by_user_id", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_value(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_status(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_stage_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        stage_id = _parse_stage_id(d.pop("stage_id", UNSET))

        def _parse_org_id(data: object) -> Union["PipedriveDealOrgIdType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                org_id_type_0 = PipedriveDealOrgIdType0.from_dict(data)

                return org_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PipedriveDealOrgIdType0", None, Unset], data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_person_id(data: object) -> Union["PipedriveDealPersonIdType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                person_id_type_0 = PipedriveDealPersonIdType0.from_dict(data)

                return person_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PipedriveDealPersonIdType0", None, Unset], data)

        person_id = _parse_person_id(d.pop("person_id", UNSET))

        pipedrive_deal = cls(
            id=id,
            add_time=add_time,
            update_time=update_time,
            created_by_user_id=created_by_user_id,
            last_updated_by_user_id=last_updated_by_user_id,
            title=title,
            value=value,
            status=status,
            stage_id=stage_id,
            org_id=org_id,
            person_id=person_id,
        )

        pipedrive_deal.additional_properties = d
        return pipedrive_deal

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
