# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...payment_method_types.types.payment_method_type import PaymentMethodType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MetadataShowConditions(pydantic.BaseModel):
    has_options: typing.Optional[bool] = pydantic.Field(
        alias="hasOptions", description="Show this field only if the entity has values set for the metadata key."
    )
    has_document: typing.Optional[bool] = pydantic.Field(
        alias="hasDocument", description="Show this field only if a document has been attached."
    )
    payment_source_types: typing.Optional[typing.List[PaymentMethodType]] = pydantic.Field(
        alias="paymentSourceTypes", description="Show this field only if the payment source type is in this list."
    )
    payment_source_custom_schema_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="paymentSourceCustomSchemaIds",
        description="Show this field only if the payment source schema ID is in this list of payment source schema IDs. This is only applicable if paymentSourceTypes contains CUSTOM.",
    )
    payment_destination_types: typing.Optional[typing.List[PaymentMethodType]] = pydantic.Field(
        alias="paymentDestinationTypes",
        description="Show this field only if the payment destination type is in this list.",
    )
    payment_destination_custom_schema_ids: typing.Optional[typing.List[str]] = pydantic.Field(
        alias="paymentDestinationCustomSchemaIds",
        description="Show this field only if the payment destination schema ID is in this list of payment destination schema IDs. This is only applicable if paymentDestinationTypes contains CUSTOM.",
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
