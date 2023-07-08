# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...commons.types.entity_id import EntityId
from ...commons.types.entity_user_id import EntityUserId
from ...commons.types.invoice_id import InvoiceId
from ...payment_method.types.currency_code import CurrencyCode
from .assigned_approver import AssignedApprover
from .invoice_line_item_request import InvoiceLineItemRequest
from .invoice_status import InvoiceStatus


class InvoiceRequest(pydantic.BaseModel):
    status: typing.Optional[InvoiceStatus]
    amount: typing.Optional[float]
    currency: typing.Optional[CurrencyCode]
    invoice_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="invoiceDate", description=("Date the invoice was created.\n")
    )
    deduction_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="deductionDate", description=("Date when funds will be deducted from payer's account.\n")
    )
    funded_date: typing.Optional[dt.datetime] = pydantic.Field(
        alias="fundedDate", description=("Date of funds settlement.\n")
    )
    due_date: typing.Optional[dt.datetime] = pydantic.Field(alias="dueDate", description=("Due date of invoice.\n"))
    invoice_number: typing.Optional[str] = pydantic.Field(alias="invoiceNumber")
    note_to_self: typing.Optional[str] = pydantic.Field(alias="noteToSelf")
    service_start_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceStartDate")
    service_end_date: typing.Optional[dt.datetime] = pydantic.Field(alias="serviceEndDate")
    payer_id: typing.Optional[EntityId] = pydantic.Field(alias="payerId")
    payment_source_id: typing.Optional[InvoiceId] = pydantic.Field(alias="paymentSourceId")
    approvers: typing.Optional[typing.List[AssignedApprover]] = pydantic.Field(
        description=("Set approvers for this invoice.\n")
    )
    vendor_id: typing.Optional[EntityId] = pydantic.Field(alias="vendorId")
    payment_destination_id: typing.Optional[InvoiceId] = pydantic.Field(alias="paymentDestinationId")
    line_items: typing.Optional[typing.List[InvoiceLineItemRequest]] = pydantic.Field(alias="lineItems")
    metadata: typing.Optional[typing.Dict[str, str]] = pydantic.Field(
        description=(
            "Metadata associated with this invoice. You can specify up to 10 keys, with key names up to 40 characters long and values up to 200 characters long.\n"
        )
    )
    uploaded_image: typing.Optional[str] = pydantic.Field(
        alias="uploadedImage",
        description=("Base64 encoded image or PDF of invoice. PNG, JPG, and PDF are supported. 10MB max.\n"),
    )
    created_by_id: typing.Optional[EntityUserId] = pydantic.Field(
        alias="createdById", description=("ID of entity user who created this invoice.\n")
    )

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
