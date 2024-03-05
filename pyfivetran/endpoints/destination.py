from __future__ import annotations

from typing import Optional, List, Dict, Any
from datetime import tzinfo
from dataclasses import dataclass
from enum import Enum


from pyfivetran.endpoints.base import Endpoint, Client, ApiDataclass
from pyfivetran.shed import GeneralApiResponse, BASE_API_URL, API_VERSION
from pyfivetran.utils import serialize_timezone


class Region(Enum):
    GCP_US_EAST4 = "GCP_US_EAST4"
    GCP_US_WEST1 = "GCP_US_WEST1"


@dataclass
class Destination(ApiDataclass):
    fivetran_id: str
    service: str
    region: Region
    setup_status: str
    group_id: str
    time_zone_offset: str | int | tzinfo
    setup_tests: Optional[List[Dict[str, Any]]] = None
    config: Optional[Dict[str, Any]] = None

    _is_deleted: bool = False

    @property
    def as_url(self) -> str:
        return f"{BASE_API_URL}/{API_VERSION}/destinations/{self.fivetran_id}"

    @property
    def raw(self) -> Dict[str, Any]:
        return getattr(self, "_raw", self.__dict__)

    def delete(self) -> GeneralApiResponse:
        resp = self.endpoint._request(method="DELETE", url=self.as_url).json()

        self._is_deleted = True
        return resp

    def modify(
        self,
        region: Optional[str | Region] = None,
        config: Optional[Dict[str, Any]] = None,
        trust_certificates: Optional[bool] = None,
        trust_fingerprints: Optional[bool] = None,
        run_setup_tests: Optional[bool] = None,
        time_zone_offset: Optional[str | int | tzinfo] = None,
    ) -> GeneralApiResponse:
        """
        Modifies the destination.

        :param region: The region of the destination
        :param config: The configuration of the destination
        :param trust_certificates: Whether to trust certificates
        :param trust_fingerprints: Whether to trust fingerprints
        :param run_setup_tests: Whether to run setup tests
        :param time_zone_offset: The time zone offset of the destination
        :return: GeneralApiResponse
        """

        if isinstance(region, Region):
            region = region.value
        elif isinstance(region, str):
            region = Region(region).value
        else:
            region = region

        payload: Dict[str, Any] = {}

        if region is not None:
            payload["region"] = region

        if config is not None:
            payload["config"] = config

        if trust_certificates is not None:
            payload["trust_certificates"] = trust_certificates

        if trust_fingerprints is not None:
            payload["trust_fingerprints"] = trust_fingerprints

        if run_setup_tests is not None:
            payload["run_setup_tests"] = run_setup_tests

        if time_zone_offset is not None:
            if not isinstance(time_zone_offset, int):
                time_zone_offset = serialize_timezone(time_zone_offset)
            payload["time_zone_offset"] = time_zone_offset

        return self.endpoint._request(
            method="PATCH", url=self.as_url, json=payload
        ).json()

    def run_setup_tests(
        self,
        trust_certificates: Optional[bool] = None,
        trust_fingerprints: Optional[bool] = None,
    ) -> GeneralApiResponse:
        """
        Runs setup tests on the destination.

        :param trust_certificates: Whether to trust certificates
        :param trust_fingerprints: Whether to trust fingerprints
        :return: GeneralApiResponse
        """
        payload = {}

        if trust_certificates is not None:
            payload["trust_certificates"] = trust_certificates

        if trust_fingerprints is not None:
            payload["trust_fingerprints"] = trust_fingerprints

        return self.endpoint._request(
            method="POST", url=f"{self.as_url}/test", json=payload
        ).json()

    @classmethod
    def _from_dict(cls, endpoint, d: Dict[str, Any]) -> "Destination":
        """
        Helper method for deserializing from a dict.

        :param d: The dict to deserialize
        :return: The deserialized object
        """
        region: Region = Region(d.get("region"))  # type: ignore

        # TODO: add logic to serialize back into TZ info

        return cls(
            endpoint=endpoint,
            fivetran_id=d.get("id"),  # type: ignore
            service=d.get("service"),  # type: ignore
            region=region,
            setup_status=d.get("setup_status"),  # type: ignore
            group_id=d.get("group_id"),  # type: ignore
            time_zone_offset=d.get("time_zone_offset"),  # type: ignore
            setup_tests=d.get("setup_tests"),  # type: ignore
            config=d.get("config"),  # type: ignore
        )


class DestinationEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        super().__init__(client)

    def get_destination(self, destination_id: str) -> Destination:
        """
        Get a destination object.

        :param destination_id: The ID of the destination
        :return: Destination
        """
        resp: GeneralApiResponse = self._request(
            method="GET", url=f"{self.BASE_URL}/destinations/{destination_id}"
        ).json()

        return Destination._from_dict(self, resp.get("data"))  # type: ignore

    def create_destination(
        self,
        group_id: str,
        service: str,
        time_zone_offset: str | int | tzinfo,
        config: Dict[
            str, Any
        ],  # TODO: probably should replace any type with a JSON serializable type alias instead
        trust_certificates: bool = False,
        trust_fingerprints: bool = False,
        run_setup_tests: Optional[bool] = None,
        region: Optional[str | Region] = None,
    ) -> Destination:
        """
        Creates a new destination within a specified group in your Fivetran account.

        :param group_id: The ID of the group
        :param service: The name of the service
        :param time_zone_offset: The time zone offset
        :param config: The config of the destination
        :param trust_certificates: Whether to trust certificates
        :param trust_fingerprints: Whether to trust fingerprints
        :param run_setup_tests: Whether to run setup tests
        :param region: The region of the destination
        :return: Destination
        """
        if isinstance(region, str):
            try:
                Region(region.upper())
            except ValueError as e:
                raise ValueError(f"Invalid region: {region}") from e
        elif isinstance(region, Region):
            region = region.name.lower()
        else:
            region = None

        if isinstance(time_zone_offset, (str, tzinfo)):
            time_zone_offset = serialize_timezone(time_zone_offset)

        payload = dict(
            group_id=group_id,
            service=service,
            time_zone_offset=time_zone_offset,
            config=config,
            trust_certificates=trust_certificates,
            trust_fingerprints=trust_fingerprints,
        )

        if run_setup_tests is not None:
            payload["run_setup_tests"] = run_setup_tests

        if region is not None:
            payload["region"] = region

        resp: GeneralApiResponse = self._request(
            method="POST", url=f"{self.BASE_URL}/destinations", json=payload
        ).json()

        return Destination._from_dict(self, resp.get("data"))  # type: ignore
