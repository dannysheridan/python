# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .token_generation_entity_options import TokenGenerationEntityOptions
from .token_generation_invoice_options import TokenGenerationInvoiceOptions
from .token_generation_pages_options import TokenGenerationPagesOptions
from .token_generation_style_options import TokenGenerationStyleOptions
from .token_generation_vendor_options import TokenGenerationVendorOptions

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class TokenGenerationOptions(pydantic.BaseModel):
    expires_in: typing.Optional[str] = pydantic.Field(
        alias="expiresIn", description="Expressed in seconds or a string describing a time span. The default is 1h."
    )
    invoice: typing.Optional[TokenGenerationInvoiceOptions]
    pages: typing.Optional[TokenGenerationPagesOptions]
    style: typing.Optional[TokenGenerationStyleOptions]
    vendors: typing.Optional[TokenGenerationVendorOptions]
    entity: typing.Optional[TokenGenerationEntityOptions]

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
