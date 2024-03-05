from __future__ import annotations

from typing import Optional, List, Dict, Any
from dataclasses import dataclass
from datetime import datetime

from pyfivetran.endpoints.base import Endpoint, Client, ApiDataclass
from pyfivetran.shed import (
    GeneralApiResponse,
    BASE_API_URL,
    API_VERSION,
    PaginatedApiResponse,
)
from pyfivetran.utils import deserialize_timestamp


@dataclass
class Group(ApiDataclass):
    fivetran_id: str
    name: str
    created_at: datetime

    _is_deleted: bool = False

    @property
    def as_url(self) -> str:
        return f"{BASE_API_URL}/{API_VERSION}/groups/{self.fivetran_id}"

    @property
    def raw(self) -> Dict[str, Any]:
        return getattr(self, "_raw", self.__dict__)

    @property
    def public_key(self) -> str:
        """
        Public key from SSH key pair.
        """
        if not hasattr(self, "_public_key"):
            resp: GeneralApiResponse = self.endpoint._request(
                method="GET", url=f"{self.as_url}/public-key"
            ).json()
            self._public_key: str = resp["data"]["public_key"]  # type: ignore

        return self._public_key

    @property
    def service_account(self) -> str:
        """
        Fivetran service account associated with the group.
        """
        if not hasattr(self, "_service_account"):
            resp: GeneralApiResponse = self.endpoint._request(
                method="GET", url=f"{self.as_url}/service-account"
            ).json()
            self._service_account: str = resp["data"]["service_account"]  # type: ignore

        return self._service_account

    @classmethod
    def _from_dict(cls, endpoint, d: Dict[str, Any]) -> "Group":
        """
        Helper method for deserializing from a dict

        :param d: The dict to deserialize
        :return: The deserialized object
        """
        cls_to_return = cls(
            endpoint=endpoint,
            fivetran_id=d["id"],
            name=d["name"],
            created_at=deserialize_timestamp(d["created_at"]),
        )

        setattr(cls_to_return, "_raw", d)

        return cls_to_return

    def delete(self) -> GeneralApiResponse:
        """
        Deletes a group in your Fivetran account.

        :return: GeneralApiResponse
        """
        return self.endpoint._request(method="DELETE", url=self.as_url).json()

    def modify(self, name: str) -> GeneralApiResponse:
        """
        Modifies a group in your Fivetran account.

        :param name: The name of the group
        :return: GeneralApiResponse
        """
        payload = dict(name=name)

        return self.endpoint._request(
            method="PATCH", url=self.as_url, json=payload
        ).json()

    def add_user(
        self, email: Optional[str] = None, role: Optional[str] = None
    ) -> GeneralApiResponse:
        """
        Adds an existing user to a group in your Fivetran account.

        :param email: The email of the user to add
        :param role: The role of the user to add
        :return: GeneralApiResponse
        """
        payload = {}

        if not email and not role:
            raise ValueError("Either email or role must be provided")

        if email is not None:
            payload["email"] = email

        if role is not None:
            payload["role"] = role

        return self.endpoint._request(
            method="POST", url=f"{self.as_url}/users", json=payload
        ).json()

    # TODO: change this to serialize to the Connector dataclass
    def list_connectors(
        self, schema: Optional[str] = None, limit: Optional[int] = None
    ) -> List[PaginatedApiResponse]:  # sourcery skip: class-extract-method
        """
        Returns a list of connectors in a group in your Fivetran account.

        :param schema: The schema of the connector
        :param limit: The number of records to return
        :return: List[PaginatedApiResponse]
        """
        params: Dict[str, str | int] = {}

        if schema is not None:
            params["schema"] = schema

        if limit is not None:
            params["limit"] = limit

        resp_list = self.endpoint._paginate(
            first_response=self.endpoint._request(
                method="GET", url=f"{self.as_url}/connectors", params=params
            ),
            endpoint=f"{self.as_url}/connectors",
            limit=limit,
        )

        return list(map(lambda x: x.json(), resp_list))

    # TODO: serialize to the User dataclass
    def list_users(self, limit: Optional[int] = None) -> List[PaginatedApiResponse]:
        """
        Returns a list of users in a group in your Fivetran account.

        :param limit: The number of records to return
        :return: List[PaginatedApiResponse]
        """
        params = {}

        if limit is not None:
            params["limit"] = limit

        resp_list = self.endpoint._paginate(
            first_response=self.endpoint._request(
                method="GET", url=f"{self.as_url}/users", params=params
            ),
            endpoint=f"{self.as_url}/users",
            limit=limit,
        )

        return list(map(lambda x: x.json(), resp_list))

    # TODO: serialize to User dataclass
    def remove_user(self, user_id: str) -> GeneralApiResponse:
        """
        Removes a user from a group in your Fivetran account.

        :param user_id: The ID of the user to remove
        :return: GeneralApiResponse
        """
        return self.endpoint._request(
            method="DELETE", url=f"{self.as_url}/users/{user_id}"
        ).json()


class GroupEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client: Client = client
        super().__init__(client)

    def create_group(self, name: str) -> Group:
        """
        Creates a new group in your fivetran account.

        :param name: The name of the group
        :return: Group
        """
        payload = dict(name=name)

        response: GeneralApiResponse = self._request(
            method="POST", url=f"{self.BASE_URL}/groups", json=payload
        ).json()

        return Group._from_dict(self, response["data"])  # type: ignore

    def list_groups(self, limit: Optional[int] = None) -> List[Group]:
        """
        Returns a list of groups in your Fivetran account.

        :param limit: The number of records to return
        :return: List[PaginatedApiResponse]
        """
        params = {}

        if limit is not None:
            params["limit"] = limit

        resp_list = self._paginate(
            first_response=self._request(
                method="GET", url=f"{self.BASE_URL}/groups", params=params
            ),
            endpoint=f"{self.BASE_URL}/groups",
            limit=limit,
        )

        jsons: List[PaginatedApiResponse] = list(map(lambda x: x.json(), resp_list))

        group_jsons: List[Dict[str, Any]] = []

        for json in jsons:
            group_jsons.extend(json.get("data").get("items"))  # type: ignore

        return list(map(lambda x: Group._from_dict(self, x), group_jsons))

    def get_group(self, group_id: str) -> Group:
        """
        Gets a group in your Fivetran account.

        :param group_id: The ID of the group
        :return: Group
        """
        resp: GeneralApiResponse = self._request(
            method="GET", url=f"{self.BASE_URL}/groups/{group_id}"
        ).json()

        return Group._from_dict(
            self,
            resp["data"],  # type: ignore
        )
