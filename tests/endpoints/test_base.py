import pytest
from httpx import Client, Response
from unittest.mock import Mock
from pyfivetran.endpoints.base import Endpoint, ApiError

# Mocked response for testing
class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data
    
    def text(self):
        return str(self.json_data)

    def raise_for_status(self):
        if self.status_code != 200:
            raise Exception(f"Status code was {self.status_code}")

@pytest.fixture
def client():
    with Client() as client:
        yield client

@pytest.fixture
def endpoint(client):
    return Endpoint(client)

@pytest.mark.parametrize("status_code, json_data, expected_exception", [
    pytest.param(200, {"key": "value"}, None, id="happy-path-no-exception"),
    pytest.param(404, {"error": "not found"}, ApiError, id="error-404"),
    pytest.param(500, {"error": "server error"}, ApiError, id="error-500"),
])
def test_request(endpoint, status_code, json_data, expected_exception):
    # Arrange
    endpoint.client.build_request = Mock(return_value="request")
    endpoint.client.send = Mock(return_value=MockResponse(json_data, status_code))

    # Act
    if expected_exception:
        with pytest.raises(expected_exception):
            endpoint._request()
    else:
        response = endpoint._request()

    # Assert
    if not expected_exception:
        assert response.json() == json_data

@pytest.mark.parametrize("responses, limit, expected_length", [
    pytest.param([{"next_cursor": "abc123", "data": []}, {"data": []}], None, 2, id="happy-path-default-limit"),
    pytest.param([{"next_cursor": "abc123", "data": []}, {"data": []}], 50, 2, id="happy-path-custom-limit"),
    pytest.param([{"data": []}], None, 1, id="happy-path-no-pagination"),
])
def test_paginate(endpoint, responses, limit, expected_length):
    # Arrange
    first_response = MockResponse(responses[0], 200)
    subsequent_responses = [MockResponse(response, 200) for response in responses[1:]]
    endpoint._request = Mock(side_effect=[first_response] + subsequent_responses)

    # Act
    result = endpoint._paginate(first_response, "dummy_endpoint", limit)

    # Assert
    assert len(result) == expected_length
    assert all(isinstance(r, Response) for r in result)

@pytest.mark.parametrize("first_response_data, status_code, expected_exception", [
    pytest.param({"error": "bad request"}, 400, ApiError, id="error-first-response"),
    pytest.param({"next_cursor": "abc123", "data": []}, 200, None, id="happy-path-subsequent-error"),
    pytest.param({"next_cursor": "abc123", "data": []}, 500, ApiError, id="error-subsequent-response"),
])
def test_paginate_with_errors(endpoint, first_response_data, status_code, expected_exception):
    # Arrange
    first_response = MockResponse(first_response_data, status_code)
    subsequent_response = MockResponse({"error": "server error"}, 500)
    endpoint._request = Mock(side_effect=[first_response, subsequent_response])

    # Act & Assert
    if expected_exception:
        with pytest.raises(expected_exception):
            endpoint._paginate(first_response, "dummy_endpoint")
    else:
        result = endpoint._paginate(first_response, "dummy_endpoint")
        assert len(result) == 1  # Only the first response is valid
