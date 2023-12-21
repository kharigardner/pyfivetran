from __future__ import annotations

from typing import Optional

from pyfivetran.endpoints.base import Endpoint, Client
from pyfivetran.shed import GeneralApiResponse, BASE_API_URL, API_VERSION


class LogEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        super().__init__(client)

    def create_service(
        self,
        group_id: Optional[str] = None,
        service: Optional[str] = None,
        enabled: Optional[bool] = None,
        **kwargs,
    ) -> GeneralApiResponse:
        """
        Creates a new logging service within a specified group
        in your Fivetran account.

        :param group_id: The ID of the group
        :param service: The name of the service
        :param enabled: Whether the service is enabled
        :param config: The config of the service
        :return: GeneralApiResponse
        """
        payload = dict(
            group_id=group_id, service=service, enabled=enabled, config=kwargs
        )

        return self._request(
            method="POST", url=f"{self.BASE_URL}/external-logging", json=payload
        ).json()

    def delete_service(self, log_id: str) -> GeneralApiResponse:
        """
        Deletes a logging service within a specified group
        in your Fivetran account.

        :param log_id: The ID of the service
        :return: GeneralApiResponse
        """
        return self._request(
            method="DELETE", url=f"{self.BASE_URL}/external-logging/{log_id}"
        ).json()

    def get_service(self, log_id: str) -> GeneralApiResponse:
        """
        Gets a logging service within a specified group
        in your Fivetran account.

        :param log_id: The ID of the service
        :return: GeneralApiResponse
        """
        return self._request(
            method="GET", url=f"{self.BASE_URL}/external-logging/{log_id}"
        ).json()

    def test_service(self, log_id: str) -> GeneralApiResponse:
        """
        Runs setup tests on a logging service
        in your Fivetran account.

        :param log_id: The ID of the service
        :return: GeneralApiResponse
        """
        return self._request(
            method="POST", url=f"{self.BASE_URL}/external-logging/{log_id}/test"
        ).json()

    def update_service(
        self, log_id: str, enabled: Optional[bool] = None, **kwargs
    ) -> GeneralApiResponse:
        """
        Updates a logging service within a specified group
        in your Fivetran account.

        :param log_id: The ID of the service
        :param enabled: Whether the service is enabled
        :param config: The config of the service
        :return: GeneralApiResponse
        """
        payload = dict(enabled=enabled, config=kwargs)

        return self._request(
            method="PATCH",
            url=f"{self.BASE_URL}/external-logging/{log_id}",
            json=payload,
        ).json()
