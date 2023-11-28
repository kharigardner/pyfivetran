from __future__ import annotations

from typing import (
    Optional,
    List,
    Dict,
    Any,
    Literal
)

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

class RoleEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + '/' + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client = client
        super().__init__(client)

    def list_roles(
            self,
            limit: Optional[int] = None
    ) -> List[PaginatedApiResponse]:
        """
        Returns a list of roles in your Fivetran account.

        :param limit: The number of records to return
        :return: List[PaginatedApiResponse]
        """
        params = dict()

        if limit is not None:
            params['limit'] = limit

        resp_list = self._paginate(
            first_response=self._request(
                method='GET',
                url=f'{self.BASE_URL}/roles',
                params=params
            ),
            endpoint=f'{self.BASE_URL}/roles',
            limit=limit
        )

        return list(map(lambda x: x.json(), resp_list))