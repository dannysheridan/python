# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InvoiceFeesResponse(pydantic.BaseModel):
    source_payment_method_fee: float = pydantic.Field(
        alias="sourcePaymentMethodFee",
        description="Fee charged for processing the source payment method. For example, credit card interchange and acquiring fees.",
    )
    source_platform_markup_fee: float = pydantic.Field(
        alias="sourcePlatformMarkupFee", description="Additional fee charged to the payer."
    )
    destination_payment_method_fee: float = pydantic.Field(
        alias="destinationPaymentMethodFee",
        description="Fee charged for processing the destination payment method. For example, postage for a check payment.",
    )
    destination_platform_markup_fee: float = pydantic.Field(
        alias="destinationPlatformMarkupFee", description="Additional fee charged to the payee."
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
