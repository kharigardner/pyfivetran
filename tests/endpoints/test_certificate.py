import pytest
from pyfivetran import CertificateEndpoint

class TestCertificateEndpoint:

    # Can approve a certificate with hash, encoded_cert, destination_id and connector_id
    def test_approve_certificate_with_all_parameters(self, mocker):
        # Mock the necessary dependencies
        client_mock = mocker.Mock()
        response_mock = mocker.Mock()
        response_mock.json.return_value = {"code": "200", "message": "Success"}
        client_mock.build_request.return_value = mocker.Mock()
        client_mock.send.return_value = response_mock

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client_mock)

        # Call the method under test
        result = endpoint.approve_certificate(
            hash="hash",
            encoded_cert="encoded_cert",
            destination_id="destination_id",
            connector_id="connector_id"
        )

        # Assert the result
        assert result == {"code": "200", "message": "Success"}

    # Can approve a fingerprint with hash, public_key, connector_id and destination_id
    def test_approve_fingerprint_with_all_parameters(self, mocker):
        # Mock the necessary dependencies
        client_mock = mocker.Mock()
        response_mock = mocker.Mock()
        response_mock.json.return_value = {"code": "200", "message": "Success"}
        client_mock.build_request.return_value = mocker.Mock()
        client_mock.send.return_value = response_mock

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client_mock)

        # Call the method under test
        result = endpoint.approve_fingerprint(
            hash="hash",
            public_key="public_key",
            connector_id="connector_id",
            destination_id="destination_id"
        )

        # Assert the result
        assert result == {"code": "200", "message": "Success"}

    # Can get certificate details with hash, connector_id and destination_id
    def test_get_certificate_details_with_all_parameters(self, mocker):
        # Mock the necessary dependencies
        client_mock = mocker.Mock()
        response_mock = mocker.Mock()
        response_mock.json.return_value = {"code": "200", "message": "Success"}
        client_mock.build_request.return_value = mocker.Mock()
        client_mock.send.return_value = response_mock

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client_mock)

        # Call the method under test
        result = endpoint.get_certificate_details(
            hash="hash",
            connector_id="connector_id",
            destination_id="destination_id"
        )

        # Assert the result
        assert result == {"code": "200", "message": "Success"}

    # When encoded_cert is bytes, it should be converted to string before being sent
    def test_encoded_cert_bytes_conversion(self, mocker):
        # Mock the necessary dependencies
        client_mock = mocker.Mock()
        response_mock = mocker.Mock()
        response_mock.json.return_value = {"code": "200", "message": "Success"}
        client_mock.build_request.return_value = mocker.Mock()
        client_mock.send.return_value = response_mock

        # Create an instance of CertificateEndpoint
        endpoint = CertificateEndpoint(client_mock)

        # Call the method under test with bytes encoded_cert
        result = endpoint.approve_certificate(
            hash="hash",
            encoded_cert=b"bytes_encoded_cert",
            destination_id="destination_id",
            connector_id="connector_id"
        )

        # Assert the result
        assert result == {"code": "200", "message": "Success"}

        # Call the method under test with string encoded_cert
        result = endpoint.approve_certificate(
            hash="hash",
            encoded_cert="string_encoded_cert",
            destination_id="destination_id",
            connector_id="connector_id"
        )

        # Assert the result
        assert result == {"code": "200", "message": "Success"}