# Generated by Codium AI
import pytest
from pyfivetran.client import (
    FivetranClient,
    ConnectorEndpoint,
    ConnectorSchemaEndpoint,
    CertificateEndpoint,
    DestinationEndpoint,
    GroupEndpoint,
    LogEndpoint,
    RoleEndpoint,
    UserEndpoint,
    WebhookEndpoint,
)


class TestFivetranClient:

    # FivetranClient can be instantiated with an api_key and api_secret
    def test_instantiation(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"
        client = FivetranClient(api_key, api_secret)
        assert client.api_key == api_key
        assert client.api_secret == api_secret

    # FivetranClient has properties for each endpoint
    def test_properties(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"
        client = FivetranClient(api_key, api_secret)
        assert isinstance(client.connector_endpoint, ConnectorEndpoint)
        assert isinstance(client.connector_schema_endpoint, ConnectorSchemaEndpoint)
        assert isinstance(client.certificate_endpoint, CertificateEndpoint)
        assert isinstance(client.destination_endpoint, DestinationEndpoint)
        assert isinstance(client.group_endpoint, GroupEndpoint)
        assert isinstance(client.logs_endpoint, LogEndpoint)
        assert isinstance(client.role_endpoint, RoleEndpoint)
        assert isinstance(client.user_endpoint, UserEndpoint)
        assert isinstance(client.webhook_endpoint, WebhookEndpoint)

    # Each endpoint has methods for interacting with the Fivetran API
    def test_endpoint_methods(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"
        client = FivetranClient(api_key, api_secret)
        assert hasattr(client.connector_endpoint, "get_connector")
        assert hasattr(client.connector_schema_endpoint, "get_connector_schema_config")
        assert hasattr(client.certificate_endpoint, "approve_certificate")
        assert hasattr(client.destination_endpoint, "get_destination")
        assert hasattr(client.group_endpoint, "get_group")
        assert hasattr(client.logs_endpoint, "get_service")
        assert hasattr(client.role_endpoint, "list_roles")
        assert hasattr(client.user_endpoint, "get_users")
        assert hasattr(client.webhook_endpoint, "get_webhook")

    # If api_key or api_secret are not provided, FivetranClient raises an exception
    def test_missing_credentials(self):
        with pytest.raises(Exception):
            client = FivetranClient("", "")

    # If an invalid endpoint is called, FivetranClient raises an exception
    def test_invalid_endpoint(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"
        client = FivetranClient(api_key, api_secret)
        with pytest.raises(Exception):
            client.invalid_endpoint

    # If an invalid parameter is passed to a method, FivetranClient raises an exception
    def test_invalid_parameter(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"
        client = FivetranClient(api_key, api_secret)
        with pytest.raises(Exception):
            client.connector_endpoint.get_connector(invalid_parameter)