# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...commons.types.address import Address
from ...commons.types.full_name import FullName
from ...commons.types.phone_number import PhoneNumber
from .representative_id import RepresentativeId
from .responsibilities import Responsibilities

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class RepresentativeResponse(pydantic.BaseModel):
    id: RepresentativeId
    name: FullName
    phone: PhoneNumber
    email: str
    address: Address
    birth_date_provided: bool = pydantic.Field(alias="birthDateProvided")
    government_id_provided: bool = pydantic.Field(alias="governmentIDProvided")
    responsibilities: Responsibilities
    created_on: dt.datetime = pydantic.Field(alias="createdOn")
    updated_on: dt.datetime = pydantic.Field(alias="updatedOn")
    disabled_on: typing.Optional[dt.datetime] = pydantic.Field(alias="disabledOn")

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
