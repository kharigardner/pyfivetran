from __future__ import annotations

from typing import Optional, List, Dict, Any, Sequence
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
class User(ApiDataclass):
    fivetran_id: str
    email: str
    verified: bool
    role: str
    active: bool
    created_at: datetime
    logged_in_at: datetime

    family_name: Optional[str]
    given_name: Optional[str] = None
    invited: Optional[bool] = None
    picture: Optional[str | bytes] = None
    phone: Optional[str] = None

    _is_deleted: bool = False

    @property
    def as_url(self) -> str:
        return f"{BASE_API_URL}/{API_VERSION}/users/{self.fivetran_id}"

    @property
    def raw(self) -> Dict[str, Any]:
        return getattr(self, "_raw", self.__dict__)

    @property
    def connector_memberships(self) -> Sequence[PaginatedApiResponse]:
        """
        All connector memberships for a user.

        :return: PaginatedApiResponse
        """
        first_resp = self.endpoint._request(
            method="GET", url=f"{self.as_url}/connectors"
        )

        paginated_resp = self.endpoint._paginate(
            first_response=first_resp, endpoint=f"{self.as_url}/connectors", limit=None
        )

        return list(map(lambda x: x.json(), paginated_resp))

    @property
    def group_memberships(self) -> Sequence[PaginatedApiResponse]:
        """
        All group memberships for a user.

        :return: PaginatedApiResponse
        """
        first_resp = self.endpoint._request(method="GET", url=f"{self.as_url}/groups")

        paginated_resp = self.endpoint._paginate(
            first_response=first_resp, endpoint=f"{self.as_url}/groups", limit=None
        )

        return list(map(lambda x: x.json(), paginated_resp))

    def delete(self) -> GeneralApiResponse:
        """
        Deletes a user in your Fivetran account.

        :return: GeneralApiResponse
        """
        return self.endpoint._request(method="DELETE", url=self.as_url).json()

    def add_connector_membership(
        self, connector_id: str, role: str
    ) -> GeneralApiResponse:
        """
        Add a connector membership.

        :param connector_id: The id of the connector
        :param role: The role of the user
        :return: GeneralApiResponse
        """
        payload = dict(connector_id=connector_id, role=role)

        return self.endpoint._request(
            method="POST", url=f"{self.as_url}/connectors", json=payload
        ).json()

    def add_group_membership(self, group_id: str, role: str) -> GeneralApiResponse:
        """
        Add a group membership.

        :param group_id: The id of the group
        :param role: The role of the user
        :return: GeneralApiResponse
        """
        payload = dict(group_id=group_id, role=role)

        return self.endpoint._request(
            method="POST", url=f"{self.as_url}/groups", json=payload
        ).json()

    @classmethod
    def _from_dict(cls, endpoint, d: Dict[str, Any]) -> "User":
        """
        Helper method for deserialzing from a dict.

        :param d: The dict to deserialize
        :return: The deserialized object
        """

        return cls(
            endpoint=endpoint,
            fivetran_id=d["id"],
            email=d["email"],
            verified=d["verified"],
            role=d["role"],
            active=d["active"],
            created_at=deserialize_timestamp(d["created_at"]),
            logged_in_at=deserialize_timestamp(d["logged_in_at"]),
            family_name=d.get("family_name"),
            given_name=d.get("given_name"),
            invited=d.get("invited"),
            picture=d.get("picture"),
            phone=d.get("phone"),
        )


class UserEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client = client
        super().__init__(client)

    def invite_user(
        self,
        email: str,
        family_name: str,
        given_name: str,
        phone: Optional[str] = None,
        picture: Optional[str] = None,
        role: Optional[str] = None,
    ) -> User:
        """
        Invite a user to your Fivetran account.

        :param email: The email of the user
        :param family_name: The family name of the user
        :param given_name: The given name of the user
        :param phone: The phone number of the user
        :param picture: The picture of the user
        :param role: The role of the user
        :return: User
        """
        payload = dict(email=email, family_name=family_name, given_name=given_name)

        if phone:
            payload["phone"] = phone
        if picture:
            payload["picture"] = picture
        if role:
            payload["role"] = role

        resp: GeneralApiResponse = self._request(
            method="POST", url=f"{self.BASE_URL}/users", json=payload
        ).json()

        return User._from_dict(self, resp.get("data"))  # type: ignore

    def get_users(self, limit: Optional[int] = None) -> Sequence[User]:
        """
        Returns a list of all users within your Fivetran account.

        :param limit: The number of records to return
        :return: Sequence[User]
        """
        if not limit:
            limit = 100

        params = {"limit": limit}

        resp_list = self._paginate(
            first_response=self._request(
                method="GET", url=f"{self.BASE_URL}/users", params=params
            ),
            endpoint=f"{self.BASE_URL}/users",
            limit=limit,
        )

        jsons: List[PaginatedApiResponse] = list(map(lambda x: x.json(), resp_list))

        user_jsons: List[Dict[str, Any]] = []

        for json in jsons:
            user_jsons.extend(json.get("data").get("items"))  # type: ignore

        return list(map(lambda x: User._from_dict(self, x), user_jsons))
