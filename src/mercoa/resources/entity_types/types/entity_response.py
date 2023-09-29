# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .account_type import AccountType
from .entity_id import EntityId
from .entity_status import EntityStatus
from .profile_response import ProfileResponse


class EntityResponse(pydantic.BaseModel):
    id: EntityId
    name: str
    email: str
    foreign_id: typing.Optional[str] = pydantic.Field(
        alias="foreignId", description="The ID used to identify this entity in your system"
    )
    email_to: typing.Optional[str] = pydantic.Field(
        alias="emailTo",
        description="Local-part/username of the email address to which to send invoices to be added to the Invoice Inbox.",
    )
    email_to_alias: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="emailToAlias",
        description="Email inbox alias addresses. Used when forwarding emails to the emailTo address from an alias.",
    )
    owned_by_org: bool = pydantic.Field(
        alias="ownedByOrg", description="True if this entity has a direct relationship with your organization."
    )
    account_type: AccountType = pydantic.Field(alias="accountType")
    profile: ProfileResponse
    status: EntityStatus
    accepted_tos: bool = pydantic.Field(
        alias="acceptedTos", description="True if this entity has accepted the terms of service."
    )
    is_payor: bool = pydantic.Field(alias="isPayor", description="True if this entity can pay invoices.")
    is_payee: bool = pydantic.Field(alias="isPayee", description="True if this entity can receive payments.")
    created_at: dt.datetime = pydantic.Field(alias="createdAt")
    updated_at: dt.datetime = pydantic.Field(alias="updatedAt")

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
