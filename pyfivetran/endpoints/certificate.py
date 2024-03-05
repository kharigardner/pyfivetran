from __future__ import annotations

from typing import Optional, List

from pyfivetran.endpoints.base import Endpoint, Client
from pyfivetran.shed import (
    GeneralApiResponse,
    BASE_API_URL,
    API_VERSION,
    PaginatedApiResponse,
)


class CertificateEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client = client
        super().__init__(client)

    def approve_certificate(
        self,
        hash: str,
        encoded_cert: str | bytes,
        destination_id: Optional[str] = None,
        connector_id: Optional[str] = None,
    ) -> GeneralApiResponse:
        """
        Approves a certificate for a connector/destination, so Fivetran trusts this certificate for a source/destination database.
        The connector/destination setup tests will fail if a non-approved certificate is provided.

        :param hash: Hash of the certificate
        :param encoded_cert: The certificate encoded in base64, as a string or bytes
        :param destination_id: Unique ID of the destination in Fivetran
        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """

        if isinstance(encoded_cert, bytes):
            # just have to serialize it as a string for the API
            encoded_cert = str(encoded_cert)

        payload = {"hash": hash, "encoded_cert": encoded_cert}

        if destination_id:
            payload["destination_id"] = destination_id

        if connector_id:
            payload["connector_id"] = connector_id

        return self._request(
            method="POST", url=f"{self.BASE_URL}/certificates", json=payload
        ).json()

    def approve_fingerprint(
        self,
        hash_: str,
        public_key: str | bytes,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
    ) -> GeneralApiResponse:
        """
        Approves a fingerprint for a connector/destination, so Fivetran trusts this fingerprint for a source/destination database.
        The connector/destination setup tests will fail if a non-approved fingerprint is provided.

        :param hash: Hash of the fingerprint
        :param public_key: The fingerprint encoded in base64, as a string or bytes
        :param destination_id: Unique ID of the destination in Fivetran
        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """
        if isinstance(public_key, bytes):
            # just have to serialize it as a string for the API
            public_key = str(public_key)

        payload = {"hash": hash_, "public_key": public_key}

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/fingerprints"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/fingerprints"
        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        return self._request(
            method="POST", url=f"{self.BASE_URL}{endpoint_}", json=payload
        ).json()

    def get_certificate_details(
        self,
        hash_: str | bytes,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
    ) -> GeneralApiResponse:
        """
        Get certificate details.

        :param hash: Hash of the certificate
        :param destination_id: Unique ID of the destination in Fivetran
        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """
        if isinstance(hash_, bytes):
            # just have to serialize it as a string for the API
            hash_ = str(hash_)

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/certificates/{hash_}"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/certificates/{hash_}"
        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        return self._request(method="GET", url=f"{self.BASE_URL}{endpoint_}").json()

    def get_fingerprint_details(
        self,
        hash_: str | bytes,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
    ) -> GeneralApiResponse:
        """
        Get fingerprint details.

        :param hash: Hash of the fingerprint
        :param destination_id: Unique ID of the destination in Fivetran
        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """
        if isinstance(hash_, bytes):
            # just have to serialize it as a string for the API
            hash_ = str(hash_)

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/fingerprints/{hash_}"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/fingerprints/{hash_}"
        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        return self._request(method="GET", url=f"{self.BASE_URL}{endpoint_}").json()

    def get_fingerprints(
        self,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> List[PaginatedApiResponse]:
        """
        Get all fingerprints for a connector or destination.

        :param connector_id: Unique ID of the connector in Fivetran
        :param destination_id: Unique ID of the destination in Fivetran
        :param limit: Number of results to return
        :return: List[PaginatedApiResponse]
        """

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/fingerprints"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/fingerprints"
        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        if not limit:
            limit = 100

        params = {"limit": limit}

        first_response = self._request(
            method="GET", url=f"{self.BASE_URL}{endpoint_}", params=params
        )

        resp = self._paginate(
            first_response=first_response, endpoint=endpoint_, limit=limit
        )

        return list(map(lambda x: x.json(), resp))

    def get_certificates(
        self,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> List[PaginatedApiResponse]:
        """
        Get all certificates for a connector or destination.

        :param connector_id: Unique ID of the connector in Fivetran
        :param destination_id: Unique ID of the destination in Fivetran
        :param limit: Number of results to return
        :return: List[PaginatedApiResponse]
        """

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/certificates"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/certificates"
        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        if not limit:
            limit = 100

        params = {"limit": limit}

        first_response = self._request(
            method="GET", url=f"{self.BASE_URL}{endpoint_}", params=params
        )

        resp = self._paginate(
            first_response=first_response,
            endpoint=f"{self.BASE_URL}{endpoint_}",
            limit=limit,
        )

        return list(map(lambda x: x.json(), resp))

    def revoke_certificate(
        self,
        hash_: str | bytes,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
    ) -> GeneralApiResponse:
        """
        Revoke a certificate.

        :param hash: Hash of the certificate
        :param destination_id: Unique ID of the destination in Fivetran
        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """
        if isinstance(hash_, bytes):
            # just have to serialize it as a string for the API
            hash_ = str(hash_)

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/certificates/{hash_}"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/certificates/{hash_}"
        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        return self._request(method="DELETE", url=f"{self.BASE_URL}{endpoint_}").json()

    def revoke_fingerprint(
        self,
        hash_: str | bytes,
        connector_id: Optional[str] = None,
        destination_id: Optional[str] = None,
    ) -> GeneralApiResponse:
        """
        Revoke a fingerprint.

        :param hash: Hash of the fingerprint
        :param destination_id: Unique ID of the destination in Fivetran
        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """
        if isinstance(hash_, bytes):
            # just have to serialize it as a string for the API
            hash_ = str(hash_)

        if connector_id:
            endpoint_ = f"/connectors/{connector_id}/fingerprints/{hash_}"
        elif destination_id:
            endpoint_ = f"/destinations/{destination_id}/fingerprints/{hash_}"

        else:
            raise ValueError("Either connector_id or destination_id must be provided")

        return self._request(method="DELETE", url=f"{self.BASE_URL}{endpoint_}").json()
