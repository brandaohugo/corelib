import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipedrive_person_custom_fields_type_0 import PipedrivePersonCustomFieldsType0
    from ..models.pipedrive_person_emails_item import PipedrivePersonEmailsItem
    from ..models.pipedrive_person_org_id_type_0 import PipedrivePersonOrgIdType0
    from ..models.pipedrive_person_owner_id_type_0 import PipedrivePersonOwnerIdType0
    from ..models.pipedrive_person_phone_item import PipedrivePersonPhoneItem


T = TypeVar("T", bound="PipedrivePerson")


@_attrs_define
class PipedrivePerson:
    """
    Attributes:
        id (Union[None, Unset, int]):
        add_time (Union[None, Unset, datetime.datetime]):
        update_time (Union[None, Unset, datetime.datetime]):
        created_by_user_id (Union[None, Unset, int]):
        last_updated_by_user_id (Union[None, Unset, int]):
        name (Union[None, Unset, str]):
        first_name (Union[None, Unset, str]):
        last_name (Union[None, Unset, str]):
        emails (Union[Unset, list['PipedrivePersonEmailsItem']]):
        phone (Union[Unset, list['PipedrivePersonPhoneItem']]):
        org_id (Union['PipedrivePersonOrgIdType0', None, Unset]):
        custom_fields (Union['PipedrivePersonCustomFieldsType0', None, Unset]):
        owner_id (Union['PipedrivePersonOwnerIdType0', None, Unset]):
    """

    id: Union[None, Unset, int] = UNSET
    add_time: Union[None, Unset, datetime.datetime] = UNSET
    update_time: Union[None, Unset, datetime.datetime] = UNSET
    created_by_user_id: Union[None, Unset, int] = UNSET
    last_updated_by_user_id: Union[None, Unset, int] = UNSET
    name: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    emails: Union[Unset, list["PipedrivePersonEmailsItem"]] = UNSET
    phone: Union[Unset, list["PipedrivePersonPhoneItem"]] = UNSET
    org_id: Union["PipedrivePersonOrgIdType0", None, Unset] = UNSET
    custom_fields: Union["PipedrivePersonCustomFieldsType0", None, Unset] = UNSET
    owner_id: Union["PipedrivePersonOwnerIdType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.pipedrive_person_custom_fields_type_0 import PipedrivePersonCustomFieldsType0
        from ..models.pipedrive_person_org_id_type_0 import PipedrivePersonOrgIdType0
        from ..models.pipedrive_person_owner_id_type_0 import PipedrivePersonOwnerIdType0

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

        name: Union[None, Unset, str]
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        emails: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)

        phone: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.phone, Unset):
            phone = []
            for phone_item_data in self.phone:
                phone_item = phone_item_data.to_dict()
                phone.append(phone_item)

        org_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.org_id, Unset):
            org_id = UNSET
        elif isinstance(self.org_id, PipedrivePersonOrgIdType0):
            org_id = self.org_id.to_dict()
        else:
            org_id = self.org_id

        custom_fields: Union[None, Unset, dict[str, Any]]
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, PipedrivePersonCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        owner_id: Union[None, Unset, dict[str, Any]]
        if isinstance(self.owner_id, Unset):
            owner_id = UNSET
        elif isinstance(self.owner_id, PipedrivePersonOwnerIdType0):
            owner_id = self.owner_id.to_dict()
        else:
            owner_id = self.owner_id

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
        if name is not UNSET:
            field_dict["name"] = name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phone is not UNSET:
            field_dict["phone"] = phone
        if org_id is not UNSET:
            field_dict["org_id"] = org_id
        if custom_fields is not UNSET:
            field_dict["custom_fields"] = custom_fields
        if owner_id is not UNSET:
            field_dict["owner_id"] = owner_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipedrive_person_custom_fields_type_0 import PipedrivePersonCustomFieldsType0
        from ..models.pipedrive_person_emails_item import PipedrivePersonEmailsItem
        from ..models.pipedrive_person_org_id_type_0 import PipedrivePersonOrgIdType0
        from ..models.pipedrive_person_owner_id_type_0 import PipedrivePersonOwnerIdType0
        from ..models.pipedrive_person_phone_item import PipedrivePersonPhoneItem

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

        def _parse_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        emails = []
        _emails = d.pop("emails", UNSET)
        for emails_item_data in _emails or []:
            emails_item = PipedrivePersonEmailsItem.from_dict(emails_item_data)

            emails.append(emails_item)

        phone = []
        _phone = d.pop("phone", UNSET)
        for phone_item_data in _phone or []:
            phone_item = PipedrivePersonPhoneItem.from_dict(phone_item_data)

            phone.append(phone_item)

        def _parse_org_id(data: object) -> Union["PipedrivePersonOrgIdType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                org_id_type_0 = PipedrivePersonOrgIdType0.from_dict(data)

                return org_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PipedrivePersonOrgIdType0", None, Unset], data)

        org_id = _parse_org_id(d.pop("org_id", UNSET))

        def _parse_custom_fields(data: object) -> Union["PipedrivePersonCustomFieldsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = PipedrivePersonCustomFieldsType0.from_dict(data)

                return custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PipedrivePersonCustomFieldsType0", None, Unset], data)

        custom_fields = _parse_custom_fields(d.pop("custom_fields", UNSET))

        def _parse_owner_id(data: object) -> Union["PipedrivePersonOwnerIdType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                owner_id_type_0 = PipedrivePersonOwnerIdType0.from_dict(data)

                return owner_id_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PipedrivePersonOwnerIdType0", None, Unset], data)

        owner_id = _parse_owner_id(d.pop("owner_id", UNSET))

        pipedrive_person = cls(
            id=id,
            add_time=add_time,
            update_time=update_time,
            created_by_user_id=created_by_user_id,
            last_updated_by_user_id=last_updated_by_user_id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            emails=emails,
            phone=phone,
            org_id=org_id,
            custom_fields=custom_fields,
            owner_id=owner_id,
        )

        pipedrive_person.additional_properties = d
        return pipedrive_person

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
