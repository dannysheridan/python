# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .account_type import AccountType
from .profile_request import ProfileRequest


class EntityRequest(pydantic.BaseModel):
    foreign_id: typing.Optional[str] = pydantic.Field(alias="foreignId")
    email_to: typing.Optional[str] = pydantic.Field(
        alias="emailTo", description=("Email inbox address. Do not inclue the @domain.com\n")
    )
    owned_by_org: typing.Optional[bool] = pydantic.Field(alias="ownedByOrg")
    account_type: AccountType = pydantic.Field(alias="accountType")
    profile: ProfileRequest

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
