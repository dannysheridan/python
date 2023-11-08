# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .payment_method_base_request import PaymentMethodBaseRequest
from .payment_method_schema_id import PaymentMethodSchemaId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CustomPaymentMethodUpdateRequest(PaymentMethodBaseRequest):
    foreign_id: typing.Optional[str] = pydantic.Field(
        alias="foreignId", description="ID for this payment method in your system"
    )
    account_name: typing.Optional[str] = pydantic.Field(alias="accountName")
    account_number: typing.Optional[str] = pydantic.Field(alias="accountNumber")
    schema_id: typing.Optional[PaymentMethodSchemaId] = pydantic.Field(
        alias="schemaId",
        description="Payment method schema used for this payment method. Defines the fields that this payment method contains.",
    )
    data: typing.Optional[typing.Dict[str, str]] = pydantic.Field(
        description="Object of key/value pairs that matches the keys in the linked payment method schema."
    )

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
