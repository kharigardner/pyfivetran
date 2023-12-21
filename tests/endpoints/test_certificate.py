# Generated by CodiumAI

import pytest

from pyfivetran.endpoints.certificate import CertificateEndpoint, Client
from pyfivetran.shed import ApiError


# Generated by CodiumAI

# Dependencies:
# pip install pytest-mock
import pytest

class TestCertificateEndpoint:

    # Can successfully approve a certificate with hash, encoded_cert, and optional destination_id and connector_id
    def test_approve_certificate_success(self, mocker):
        # Define the MockResponse class
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data

            def json(self):
                return self.json_data

        # Mock the _request method
        mocker.patch.object(CertificateEndpoint, '_request', return_value=MockResponse(status_code=200, json_data={'message': 'Certificate approved'}))

        # Create a mock client
        client = mocker.Mock(spec=Client)

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client)

        # Call the approve_certificate method
        response = endpoint.approve_certificate(hash='12345', encoded_cert='abcde')

        # Assert that the _request method was called with the correct parameters
        endpoint._request.assert_called_with(
            method='POST',
            url=f'{endpoint.BASE_URL}/certificates',
            json={
                'hash': '12345',
                'encoded_cert': 'abcde'
            }
        )

        # Assert that the response is as expected
        assert response == {'message': 'Certificate approved'}

    # Can successfully approve a fingerprint with hash, public_key, and connector_id
    def test_approve_fingerprint_success_with_connector_id(self, mocker):
        # Define the MockResponse class
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data

            def json(self):
                return self.json_data

        # Mock the _request method
        mocker.patch.object(CertificateEndpoint, '_request', return_value=MockResponse(status_code=200, json_data={'message': 'Fingerprint approved'}))

        # Create a mock client
        client = mocker.Mock(spec=Client)

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client)

        # Call the approve_fingerprint method with connector_id
        response = endpoint.approve_fingerprint(hash='12345', public_key='abcde', connector_id='connector_123')

        # Assert that the _request method was called with the correct parameters
        endpoint._request.assert_called_once_with(
            method='POST',
            url=f'{endpoint.BASE_URL}/connectors/connector_123/fingerprints',
            json={
                'hash': '12345',
                'public_key': 'abcde'
            }
        )

        # Assert that the response is as expected
        assert response == {'message': 'Fingerprint approved'}

    # Can successfully get certificate details with hash and optional connector_id and destination_id
    def test_get_certificate_details_success(self, mocker):
        # Define the MockResponse class
        class MockResponse:
            def __init__(self, status_code, json_data):
                self.status_code = status_code
                self.json_data = json_data

            def json(self):
                return self.json_data

        # Create a mock client
        client = mocker.Mock(spec=Client)

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client)

        # Mock the _request method
        mocker.patch.object(CertificateEndpoint, '_request', return_value=MockResponse(status_code=200, json_data={'certificate_id': '12345'}))

        # Call the get_certificate_details method with connector_id
        response = endpoint.get_certificate_details(hash='12345', connector_id='connector_123')

        # Assert that the _request method was called with the correct parameters
        endpoint._request.assert_called_once_with(
            method='GET',
            url=f'{endpoint.BASE_URL}/connectors/connector_123/certificates/12345'
        )

        # Assert that the response is as expected
        assert response == {'certificate_id': '12345'}

        # Reset the mock object
        endpoint._request.reset_mock()

        # Call the get_certificate_details method with destination_id
        response = endpoint.get_certificate_details(hash='12345', destination_id='destination_123')

        # Assert that the _request method was called with the correct parameters
        endpoint._request.assert_called_once_with(
            method='GET',
            url=f'{endpoint.BASE_URL}/destinations/destination_123/certificates/12345'
        )

        # Assert that the response is as expected
        assert response == {'certificate_id': '12345'}

    # Should raise a ValueError if neither connector_id nor destination_id is provided for approve_fingerprint, get_certificate_details, get_fingerprint_details, get_fingerprints, get_certificates, revoke_certificate, and revoke_fingerprint
    def test_value_error_no_connector_id_or_destination_id(self, mocker):
        # Create a mock client
        client = mocker.Mock(spec=Client)
    
        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client)
    
        # Call the approve_fingerprint method without connector_id or destination_id
        with pytest.raises(ValueError):
            endpoint.approve_fingerprint(hash='12345', public_key='abcde')
    
        # Call the get_certificate_details method without connector_id or destination_id
        with pytest.raises(ValueError):
            endpoint.get_certificate_details(hash='12345')
    
        # Call the get_fingerprint_details method without connector_id or destination_id
        with pytest.raises(ValueError):
            endpoint.get_fingerprint_details(hash='12345')
    
        # Call the get_fingerprints method without connector_id or destination_id
        with pytest.raises(ValueError):
            endpoint.get_fingerprints()
    
        # Call the get_certificates method