# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ...entity_types.types.approval_policy_response import ApprovalPolicyResponse
from ...entity_types.types.entity_id import EntityId
from ...entity_types.types.entity_response import EntityResponse
from ...entity_types.types.entity_user_response import EntityUserResponse
from ...payment_method_types.types.currency_code import CurrencyCode
from ...payment_method_types.types.payment_method_id import PaymentMethodId
from ...payment_method_types.types.payment_method_response import PaymentMethodResponse
from ...transaction.types.transaction_response import TransactionResponse
from .comment_response import CommentResponse
from .invoice_approver_response import InvoiceApproverResponse
from .invoice_id import InvoiceId
from .invoice_line_item_response import InvoiceLineItemResponse
from .invoice_status import InvoiceStatus


class InvoiceResponse(pydantic.BaseModel):
    id: InvoiceId
    status: InvoiceStatus
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
    payer: typing.Optional[EntityResponse]
    payment_source: typing.Optional[PaymentMethodResponse] = pydantic.Field(alias="paymentSource")
    payment_source_id: typing.Optional[PaymentMethodId] = pydantic.Field(alias="paymentSourceId")
    vendor_id: typing.Optional[EntityId] = pydantic.Field(alias="vendorId")
    vendor: typing.Optional[EntityResponse]
    payment_destination: typing.Optional[PaymentMethodResponse] = pydantic.Field(alias="paymentDestination")
    payment_destination_id: typing.Optional[PaymentMethodId] = pydantic.Field(alias="paymentDestinationId")
    payment_destination_confirmed: bool = pydantic.Field(alias="paymentDestinationConfirmed")
    has_documents: bool = pydantic.Field(alias="hasDocuments")
    comments: typing.Optional[typing.List[CommentResponse]]
    transactions: typing.Optional[typing.List[TransactionResponse]]
    line_items: typing.Optional[typing.List[InvoiceLineItemResponse]] = pydantic.Field(alias="lineItems")
    approvers: typing.List[InvoiceApproverResponse]
    approval_policy: typing.List[ApprovalPolicyResponse] = pydantic.Field(alias="approvalPolicy")
    metadata: typing.Dict[str, str] = pydantic.Field(description=("Metadata associated with this invoice.\n"))
    created_by: typing.Optional[EntityUserResponse] = pydantic.Field(
        alias="createdBy", description=("Entity user who created this invoice.\n")
    )
    processed_at: typing.Optional[dt.datetime] = pydantic.Field(alias="processedAt")
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
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
