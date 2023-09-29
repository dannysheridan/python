# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...payment_method_types.types.currency_code import CurrencyCode


class InvoiceLineItemResponse(pydantic.BaseModel):
    id: str
    amount: typing.Optional[float] = pydantic.Field(description="Total amount of line item in major units.")
    currency: typing.Optional[CurrencyCode]
    description: typing.Optional[str]
    name: typing.Optional[str]
    quantity: typing.Optional[int]
    unit_price: typing.Optional[float] = pydantic.Field(
        alias="unitPrice", description="Unit price of line item in major units."
    )
    service_start_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceStartDate")
    service_end_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceEndDate")
    metadata: typing.Optional[typing.Dict[str, str]]
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
