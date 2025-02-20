# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .business_profile_request import BusinessProfileRequest
from .individual_profile_request import IndividualProfileRequest

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ProfileRequest(pydantic.BaseModel):
    business: typing.Optional[BusinessProfileRequest] = pydantic.Field(
        description="If this entity is a business, set this field"
    )
    individual: typing.Optional[IndividualProfileRequest] = pydantic.Field(
        description="If this entity is a individual, set this field"
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
        json_encoders = {dt.datetime: serialize_datetime}
