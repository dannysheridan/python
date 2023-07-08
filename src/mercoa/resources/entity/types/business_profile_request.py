# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.address import Address
from ...commons.types.phone_number import PhoneNumber
from .business_type import BusinessType
from .tax_id import TaxId


class BusinessProfileRequest(pydantic.BaseModel):
    email: typing.Optional[str]
    legal_business_name: str = pydantic.Field(alias="legalBusinessName")
    business_type: typing.Optional[BusinessType] = pydantic.Field(alias="businessType")
    phone: typing.Optional[PhoneNumber]
    doing_business_as: typing.Optional[str] = pydantic.Field(alias="doingBusinessAs")
    website: typing.Optional[str]
    description: typing.Optional[str]
    address: typing.Optional[Address]
    owners_provided: typing.Optional[bool] = pydantic.Field(alias="ownersProvided")
    tax_id: typing.Optional[TaxId] = pydantic.Field(alias="taxId")

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
