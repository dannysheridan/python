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
    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId")
    email_to: typing.Optional[str] = pydantic.Field(alias="emailTo")
    owned_by_org: bool = pydantic.Field(alias="ownedByOrg")
    account_type: AccountType = pydantic.Field(alias="accountType")
    name: str
    email: str
    profile: ProfileResponse
    status: EntityStatus
    accepted_tos: bool = pydantic.Field(alias="acceptedTos")
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
