from __future__ import annotations

from typing import Optional, Dict, Any, Literal

from pyfivetran.endpoints.base import Endpoint, Client

from pyfivetran.shed import GeneralApiResponse, BASE_API_URL, API_VERSION, ApiError


class ConnectorSchemaEndpoint(Endpoint):
    BASE_URL: str = BASE_API_URL + "/" + API_VERSION

    def __init__(self, client: Client) -> None:
        self.client = client
        super().__init__(client)

    def modify_connector_column_config(
        self,
        connector_id: str,
        schema_name: str,
        table_name: str,
        column_name: str,
        enabled: Optional[bool] = None,
        hashed: Optional[bool] = None,
    ) -> GeneralApiResponse:
        """
        Modifies the column configuration for a specific connector.

        :param connector_id: Unique ID of the connector in Fivetran
        :param schema_name: The schema name within the Fivetran system
        :param table_name: The table name within the Fivetran system
        :param column_name: The column name within the Fivetran system
        :param enabled: Whether the column is enabled
        :param hashed: Whether the column is hashed
        :return: GeneralApiResponse
        """
        payload = {}

        if enabled is not None:
            payload["enabled"] = enabled

        if hashed is not None:
            payload["hashed"] = hashed

        if not payload:
            # Is this a normal pattern? On optional args, return an error if trying to update with nothing?
            raise ApiError("No payload provided to modify_connector_column_config")

        return self._request(
            method="PATCH",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas/{schema_name}/tables/{table_name}/columns/{column_name}",
            json=payload,
        ).json()

    def modify_connector_database_schema_config(
        self,
        connector_id: str,
        schema_name: str,
        enabled: Optional[bool] = None,
        tables: Optional[Dict[Any, Any]] = None,
    ) -> GeneralApiResponse:
        """
        Modify connector database schema config.

        :param connector_id: Unique ID of the connector in Fivetran
        :param schema_name: The schema name within the Fivetran system
        :param enabled: Whether the schema is enabled
        :param tables: The tables within the schema
        :return: GeneralApiResponse
        """
        payload: Dict[Any, Any] = {}

        if enabled is not None:
            payload["enabled"] = enabled

        if tables is not None:
            payload["tables"] = tables

        if not payload:
            # Is this a normal pattern? On optional args, return an error if trying to update with nothing?
            raise ApiError(
                "No payload provided to modify_connector_database_schema_config"
            )

        return self._request(
            method="PATCH",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas/{schema_name}",
            json=payload,
        ).json()

    def modify_connector_schema_config(
        self,
        connector_id: str,
        schemas: Optional[Dict[Any, Any]] = None,
        schema_change_handling: Optional[
            Literal["ALLOW_ALL", "ALLOW_COLUMNS", "BLOCK_ALL"]
        ] = None,
    ) -> GeneralApiResponse:
        """
        Updates the schema configuration for a specific connector.

        :param connector_id: Unique ID of the connector in Fivetran
        :param schemas: The schemas within the Fivetran system
        :param schema_change_handling: The schema change handling
        :return: GeneralApiResponse
        """

        if schema_change_handling not in ["ALLOW_ALL", "ALLOW_COLUMNS", "BLOCK_ALL"]:
            raise ApiError(
                "Invalid schema_change_handling value provided"
            ) from ValueError()

        payload: Dict[Any, Any] = {}

        if schemas is not None:
            payload["schemas"] = schemas

        if schema_change_handling is not None:
            payload["schema_change_handling"] = schema_change_handling

        if not payload:
            # Is this a normal pattern? On optional args, return an error if trying to update with nothing?
            raise ApiError("No payload provided to modify_connector_schema_config")

        return self._request(
            method="PATCH",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas",
            json=payload,
        ).json()

    def modify_table_config(
        self,
        connector_id: str,
        schema_name: str,
        table_name: str,
        enabled: Optional[bool] = None,
        columns: Optional[Dict[Any, Any]] = None,
        sync_mode: Optional[Literal["SOFT_DELETE", "HISTORY", "LIVE"]] = None,
    ) -> GeneralApiResponse:
        """
        Updates the table configuration for a specific connector.

        :param connector_id: Unique ID of the connector in Fivetran
        :param schema_name: The schema name within the Fivetran system
        :param table_name: The table name within the Fivetran system
        :param enabled: Whether the table is enabled
        :param columns: The columns within the table
        :param sync_mode: The sync mode for the table
        :return: GeneralApiResponse
        """

        if sync_mode not in ["SOFT_DELETE", "HISTORY", "LIVE"]:
            raise ApiError("Invalid sync_mode value provided") from ValueError()

        payload: Dict[Any, Any] = {}

        if enabled is not None:
            payload["enabled"] = enabled

        if columns is not None:
            payload["columns"] = columns

        if sync_mode is not None:
            payload["sync_mode"] = sync_mode

        if not payload:
            # Is this a normal pattern? On optional args, return an error if trying to update with nothing?
            raise ApiError("No payload provided to modify_table_config")

        return self._request(
            method="PATCH",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas/{schema_name}/tables/{table_name}",
            json=payload,
        ).json()

    def resync_connector_table_data(
        self, connector_id: str, **prop_kwargs: Optional[Dict[str, Any]]
    ) -> GeneralApiResponse:
        """
        Triggers a historical sync of all data for multiple schema tables within a connector.
        This action does not override the standard sync frequency you defined in the Fivetran dashboard.

        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """

        return self._request(
            method="POST",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas/tables/resync",
            json=prop_kwargs,
        ).json()

    def reload_connector_schema_config(
        self, connector_id: str, exclude_mode: Optional[str] = None
    ) -> GeneralApiResponse:
        """
        Reloads the schema configuration for a specific connector.

        :param connector_id: Unique ID of the connector in Fivetran
        :param exclude_mode: The exclude mode
        :return: GeneralApiResponse
        """

        payload: Dict[Any, Any] = {}

        if exclude_mode is not None:
            payload["exclude_mode"] = exclude_mode

        if not payload:
            # Is this a normal pattern? On optional args, return an error if trying to update with nothing?
            raise ApiError("No payload provided to reload_connector_schema_config")

        return self._request(
            method="POST",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas/reload",
            json=payload,
        ).json()

    def get_connector_schema_config(self, connector_id: str) -> GeneralApiResponse:
        """
        Get the connector schema config for an existing connector within your Fivetran account.

        :param connector_id: Unique ID of the connector in Fivetran
        :return: GeneralApiResponse
        """

        return self._request(
            method="GET", url=f"{self.BASE_URL}/connectors/{connector_id}/schemas"
        ).json()

    def get_source_table_columns_config(
        self, connector_id: str, schema: str, table: str
    ) -> GeneralApiResponse:
        """
        Get the source table columns config for an existing connector within your Fivetran account.

        :param connector_id: Unique ID of the connector in Fivetran
        :param schema: The schema name within the Fivetran system
        :param table: The table name within the Fivetran system
        :return: GeneralApiResponse
        """

        return self._request(
            method="GET",
            url=f"{self.BASE_URL}/connectors/{connector_id}/schemas/{schema}/tables/{table}/columns",
        ).json()
