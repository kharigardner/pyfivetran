from __future__ import annotations

from typing import (
    Optional,
    List,
    Dict,
    Any,
    Literal
)
from dataclasses import dataclass
from datetime import datetime

from pyfivetran.endpoints.base import (
    Endpoint,
    Client,
    ApiDataclass
)
from pyfivetran.shed import (
    GeneralApiResponse,
    BASE_API_URL,
    API_VERSION,
    ApiError,
    PaginatedApiResponse
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
        return f'{BASE_API_URL}/{API_VERSION}/users/{self.fivetran_id}'
    
    @property
    def raw(self) -> Dict[str, Any]:
        return self._raw if hasattr(self, '_raw') else self.__dict__
    
    @classmethod
    def _from_dict(cls, endpoint, d: Dict[str, Any]) -> 'User':
        """
        Helper method for deserialzing from a dict.

        :param d: The dict to deserialize
        :return: The deserialized object
        """

        return cls(
            endpoint=endpoint,
            fivetran_id=d['id'],
            email=d['email'],
            verified=d['verified'],
            role=d['role'],
            active=d['active'],
            created_at=deserialize_timestamp(d['created_at']),
            logged_in_at=deserialize_timestamp(d['logged_in_at']),
            family_name=d.get('family_name'),
            given_name=d.get('given_name'),
            invited=d.get('invited'),
            picture=d.get('picture'),
            phone=d.get('phone')
        )