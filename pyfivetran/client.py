from typing import (
    TYPE_CHECKING,
    NamedTuple,
    Dict
)

from lazy import lazy
import httpx

from pyfivetran.endpoints import (
    CertificateEndpoint,
    ConnectorEndpoint,
    ConnectorSchemaEndpoint,
    DestinationEndpoint
)

class AuthenticationTuple(NamedTuple):
    basic: httpx.BasicAuth
    mapping: Dict[str, str]

class FivetranClient:
    """
    Interface class for Fivetran API interactions via endpoints.
    """
    def __init__(
            self,
            api_key: str,
            api_secret: str
    ) -> None:
        self.api_key = api_key
        self.api_secret = api_secret
        self._client = httpx.Client()

    @property
    def authentication(self) -> AuthenticationTuple:
        return AuthenticationTuple(
            basic=httpx.BasicAuth(self.api_key, self.api_secret),
            mapping={'Authorization': f'Basic {self.api_key}'}
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