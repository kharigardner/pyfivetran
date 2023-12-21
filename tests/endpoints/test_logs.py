import pytest
from datetime import datetime
from pyfivetran.endpoints.logs import LogEndpoint, BASE_API_URL, API_VERSION

class TestLogEndpoint:

    @pytest.fixture
    def log_endpoint(self, mocker):
        client_mock = mocker.Mock()
        return LogEndpoint(client_mock)

    def test_create_service(self, log_endpoint, mocker):
        # Mock the necessary dependencies
        log_endpoint._request = mocker.Mock()
        log_endpoint._request.return_value.json.return_value = {'status': 'success'}

        # Call the create_service method
        response = log_endpoint.create_service(group_id='123', service='Test Service', enabled=True, key='value')

        # Assertions
        assert response == {'status': 'success'}
        log_endpoint._request.assert_called_once_with(
            method='POST',
            url=f'{BASE_API_URL}/{API_VERSION}/external-logging',
            json={
                'group_id': '123',
                'service': 'Test Service',
                'enabled': True,
                'config': {'key': 'value'}
            }
        )

    def test_delete_service(self, log_endpoint, mocker):
        # Mock the necessary dependencies
        log_endpoint._request = mocker.Mock()
        log_endpoint._request.return_value.json.return_value = {'status': 'success'}

        # Call the delete_service method
        response = log_endpoint.delete_service(log_id='456')

        # Assertions
        assert response == {'status': 'success'}
        log_endpoint._request.assert_called_once_with(
            method='DELETE',
            url=f'{BASE_API_URL}/{API_VERSION}/external-logging/456'
        )

    def test_get_service(self, log_endpoint, mocker):
        # Mock the necessary dependencies
        log_endpoint._request = mocker.Mock()
        log_endpoint._request.return_value.json.return_value = {'status': 'success'}

        # Call the get_service method
        response = log_endpoint.get_service(log_id='789')

        # Assertions
        assert response == {'status': 'success'}
        log_endpoint._request.assert_called_once_with(
            method='GET',
            url=f'{BASE_API_URL}/{API_VERSION}/external-logging/789'
        )

    def test_test_service(self, log_endpoint, mocker):
        # Mock the necessary dependencies
        log_endpoint._request = mocker.Mock()
        log_endpoint._request.return_value.json.return_value = {'status': 'success'}

        # Call the test_service method
        response = log_endpoint.test_service(log_id='123')

        # Assertions
        assert response == {'status': 'success'}
        log_endpoint._request.assert_called_once_with(
            method='POST',
            url=f'{BASE_API_URL}/{API_VERSION}/external-logging/123/test'
        )

    def test_update_service(self, log_endpoint, mocker):
        # Mock the necessary dependencies
        log_endpoint._request = mocker.Mock()
        log_endpoint._request.return_value.json.return_value = {'status': 'success'}

        # Call the update_service method
        response = log_endpoint.update_service(log_id='456', enabled=True, key= 'value')

        # Assertions
        assert response == {'status': 'success'}
        log_endpoint._request.assert_called_once_with(
            method='PATCH',
            url=f'{BASE_API_URL}/{API_VERSION}/external-logging/456',
            json={
                'enabled': True,
                'config': {'key': 'value'}
            }
        )