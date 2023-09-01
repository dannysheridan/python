# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .payment_method_schema_field_type import PaymentMethodSchemaFieldType


class PaymentMethodSchemaField(pydantic.BaseModel):
    name: str
    display_name: typing.Optional[str] = pydantic.Field(alias="displayName")
    type: PaymentMethodSchemaFieldType
    optional: bool = pydantic.Field(description="Indicates whether this field is optional")
    use_as_account_name: typing.Optional[bool] = pydantic.Field(
        alias="useAsAccountName",
        description="Indicates whether this field should be used as the name of the payment method. Only one field can be used as the name. Will set the accountName field of the payment method to the value of this field.",
    )
    use_as_account_number: typing.Optional[bool] = pydantic.Field(
        alias="useAsAccountNumber",
        description="Indicates whether this field should be used as the account number of the payment method. Only one field can be used as the account number. Will set the accountNumber field of the payment method to the value of this field.",
    )
    options: typing.Optional[typing.List[str]] = pydantic.Field(
        description="When type is 'select', provide options that can be selected"
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
