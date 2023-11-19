import pytest

import httpx

from pyfivetran import FivetranClient

class TestFivetranClient:

    # FivetranClient can be initialized with an api_key and api_secret.
    def test_initialize_with_api_key_and_api_secret(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"

        client = FivetranClient(api_key, api_secret)

        assert client.api_key == api_key
        assert client.api_secret == api_secret

    # The authentication property returns a tuple with basic authentication and a mapping.
    def test_authentication_property(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"

        client = FivetranClient(api_key, api_secret)

        auth = client.authentication
        assert isinstance(auth, tuple)
        assert isinstance(auth.basic, httpx.BasicAuth)
        assert isinstance(auth.mapping, dict)

    # The client property returns an httpx client with basic authentication.
    def test_client_property(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"

        client = FivetranClient(api_key, api_secret)

        http_client = client.client
        assert isinstance(http_client, httpx.Client)
        assert isinstance(http_client.auth, httpx.BasicAuth)

    # If api_key or api_secret are None, FivetranClient raises an exception.
    def test_initialize_with_none_api_key_or_api_secret(self):
        with pytest.raises(Exception):
            client = FivetranClient(None, "your_api_secret")

        with pytest.raises(Exception):
            client = FivetranClient("your_api_key", None)

    # If the client is not authenticated, FivetranClient raises an exception.
    def test_client_not_authenticated(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"

        client = FivetranClient(api_key, api_secret)
        client._client.auth = None

        with pytest.raises(Exception):
            client.connector_endpoint

    # If the client raises an exception, FivetranClient raises an exception.
    def test_client_raises_exception(self):
        api_key = "your_api_key"
        api_secret = "your_api_secret"

        client = FivetranClient(api_key, api_secret)
        client._client.get = lambda *args, **kwargs: Exception("Error")

        with pytest.raises(Exception):
            client.connector_endpoint