import pytest
from unittest.mock import Mock, patch
from datetime import datetime

from pyfivetran import Connector, ConnectorEndpoint
from pyfivetran.shed import ApiError, PaginatedApiResponse, GeneralApiResponse

class TestConnector:

    # Connector can be instantiated with required arguments
    def test_instantiation_with_required_arguments(self):
        connector = Connector(
            fivetran_id='123',
            service='service',
            schema='schema',
            paused=False,
            sync_frequency=60,
            pause_after_trial=False,
            group_id='group',
            connected_by='user',
            service_version=1,
            created_at=datetime.now()
        )
    
        assert connector.fivetran_id == '123'
        assert connector.service == 'service'
        assert connector.schema == 'schema'
        assert connector.paused == False
        assert connector.sync_frequency == 60
        assert connector.pause_after_trial == False
        assert connector.group_id == 'group'
        assert connector.connected_by == 'user'
        assert connector.service_version == 1
        assert isinstance(connector.created_at, datetime)

    # Connector can be modified with valid arguments
    def test_modification_with_valid_arguments(self, mocker):
        endpoint_mock = mocker.Mock()
        connector = Connector(
            fivetran_id='123',
            service='service',
            schema='schema',
            paused=False,
            sync_frequency=60,
            pause_after_trial=False,
            group_id='group',
            connected_by='user',
            service_version=1,
            created_at=datetime.now(),
            endpoint=endpoint_mock
        )
    
        response_mock = mocker.Mock()
        response_mock.json.return_value = {'success': True}
        endpoint_mock._request.return_value = response_mock
    
        connector.modify(paused=True)
    
        assert connector.paused == True
        endpoint_mock._request.assert_called_once_with(
            method='PATCH',
            url=connector.as_url,
            json={'paused': True}
        )

    # Connector can be deleted
    def test_deletion(self, mocker):
        endpoint_mock = mocker.Mock()
        connector = Connector(
            fivetran_id='123',
            service='service',
            schema='schema',
            paused=False,
            sync_frequency=60,
            pause_after_trial=False,
            group_id='group',
            connected_by='user',
            service_version=1,
            created_at=datetime.now(),
            endpoint=endpoint_mock
        )
    
        response_mock = mocker.Mock()
        response_mock.json.return_value = {'success': True}
        endpoint_mock.client.delete.return_value = response_mock
    
        connector.delete()
    
        assert connector._is_deleted == True
        endpoint_mock.client.delete.assert_called_once_with(url=connector.as_url)

    # Connector cannot be modified with invalid arguments
    def test_modification_with_invalid_arguments(self, mocker):
        endpoint_mock = mocker.Mock()
        connector = Connector(
            fivetran_id='123',
            service='service',
            schema='schema',
            paused=False,
            sync_frequency=60,
            pause_after_trial=False,
            group_id='group',
            connected_by='user',
            service_version=1,
            created_at=datetime.now(),
            endpoint=endpoint_mock
        )
    
        with pytest.raises(ApiError):
            connector.modify(sync_frequency=10)
    
        assert connector.sync_frequency == 60
        endpoint_mock._request.assert_not_called()

    # Connector cannot be synced with invalid arguments
    def test_sync_with_invalid_arguments(self, mocker):
        endpoint_mock = mocker.Mock()
        connector = Connector(
            fivetran_id='123',
            service='service',
            schema='schema',
            paused=False,
            sync_frequency=60,
            pause_after_trial=False,
            group_id='group',
            connected_by='user',
            service_version=1,
            created_at=datetime.now(),
            endpoint=endpoint_mock
        )
    
        with pytest.raises(ApiError):
            connector.sync(force='invalid')
    
        endpoint_mock._request.assert_not_called()



# Mock the Client and Connector classes
class MockClient:
    def __init__(self):
        self.session = Mock()

class MockConnector:
    @staticmethod
    def _from_dict(endpoint, d):
        return d

# Patch the imports in the connector module
@pytest.fixture(autouse=True)
def mock_classes(monkeypatch):
    monkeypatch.setattr("pyfivetran.endpoints.connector.Client", MockClient)
    monkeypatch.setattr("pyfivetran.endpoints.connector.Connector", MockConnector)

# Parametrized test for ConnectorEndpoint.connect_card
@pytest.mark.parametrize(
    "connector_id, redirect_uri, hide_setup_guide, expected_response, test_id",
    [
        ("123", "http://example.com/callback", None, {"success": True}, "happy_path_no_hide"),
        ("123", "http://example.com/callback", True, {"success": True}, "happy_path_hide_true"),
        ("123", "http://example.com/callback", False, {"success": True}, "happy_path_hide_false"),
        # Add more test cases for edge and error scenarios
    ]
)
def test_connect_card(connector_id, redirect_uri, hide_setup_guide, expected_response, test_id):
    # Arrange
    client = MockClient()
    endpoint = ConnectorEndpoint(client)
    client.session.request.return_value.json.return_value = expected_response

    # Act
    response = endpoint.connect_card(connector_id, redirect_uri, hide_setup_guide)

    # Assert
    client.session.request.assert_called_once_with(
        method='POST',
        url=f'{ConnectorEndpoint.BASE_URL}/connectors/{connector_id}/connect-card',
        json={'redirect_uri': redirect_uri, **({'hide_setup_guide': hide_setup_guide} if hide_setup_guide is not None else {})}
    )
    assert response == expected_response

# Parametrized test for ConnectorEndpoint.get_config_metadata
@pytest.mark.parametrize(
    "service, expected_response, test_id",
    [
        ("service_a", {"config": "metadata"}, "happy_path_service_a"),
        ("service_b", {"config": "metadata"}, "happy_path_service_b"),
        # Add more test cases for edge and error scenarios
    ]
)
def test_get_config_metadata(service, expected_response, test_id):
    # Arrange
    client = MockClient()
    endpoint = ConnectorEndpoint(client)
    client.session.request.return_value.json.return_value = expected_response

    # Act
    response = endpoint.get_config_metadata(service)

    # Assert
    client.session.request.assert_called_once_with(
        method='GET',
        url=f'{ConnectorEndpoint.BASE_URL}/metadata/connector-types/{service}'
    )
    assert response == expected_response

# Parametrized test for ConnectorEndpoint.get_connector
@pytest.mark.parametrize(
    "connector_id, expected_response, test_id",
    [
        ("123", {"id": "123", "name": "Test Connector"}, "happy_path"),
        # Add more test cases for edge and error scenarios
    ]
)
def test_get_connector(connector_id, expected_response, test_id):
    # Arrange
    client = MockClient()
    endpoint = ConnectorEndpoint(client)
    client.session.request.return_value.json.return_value = {"data": expected_response}

    # Act
    response = endpoint.get_connector(connector_id)

    # Assert
    client.session.request.assert_called_once_with(
        method='GET',
        url=f'{ConnectorEndpoint.BASE_URL}/connectors/{connector_id}'
    )
    assert response == expected_response

# Parametrized test for ConnectorEndpoint.get_connector_state
@pytest.mark.parametrize(
    "connector_id, expected_response, test_id",
    [
        ("123", {"state": "running"}, "happy_path"),
        # Add more test cases for edge and error scenarios
    ]
)
def test_get_connector_state(connector_id, expected_response, test_id):
    # Arrange
    client = MockClient()
    endpoint = ConnectorEndpoint(client)
    client.session.request.return_value.json.return_value = expected_response

    # Act
    response = endpoint.get_connector_state(connector_id)

    # Assert
    client.session.request.assert_called_once_with(
        method='GET',
        url=f'{ConnectorEndpoint.BASE_URL}/connectors/{connector_id}/state'
    )
    assert response == expected_response

# Parametrized test for ConnectorEndpoint.get_source_metadata
@pytest.mark.parametrize(
    "limit, expected_responses, test_id",
    [
        (None, [{"source": "metadata"}], "happy_path_default_limit"),
        (50, [{"source": "metadata"}], "happy_path_custom_limit"),
        # Add more test cases for edge and error scenarios
    ]
)
def test_get_source_metadata(limit, expected_responses, test_id):
    # Arrange
    client = MockClient()
    endpoint = ConnectorEndpoint(client)
    client.session.request.return_value = Mock()
    client.session.request.return_value.json.side_effect = [response for response in expected_responses]

    # Act
    responses = endpoint.get_source_metadata(limit)

    # Assert
    assert all(isinstance(response, dict) for response in responses)
    assert len(responses) == len(expected_responses)
    for response, expected in zip(responses, expected_responses):
        assert response == expected
