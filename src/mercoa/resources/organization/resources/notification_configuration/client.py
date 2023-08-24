# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from .....core.api_error import ApiError
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_headers import remove_none_from_headers
from .....environment import MercoaEnvironment
from ....commons.errors.auth_header_malformed_error import AuthHeaderMalformedError
from ....commons.errors.auth_header_missing_error import AuthHeaderMissingError
from ....commons.errors.invalid_postal_code import InvalidPostalCode
from ....commons.errors.invalid_state_or_province import InvalidStateOrProvince
from ....commons.errors.unauthorized import Unauthorized
from ....entity_types.errors.entity_foreign_id_already_exists import EntityForeignIdAlreadyExists
from ....entity_types.errors.invalid_tax_id import InvalidTaxId
from ....entity_types.types.notification_type import NotificationType
from ....organization_types.types.notification_configuration_request import NotificationConfigurationRequest
from ....organization_types.types.notification_configuration_response import NotificationConfigurationResponse


class NotificationConfigurationClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    def get_all(self) -> typing.List[NotificationConfigurationResponse]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "organization/notification-configurations"),
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
            return pydantic.parse_obj_as(typing.List[NotificationConfigurationResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, notification_type: NotificationType) -> NotificationConfigurationResponse:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"organization/notification-configuration/{notification_type}"
            ),
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
            return pydantic.parse_obj_as(NotificationConfigurationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, notification_type: NotificationType, *, request: NotificationConfigurationRequest
    ) -> NotificationConfigurationResponse:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"organization/notification-configuration/{notification_type}"
            ),
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
            return pydantic.parse_obj_as(NotificationConfigurationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def reset(self, notification_type: NotificationType) -> None:
        _response = httpx.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._environment.value}/", f"organization/notification-configuration/{notification_type}"
            ),
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
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncNotificationConfigurationClient:
    def __init__(self, *, environment: MercoaEnvironment = MercoaEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token

    async def get_all(self) -> typing.List[NotificationConfigurationResponse]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "organization/notification-configurations"),
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
            return pydantic.parse_obj_as(typing.List[NotificationConfigurationResponse], _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, notification_type: NotificationType) -> NotificationConfigurationResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"organization/notification-configuration/{notification_type}"
                ),
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
            return pydantic.parse_obj_as(NotificationConfigurationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, notification_type: NotificationType, *, request: NotificationConfigurationRequest
    ) -> NotificationConfigurationResponse:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"organization/notification-configuration/{notification_type}"
                ),
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
            return pydantic.parse_obj_as(NotificationConfigurationResponse, _response_json)  # type: ignore
        if "errorName" in _response_json:
            if _response_json["errorName"] == "AuthHeaderMissingError":
                raise AuthHeaderMissingError()
            if _response_json["errorName"] == "AuthHeaderMalformedError":
                raise AuthHeaderMalformedError(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "Unauthorized":
                raise Unauthorized(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def reset(self, notification_type: NotificationType) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "DELETE",
                urllib.parse.urljoin(
                    f"{self._environment.value}/", f"organization/notification-configuration/{notification_type}"
                ),
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
            if _response_json["errorName"] == "InvalidPostalCode":
                raise InvalidPostalCode(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidStateOrProvince":
                raise InvalidStateOrProvince(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "InvalidTaxId":
                raise InvalidTaxId(pydantic.parse_obj_as(str, _response_json["content"]))  # type: ignore
            if _response_json["errorName"] == "EntityForeignIdAlreadyExists":
                raise EntityForeignIdAlreadyExists(
                    pydantic.parse_obj_as(str, _response_json["content"])  # type: ignore
                )
        raise ApiError(status_code=_response.status_code, body=_response_json)