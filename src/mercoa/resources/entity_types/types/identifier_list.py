# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .entity_user_id import EntityUserId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class IdentifierList_RolesList(pydantic.BaseModel):
    type: typing_extensions.Literal["rolesList"]
    value: typing.List[str]

    class Config:
        frozen = True
        smart_union = True


class IdentifierList_UserList(pydantic.BaseModel):
    type: typing_extensions.Literal["userList"]
    value: typing.List[EntityUserId]

    class Config:
        frozen = True
        smart_union = True


IdentifierList = typing.Union[IdentifierList_RolesList, IdentifierList_UserList]
