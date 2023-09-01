# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .currency_code import CurrencyCode
from .payment_method_schema_field import PaymentMethodSchemaField
from .payment_method_schema_id import PaymentMethodSchemaId


class PaymentMethodSchemaResponse(pydantic.BaseModel):
    id: PaymentMethodSchemaId
    name: str
    is_source: bool = pydantic.Field(
        alias="isSource", description="This payment method can be used as a payment source for an invoice"
    )
    is_destination: bool = pydantic.Field(
        alias="isDestination", description="This payment method can be used as a payment destination for an invoice"
    )
    supported_currencies: typing.List[CurrencyCode] = pydantic.Field(
        alias="supportedCurrencies", description="List of currencies that this payment method supports."
    )
    fields: typing.List[PaymentMethodSchemaField]
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
