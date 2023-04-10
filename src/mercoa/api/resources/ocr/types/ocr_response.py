# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...entity.types.entity_response import EntityResponse
from ...invoice.types.invoice_response import InvoiceResponse
from ...payment_method.types.bank_account_response import BankAccountResponse
from ...payment_method.types.check_response import CheckResponse


class OCRResponse(pydantic.BaseModel):
    invoice: InvoiceResponse
    vendor: EntityResponse
    check: typing.Optional[CheckResponse]
    bank_account: typing.Optional[BankAccountResponse] = pydantic.Field(alias="bankAccount")

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
