# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .bank_type import BankType


class BankAccountBaseRequest(pydantic.BaseModel):
    bank_name: typing.Optional[str] = pydantic.Field(alias="bankName")
    routing_number: typing.Optional[str] = pydantic.Field(alias="routingNumber")
    account_number: typing.Optional[str] = pydantic.Field(alias="accountNumber")
    plaid_public_token: typing.Optional[str] = pydantic.Field(
        alias="plaidPublicToken", description=("Public token from Plaid Link\n")
    )
    account_type: typing.Optional[BankType] = pydantic.Field(alias="accountType")

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