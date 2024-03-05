from __future__ import annotations

from typing import Optional, List, Dict, Any, Literal, TYPE_CHECKING
from datetime import datetime
from dataclasses import dataclass

from httpx import HTTPStatusError

from pyfivetran.utils import deserialize_timestamp
from pyfivetran.endpoints.base import Endpoint, Client, ApiDataclass
from pyfivetran.shed import (
    GeneralApiResponse,
    BASE_API_URL,
    API_VERSION,
    ApiError,
    PaginatedApiResponse,
)


@dataclass
class Connector(ApiDataclass):
    fivetran_id: str
    service: str
    schema: str
    paused: bool
    sync_frequency: int
    pause_after_trial: bool
    group_id: str
    connected_by: str
    service_version: int
    created_at: datetime | str
    data_delay_senstivity: Literal["LOW", "NORMAL", "HIGH", "CUSTOM"] = "NORMAL"

    setup_tests: Optional[List[Dict[str, Any]]] = None
    source_sync_details: Optional[Dict[str, Any]] = None
    data_delay_threshold: Optional[int] = 0
    connect_card: Optional[Dict[str, Any]] = None
    status: Optional[Dict[str, Any]] = None
    daily_sync_time: Optional[str] = None
    succeeded_at: Optional[datetime | str] = None
    failed_at: Optional[str | datetime] = None
    schedule_type: Literal["auto", "manual"] = "auto"
    connect_card_config: Optional[Dict[str, Any]] = None
    config: Optional[Dict[str, Any]] = None

    _is_deleted: bool = False

    @property
    def as_url(self) -> str:
        return f"{BASE_API_URL}/{API_VERSION}/connectors/{self.fivetran_id}"

    @property
    def raw(self) -> Dict[str, Any]:
        return self._raw if hasattr(self, "_raw") else self.__dict__  # type: ignore

    def modify(
        self,
        config: Optional[Dict[str, Any]] = None,
        auth: Optional[Dict[str, Any]] = None,
        paused: Optional[bool] = None,
        trust_certificates: Optional[bool] = None,
        trust_fingerprints: Optional[bool] = None,
        daily_sync_time: Optional[str] = None,
        run_setup_tests: Optional[bool] = None,
        sync_frequency: Optional[int] = None,
    ) -> GeneralApiResponse:
        if sync_frequency and sync_frequency not in [
            5,
            15,
            30,
            60,
            120,
            180,
            360,
            480,
            720,
            1440,
        ]:
            raise ApiError("Invalid sync_frequency value provided") from ValueError()

        payload: Dict[str, Any] = {}

        if config is not None:
            payload["config"] = config

        if auth is not None:
            payload["auth"] = auth

        if paused is not None:
            payload["paused"] = paused

        if trust_certificates is not None:
            payload["trust_certificates"] = trust_certificates

        if trust_fingerprints is not None:
            payload["trust_fingerprints"] = trust_fingerprints

        if daily_sync_time is not None:
            payload["daily_sync_time"] = daily_sync_time

        if run_setup_tests is not None:
            payload["run_setup_tests"] = run_setup_tests

        if sync_frequency is not None:
            payload["sync_frequency"] = sync_frequency

        # moving this under the resp, so we only modify if the function succeeds

        resp = self.endpoint._request(
            method="PATCH", url=self.as_url, json=payload
        ).json()

        for key, value in payload.items():
            if value is not None:
                setattr(self, key, value)

        return resp

    def modify_state(self, state: Dict[str, Any]) -> GeneralApiResponse:
        """
        Modifies the connector state. This endpoint is only supported for
        function connectors.

        :param state: The state of the connector
        :return: GeneralApiResponse
        """
        return self.endpoint._request(
            method="PATCH", url=f"{self.as_url}/state", json=state
        ).json()

    def delete(self) -> Optional[GeneralApiResponse]:
        """
        Deletes the connector.
        :return: GeneralApiResponse
        """
        # TODO: need to adjust this to use the endpoint attribute
        obj = self.endpoint.client.delete(url=self.as_url)
        try:
            obj.raise_for_status()
            obj_json = obj.json()
            self._is_deleted = True
        except HTTPStatusError as e:
            if obj.status_code == 404:
                obj_json = None
            else:
                raise e
        return obj_json

    def resync(
        self, scope: Optional[Dict[str, List[str]]] = None
    ) -> GeneralApiResponse:
        """
        Resyncs the connector.

        :param scope: A map containing an array of tables to re-sync for each schema, must be non-empty.
        :return: GeneralApiResponse
        """
        return self.endpoint._request(method="POST", url=f"{self.as_url}/resync").json()

    def run_setup_tests(
        self,
        trust_certificates: Optional[bool] = None,
        trust_fingerprints: Optional[bool] = None,
    ) -> GeneralApiResponse:
        """
        Runs setup tests on the connector.

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

    def sync(self, force: Optional[bool] = None) -> GeneralApiResponse:
        """
        Triggers a data sync for an existing connector within your Fivetran account without waiting for the next scheduled sync.
        This action does not override the standard sync frequency you defined in the Fivetran dashboard.

        :param force: If force is true and the connector is currently syncing, it will stop the sync and re-run it.
        :return: GeneralApiResponse
        """
        if not force:
            force = False

        payload = dict(force=force)

        return self.endpoint._request(
            method="POST", url=f"{self.as_url}/sync", json=payload
        ).json()

    @classmethod
    def _from_dict(cls, endpoint, d: Dict[str, Any]) -> "Connector":
        """
        Helper method for deserializing from a dict
        :param d: The dict to deserialize
        :return: The deserialized object
        """

        # TODO: change this to the utility deserialize timestamp function
        # convert to datetimes
        # timestamps come in the format: 2019-08-24T14:15:22Z
        if d.get("succeeded_at") and isinstance(d.get("succeeded_at"), str):
            d["succeeded_at"] = deserialize_timestamp(
                d["succeeded_at"]
            )
        if d.get("created_at") and isinstance(d.get("created_at"), str):
            d["created_at"] = deserialize_timestamp(
                d["created_at"]
            )
        if d.get("failed_at") and isinstance(d.get("failed_at"), str):
            d["failed_at"] = deserialize_timestamp(d["failed_at"])

        cls_to_return = cls(
            fivetran_id=d['id'],
            service=d['service'],
            schema=d['schema'],
            paused=d['paused'],
            status=d.get("status"),
            daily_sync_time=d.get("daily_sync_time"),
            succeeded_at=d.get("succeeded_at"),
            connect_card=d.get("connect_card"),
            sync_frequency=int(d["sync_frequency"]),
            pause_after_trial=bool(d["pause_after_trial"]),
            data_delay_threshold=d.get("data_delay_threshold"),
            group_id=str(d["group_id"]),
            connected_by=d["connected_by"],
            setup_tests=d.get("setup_tests"),
            source_sync_details=d.get("source_sync_details"),
            service_version=d["service_version"],
            created_at=d["created_at"], 
            failed_at=d.get("failed_at"),
            schedule_type=d["schedule_type"],
            connect_card_config=d.get("connect_card_config"),
            config=d.get("config"),
            _is_deleted=False,
            endpoint=endpoint
        )

        setattr(cls_to_return, "_raw", d)
        return cls_to_return


class ConnectorEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        super().__init__(client)

    def connect_card(
        self,
        connector_id: str,
        redirect_uri: str,
        hide_setup_guide: Optional[bool] = None,
    ) -> GeneralApiResponse:
        """
        Generates the Connect Card URI for the connector.

        :param connector_id: Unique ID of the connector in Fivetran
        :param redirect_uri: Redirect URI for the connector
        :param hide_setup_guide: Whether to hide the setup guide
        :return: GeneralApiResponse
        """
        payload: Dict[str, Any] = {"redirect_uri": redirect_uri}

        if hide_setup_guide is not None:
            payload["hide_setup_guide"] = hide_setup_guide

        return self._request(
            method="POST",
            url=f"{self.BASE_URL}/connectors/{connector_id}/connect-card",
            json=payload,
        ).json()

    def get_config_metadata(self, service: str) -> GeneralApiResponse:
        """
        Returns metadata of configuration parameters and authorization parameters for a
        specified connector type.

        :param service: The service to get the config metadata for
        :return: GeneralApiResponse
        """
        return self._request(
            method="GET", url=f"{self.BASE_URL}/metadata/connector-types/{service}"
        ).json()

    def get_connector(self, connector_id: str) -> Connector:
        """
        Gets a connector.

        :param connector_id: Unique ID of the connector in Fivetran
        :return: Connector
        """
        return Connector._from_dict(
            endpoint=self,
            d=self._request(
                method="GET", url=f"{self.BASE_URL}/connectors/{connector_id}"
            ).json()["data"],
        )

    # TODO: maybe move this method into the Connector class?
    def get_connector_state(self, connector_id: str) -> GeneralApiResponse:
        """
        Return connector state. Only supported for function connectors.

        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """
        return self._request(
            method="GET", url=f"{self.BASE_URL}/connectors/{connector_id}/state"
        ).json()

    def get_source_metadata(
        self, limit: Optional[int] = None
    ) -> List[PaginatedApiResponse]:
        """
        Returns all available source types within your Fivetran account.
        This endpoint makes it easier to display Fivetran connectors within your application because it provides metadata including the proper source name (‘Facebook Ad Account’ instead of facebook_ad_account), the source icon, and links to Fivetran resources.
        As we update source names and icons, that metadata will automatically update within this endpoint

        :param limit: The number of records to return
        :return: List[PaginatedApiResponse]
        """

        if not limit:
            limit = 100

        params = {"limit": limit}

        resp_list = self._paginate(
            first_response=self._request(
                method="GET",
                url=f"{self.BASE_URL}/metadata/connector-types",
                params=params,
            ),
            endpoint=f"{self.BASE_URL}/metadata/connector-types",
            limit=limit,
        )

        return list(map(lambda x: x.json(), resp_list))

    def create_connector(self, connector: Connector | dict[str, Any]) -> Connector:
        """
        Creates a new connector.

        :param connector: Connector
        :return: Connector
        """
        if isinstance(connector, Connector):
            connector = connector.raw
            for k, v in connector.items():
                if v is None:
                    del connector[k]

        return Connector._from_dict(
            endpoint=self,
            d=self._request(
                method="POST",
                url=f"{self.BASE_URL}/connectors",
                json=connector,
            ).json()["data"],
        )
