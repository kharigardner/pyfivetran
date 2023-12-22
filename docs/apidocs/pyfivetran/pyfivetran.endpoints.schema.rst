:py:mod:`pyfivetran.endpoints.schema`
=====================================

.. py:module:: pyfivetran.endpoints.schema

.. autodoc2-docstring:: pyfivetran.endpoints.schema
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`ConnectorSchemaEndpoint <pyfivetran.endpoints.schema.ConnectorSchemaEndpoint>`
     -

API
~~~

.. py:class:: ConnectorSchemaEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.BASE_URL

   .. py:method:: modify_connector_column_config(connector_id: str, schema_name: str, table_name: str, column_name: str, enabled: typing.Optional[bool] = None, hashed: typing.Optional[bool] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_connector_column_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_connector_column_config

   .. py:method:: modify_connector_database_schema_config(connector_id: str, schema_name: str, enabled: typing.Optional[bool] = None, tables: typing.Optional[typing.Dict[typing.Any, typing.Any]] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_connector_database_schema_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_connector_database_schema_config

   .. py:method:: modify_connector_schema_config(connector_id: str, schemas: typing.Optional[typing.Dict[typing.Any, typing.Any]] = None, schema_change_handling: typing.Optional[typing.Literal[ALLOW_ALL, ALLOW_COLUMNS, BLOCK_ALL]] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_connector_schema_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_connector_schema_config

   .. py:method:: modify_table_config(connector_id: str, schema_name: str, table_name: str, enabled: typing.Optional[bool] = None, columns: typing.Optional[typing.Dict[typing.Any, typing.Any]] = None, sync_mode: typing.Optional[typing.Literal[SOFT_DELETE, HISTORY, LIVE]] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_table_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.modify_table_config

   .. py:method:: resync_connector_table_data(connector_id: str, **prop_kwargs: typing.Optional[typing.Dict[str, typing.Any]]) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.resync_connector_table_data

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.resync_connector_table_data

   .. py:method:: reload_connector_schema_config(connector_id: str, exclude_mode: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.reload_connector_schema_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.reload_connector_schema_config

   .. py:method:: get_connector_schema_config(connector_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.get_connector_schema_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.get_connector_schema_config

   .. py:method:: get_source_table_columns_config(connector_id: str, schema: str, table: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.get_source_table_columns_config

      .. autodoc2-docstring:: pyfivetran.endpoints.schema.ConnectorSchemaEndpoint.get_source_table_columns_config
