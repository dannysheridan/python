# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from ...invoice_types.types.invoice_id import InvoiceId
from .notification_id import NotificationId
from .notification_type import NotificationType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class NotificationResponse(pydantic.BaseModel):
    id: NotificationId
    invoice_id: typing.Optional[InvoiceId] = pydantic.Field(
        alias="invoiceId",
        description="The invoice ID that this notification is related to. This field is only present for notifications related to invoices.",
    )
    type: NotificationType
    created_at: dt.datetime = pydantic.Field(alias="createdAt")

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
