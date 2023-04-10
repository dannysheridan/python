# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ....environment import MercoaEnvironment
from ...core.api_error import ApiError
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_headers import remove_none_from_headers
from ..entity.types.entity_id import EntityId
from .types.payment_method_id import PaymentMethodId
from .types.payment_method_request import PaymentMethodRequest
from .types.payment_method_response import PaymentMethodResponse
from .types.payment_method_type import PaymentMethodType


class PaymentMethodClient:
    def __init__(
        self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    def get_all(
        self,
        entity_id: EntityId,
        *,
        type: typing.Union[typing.Optional[PaymentMethodType], typing.List[PaymentMethodType]],
    ) -> typing.List[PaymentMethodResponse]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", f"entity/{entity_id}/paymentMethods"),
            params={"type": type},
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[PaymentMethodResponse], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, entity_id: EntityId, *, request: PaymentMethodRequest) -> PaymentMethodResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod"),
            json=jsonable_encoder(request),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentMethodResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, entity_id: EntityId, payment_method_id: PaymentMethodId) -> PaymentMethodResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod/{payment_method_id}"
            ),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentMethodResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, entity_id: EntityId, payment_method_id: PaymentMethodId) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod/{payment_method_id}"
            ),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def initiate_micro_deposits(self, entity_id: EntityId, payment_method_id: PaymentMethodId) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod/{payment_method_id}/micro-deposits"
            ),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def complete_micro_deposits(
        self, entity_id: EntityId, payment_method_id: PaymentMethodId, *, amounts: typing.List[int]
    ) -> None:
        _response = httpx.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod/{payment_method_id}/micro-deposits"
            ),
            json=jsonable_encoder({"amounts": amounts}),
            headers=remove_none_from_headers(
                {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
            ),
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPaymentMethodClient:
    def __init__(
        self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: typing.Optional[str] = None
    ):
        self._environment = environment
        self._token = token

    async def get_all(
        self,
        entity_id: EntityId,
        *,
        type: typing.Union[typing.Optional[PaymentMethodType], typing.List[PaymentMethodType]],
    ) -> typing.List[PaymentMethodResponse]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", f"entity/{entity_id}/paymentMethods"),
                params={"type": type},
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[PaymentMethodResponse], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, entity_id: EntityId, *, request: PaymentMethodRequest) -> PaymentMethodResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod"),
                json=jsonable_encoder(request),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentMethodResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, entity_id: EntityId, payment_method_id: PaymentMethodId) -> PaymentMethodResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod/{payment_method_id}"
                ),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(PaymentMethodResponse, _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, entity_id: EntityId, payment_method_id: PaymentMethodId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"entity/{entity_id}/paymentMethod/{payment_method_id}"
                ),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def initiate_micro_deposits(self, entity_id: EntityId, payment_method_id: PaymentMethodId) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(
                    f"{self._environment.value}/",
                    f"entity/{entity_id}/paymentMethod/{payment_method_id}/micro-deposits",
                ),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def complete_micro_deposits(
        self, entity_id: EntityId, payment_method_id: PaymentMethodId, *, amounts: typing.List[int]
    ) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "PUT",
                urllib.parse.urljoin(
                    f"{self._environment.value}/",
                    f"entity/{entity_id}/paymentMethod/{payment_method_id}/micro-deposits",
                ),
                json=jsonable_encoder({"amounts": amounts}),
                headers=remove_none_from_headers(
                    {"Authorization": f"Bearer {self._token}" if self._token is not None else None}
                ),
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
