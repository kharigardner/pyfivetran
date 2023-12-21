# Generated by CodiumAI

import pytest

from pyfivetran.endpoints.webhook import WebhookEndpoint, Client


class TestWebhookEndpoint:

    # Create a webhook with mandatory parameters
    def test_create_webhook_mandatory_parameters(self, mocker):
        # Mock the _request method
        mocker.patch.object(WebhookEndpoint, '_request', return_value=mocker.Mock(json=lambda: {'code': 200, 'message': 'Success', 'data': {}}))

        # Create a WebhookEndpoint instance
        client = Client()
        webhook_endpoint = WebhookEndpoint(client)

        # Call the create_webhook method with mandatory parameters
        response = webhook_endpoint.create_webhook(url='https://example.com')

        # Assert that the response is as expected
        assert response == {'code': 200, 'message': 'Success', 'data': {}}

    # Create a webhook with all parameters
    def test_create_webhook_all_parameters(self, mocker):
        # Mock the _request method
        class MockResponse:
            def __init__(self, data):
                self.data = data
        
            def json(self):
                return self.data

        mocker.patch.object(WebhookEndpoint, '_request', return_value=MockResponse({'code': 200, 'message': 'Success', 'data': {}}))

        # Create a WebhookEndpoint instance
        client = Client()
        webhook_endpoint = WebhookEndpoint(client)

        # Call the create_webhook method with all parameters
        response = webhook_endpoint.create_webhook(url='https://example.com', events=['event1', 'event2'], active=True, secret='secret', webhook_type='account')

        # Assert that the response is as expected
        assert response == {'code': 200, 'message': 'Success', 'data': {}}

    # delete a webhook
    def test_delete_webhook(self, mocker):
        # Create a mock response object
        mock_response = mocker.Mock()
        mock_response.json.return_value = {'code': 200, 'message': 'Success', 'data': {}}
    
        # Mock the _request method
        mocker.patch.object(WebhookEndpoint, '_request', return_value=mock_response)

        # Create a WebhookEndpoint instance
        client = Client()
        webhook_endpoint = WebhookEndpoint(client)

        # Call the delete_webhook method
        response = webhook_endpoint.delete_webhook(webhook_id='123')

        # Assert that the response is as expected
        assert response == {'code': 200, 'message': 'Success', 'data': {}}

    # Create a webhook with invalid events
    def test_create_webhook_invalid_events(self, mocker):
        import unittest
        # Mock the _request method
        mocker.patch.object(WebhookEndpoint, '_request', return_value=unittest.mock.Mock())

        # Create a WebhookEndpoint instance
        client = Client()
        webhook_endpoint = WebhookEndpoint(client)

        # Call the create_webhook method with invalid events
        response = webhook_endpoint.create_webhook(url='https://example.com', events=['invalid_event'])

        # Assert that the response is a Mock object
        assert isinstance(response, unittest.mock.Mock)

    # Create a webhook with an invalid webhook_type
    def test_create_webhook_invalid_webhook_type(self, mocker):
        # Mock the _request method
        mocker.patch.object(WebhookEndpoint, '_request', return_value=mocker.MagicMock(json=lambda: {'code': 400, 'message': 'Invalid webhook type', 'data': {}}))

        # Create a WebhookEndpoint instance
        client = Client()
        webhook_endpoint = WebhookEndpoint(client)

        # Call the create_webhook method with an invalid webhook type
        response = webhook_endpoint.create_webhook(url='https://example.com', webhook_type='invalid_type')

        # Assert that the response is as expected
        assert response == {'code': 400, 'message': 'Invalid webhook type', 'data': {}}