# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.datetime_utils import serialize_datetime
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ...environment import MercoaEnvironment
from ..commons.errors.auth_header_malformed_error import AuthHeaderMalformedError
from ..commons.errors.auth_header_missing_error import AuthHeaderMissingError
from ..commons.errors.unauthorized import Unauthorized
from ..commons.types.entity_id import EntityId
from ..commons.types.invoice_id import InvoiceId
from ..commons.types.order_direction import OrderDirection
from .resources.approval.client import ApprovalClient, AsyncApprovalClient
from .resources.comment.client import AsyncCommentClient, CommentClient
from .resources.document.client import AsyncDocumentClient, DocumentClient
from .types.invoice_order_by_field import InvoiceOrderByField
from .types.invoice_request import InvoiceRequest
from .types.invoice_response import InvoiceResponse
from .types.invoice_status import InvoiceStatus


class InvoiceClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token
        self.approval = ApprovalClient(environment=self._environment, token=self._token)
        self.comment = CommentClient(environment=self._environment, token=self._token)
        self.document = DocumentClient(environment=self._environment, token=self._token)

    def find(
        self,
        *,
        entity_ids: typing.Union[typing.Optional[EntityId], typing.List[EntityId]],
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[InvoiceOrderByField] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[InvoiceId] = None,
        search: typing.Optional[str] = None,
        status: typing.Union[typing.Optional[InvoiceStatus], typing.List[InvoiceStatus]],
    ) -> typing.List[InvoiceResponse]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "invoices"),
            params={
                "entityIds": entity_ids,
                "startDate": serialize_datetime(start_date) if start_date is not None else None,
                "endDate": serialize_datetime(end_date) if end_date is not None else None,
                "orderBy": order_by,
                "orderDirection": order_direction,
                "limit": limit,
                "startingAfter": starting_after,
                "search": search,
                "status": status,
            },
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[InvoiceResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: InvoiceRequest) -> InvoiceResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "invoice"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, invoice_id: InvoiceId) -> InvoiceResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(self, invoice_id: InvoiceId, *, request: InvoiceRequest) -> InvoiceResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, invoice_id: InvoiceId) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_vendor_link(self, invoice_id: InvoiceId) -> str:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}/vendorlink"),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
            timeout=60,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInvoiceClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token
        self.approval = AsyncApprovalClient(environment=self._environment, token=self._token)
        self.comment = AsyncCommentClient(environment=self._environment, token=self._token)
        self.document = AsyncDocumentClient(environment=self._environment, token=self._token)

    async def find(
        self,
        *,
        entity_ids: typing.Union[typing.Optional[EntityId], typing.List[EntityId]],
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        order_by: typing.Optional[InvoiceOrderByField] = None,
        order_direction: typing.Optional[OrderDirection] = None,
        limit: typing.Optional[int] = None,
        starting_after: typing.Optional[InvoiceId] = None,
        search: typing.Optional[str] = None,
        status: typing.Union[typing.Optional[InvoiceStatus], typing.List[InvoiceStatus]],
    ) -> typing.List[InvoiceResponse]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "invoices"),
                params={
                    "entityIds": entity_ids,
                    "startDate": serialize_datetime(start_date) if start_date is not None else None,
                    "endDate": serialize_datetime(end_date) if end_date is not None else None,
                    "orderBy": order_by,
                    "orderDirection": order_direction,
                    "limit": limit,
                    "startingAfter": starting_after,
                    "search": search,
                    "status": status,
                },
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[InvoiceResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: InvoiceRequest) -> InvoiceResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "invoice"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, invoice_id: InvoiceId) -> InvoiceResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(self, invoice_id: InvoiceId, *, request: InvoiceRequest) -> InvoiceResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InvoiceResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, invoice_id: InvoiceId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_vendor_link(self, invoice_id: InvoiceId) -> str:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"invoice/{invoice_id}/vendorlink"),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
                timeout=60,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(str, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)
