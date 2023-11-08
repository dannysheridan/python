# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .cloud_mailin_attachment import CloudMailinAttachment
from .cloud_mailin_envelope import CloudMailinEnvelope

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class CloudMailinRequest(pydantic.BaseModel):
    headers: typing.Any
    envelope: CloudMailinEnvelope
    plain: str
    html: typing.Optional[str]
    reply_plain: typing.Optional[str]
    attachments: typing.List[CloudMailinAttachment]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
