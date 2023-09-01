# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .invoice_notification_configuration_request import InvoiceNotificationConfigurationRequest


class NotificationConfigurationRequest_Invoice(InvoiceNotificationConfigurationRequest):
    notification_type: typing_extensions.Literal["invoice"] = pydantic.Field(alias="notificationType")

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


NotificationConfigurationRequest = typing.Union[NotificationConfigurationRequest_Invoice]
