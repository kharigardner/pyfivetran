from __future__ import annotations # for | union syntax

from typing import List, Optional, Dict, Any
from abc import ABC, abstractmethod
from dataclasses import dataclass
from httpx import Client, Response

from pyfivetran.shed import ApiError, PaginatedApiResponse


class Endpoint(ABC):
    def __init__(self, client: Client) -> None:
        self.client = client

    def _request(self, **kwargs) -> Response:
        """
        Helper function to make an API request
        """
        built_request = self.client.build_request(**kwargs)
        response = self.client.send(built_request)

        try:
            response.raise_for_status()
        except Exception as e:
            raise ApiError(response.text) from e

        return response

    def _paginate(
        self,
        first_response: Response,
        endpoint: str,
        limit: Optional[int] = None,
    ) -> List[Response]:
        """
        Helper function to paginate through API responses

        :param first_response: The first response from the API
        :param endpoint: The endpoint to paginate
        :return: A list of responses from the API
        """

        if not limit:
            limit = 100

        try:
            first_response.raise_for_status()
        except Exception as e:
            raise ApiError(first_response.text) from e

        responses = [first_response]
        json_resp: PaginatedApiResponse = first_response.json()

        while json_resp.get("next_cursor"):
            next_response = self._request(
                url=endpoint,
                params={"cursor": json_resp.get("next_cursor"), "limit": limit},
            )

            try:
                next_response.raise_for_status()
            except Exception as e:
                raise ApiError(next_response.text) from e

            responses.append(next_response)
            json_resp = next_response.json()

        return responses


@dataclass
class ApiDataclass(ABC):
    endpoint: Endpoint

    @classmethod
    @abstractmethod
    def _from_dict(cls, endpoint, d: Dict[str, Any]) -> "ApiDataclass":
        ...

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(endpoint={self.endpoint.__class__.__name__}, fivetran_id={getattr(self, 'fivetran_id', None) or 'None'})"