from __future__ import annotations # for | union syntax

from typing import NamedTuple, Dict

from lazy import lazy
import httpx

from pyfivetran.endpoints import (
    CertificateEndpoint,
    ConnectorEndpoint,
    ConnectorSchemaEndpoint,
    DestinationEndpoint,
    GroupEndpoint,
    LogEndpoint,
    RoleEndpoint,
    UserEndpoint,
    WebhookEndpoint,
)
from pyfivetran.shed import GeneralApiResponse

class AuthenticationTuple(NamedTuple):
    basic: httpx.BasicAuth
    mapping: Dict[str, str]


class FivetranClient:
    """
    Interface class for Fivetran API interactions via endpoints.
    """

    def __init__(self, api_key: str, api_secret: str, **httpx_kwargs) -> None:
        if not api_key or not api_secret:
            raise ValueError("api_key and api_secret are required")
        self.api_key = api_key
        self.api_secret = api_secret
        self._client = httpx.Client(**httpx_kwargs)

    @lazy
    def account_info(self) -> GeneralApiResponse:
        """
        Returns information about current account from API key.
        """
        url = '"https://api.fivetran.com/v1/account/info"'
        return self.client.get(url).json()

    @property
    def authentication(self) -> AuthenticationTuple:
        return AuthenticationTuple(
            basic=httpx.BasicAuth(self.api_key, self.api_secret),
            mapping={"Authorization": f"Bearer {self.api_key}:{self.api_secret}"},
        )

    @property
    def client(self) -> httpx.Client:
        if not self._client.auth:
            self._client.auth = self.authentication.basic
        return self._client

    @lazy
    def connector_endpoint(self) -> ConnectorEndpoint:
        return ConnectorEndpoint(self.client)

    @lazy
    def connector_schema_endpoint(self) -> ConnectorSchemaEndpoint:
        return ConnectorSchemaEndpoint(self.client)

    @lazy
    def certificate_endpoint(self) -> CertificateEndpoint:
        return CertificateEndpoint(self.client)

    @lazy
    def destination_endpoint(self) -> DestinationEndpoint:
        return DestinationEndpoint(self.client)

    @lazy
    def group_endpoint(self) -> GroupEndpoint:
        return GroupEndpoint(self.client)

    @lazy
    def logs_endpoint(self) -> LogEndpoint:
        return LogEndpoint(self.client)

    @lazy
    def role_endpoint(self) -> RoleEndpoint:
        return RoleEndpoint(self.client)

    @lazy
    def user_endpoint(self) -> UserEndpoint:
        return UserEndpoint(self.client)

    @lazy
    def webhook_endpoint(self) -> WebhookEndpoint:
        return WebhookEndpoint(self.client)
