from __future__ import annotations

from typing import Optional, List, Dict, Any, Sequence, Literal

from pyfivetran.endpoints.base import Endpoint, Client
from pyfivetran.shed import (
    GeneralApiResponse,
    BASE_API_URL,
    API_VERSION,
    PaginatedApiResponse,
)


class WebhookEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        super().__init__(client)

    def create_webhook(
        self,
        url: str,
        events: Optional[List[str]] = None,
        active: Optional[bool] = None,
        secret: Optional[str] = None,
        webhook_type: Literal["account", "group"] = "account",
    ) -> GeneralApiResponse:
        """
        Create a webhook for either a account or a group.

        :param url: The url of the webhook
        :param events: The events to subscribe to
        :param active: Whether the webhook is active
        :param secret: The secret of the webhook
        :param webhook_type: The type of webhook

        :return: GeneralApiResponse
        """
        payload: Dict[str, Any] = dict(url=url)

        if events:
            payload["events"] = events

        if active:
            payload["active"] = active

        if secret:
            payload["secret"] = secret

        resp = self._request(
            method="POST", url=f"{self.BASE_URL}/webhooks/{webhook_type}", json=payload
        )

        return resp.json()

    def delete_webhook(self, webhook_id: str) -> GeneralApiResponse:
        """
        Delete a webhook.

        :param webhook_id: The id of the webhook
        :return: GeneralApiResponse
        """
        resp = self._request(
            method="DELETE", url=f"{self.BASE_URL}/webhooks/{webhook_id}"
        )

        return resp.json()

    def list_webhook(
        self, limit: Optional[int] = None
    ) -> Sequence[PaginatedApiResponse]:
        """
        List all webhooks.

        :param limit: The number of records to return
        :return: Sequence[PaginatedApiResponse]
        """
        if not limit:
            limit = 100

        params = {"limit": limit}

        resp_list = self._paginate(
            first_response=self._request(
                method="GET", url=f"{self.BASE_URL}/webhooks", params=params
            ),
            endpoint=f"{self.BASE_URL}/webhooks",
            limit=limit,
        )

        return list(map(lambda x: x.json(), resp_list))

    def get_webhook(self, webhook_id: str) -> GeneralApiResponse:
        """
        Get a webhook.

        :param webhook_id: The id of the webhook
        :return: GeneralApiResponse
        """
        resp = self._request(method="GET", url=f"{self.BASE_URL}/webhooks/{webhook_id}")

        return resp.json()

    def test_webhook(self, webhook_id: str, event: str) -> GeneralApiResponse:
        """
        Test a webhook.

        :param webhook_id: The id of the webhook
        :param event: The event to test
        :return: GeneralApiResponse
        """
        resp = self._request(
            method="POST",
            url=f"{self.BASE_URL}/webhooks/{webhook_id}/test",
            json={"event": event},
        )

        return resp.json()
