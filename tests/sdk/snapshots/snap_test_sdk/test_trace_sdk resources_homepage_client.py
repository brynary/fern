# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx
import pydantic

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...environment import FernIrEnvironment
from ..commons.types.problem_id import ProblemId

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class HomepageClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PROD, client_wrapper: SyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    def get_homepage_problems(self) -> typing.List[ProblemId]:
        _response = httpx.request(
            "GET",
            urllib.parse.urljoin(f"{self._environment.value}/", "homepage-problems"),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ProblemId], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def set_homepage_problems(self, *, request: typing.List[ProblemId]) -> None:
        _response = httpx.request(
            "POST",
            urllib.parse.urljoin(f"{self._environment.value}/", "homepage-problems"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=None,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncHomepageClient:
    def __init__(self, *, environment: FernIrEnvironment = FernIrEnvironment.PROD, client_wrapper: AsyncClientWrapper):
        self._environment = environment
        self._client_wrapper = client_wrapper

    async def get_homepage_problems(self) -> typing.List[ProblemId]:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "GET",
                urllib.parse.urljoin(f"{self._environment.value}/", "homepage-problems"),
                headers=self._client_wrapper.get_headers(),
                timeout=None,
            )
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(typing.List[ProblemId], _response_json)  # type: ignore
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def set_homepage_problems(self, *, request: typing.List[ProblemId]) -> None:
        async with httpx.AsyncClient() as _client:
            _response = await _client.request(
                "POST",
                urllib.parse.urljoin(f"{self._environment.value}/", "homepage-problems"),
                json=jsonable_encoder(request),
                headers=self._client_wrapper.get_headers(),
                timeout=None,
            )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
