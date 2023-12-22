:py:mod:`pyfivetran.endpoints.connector`
========================================

.. py:module:: pyfivetran.endpoints.connector

.. autodoc2-docstring:: pyfivetran.endpoints.connector
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Connector <pyfivetran.endpoints.connector.Connector>`
     -
   * - :py:obj:`ConnectorEndpoint <pyfivetran.endpoints.connector.ConnectorEndpoint>`
     -

API
~~~

.. py:class:: Connector
   :canonical: pyfivetran.endpoints.connector.Connector

   Bases: :py:obj:`pyfivetran.endpoints.base.ApiDataclass`

   .. py:attribute:: fivetran_id
      :canonical: pyfivetran.endpoints.connector.Connector.fivetran_id
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.fivetran_id

   .. py:attribute:: service
      :canonical: pyfivetran.endpoints.connector.Connector.service
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.service

   .. py:attribute:: schema
      :canonical: pyfivetran.endpoints.connector.Connector.schema
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.schema

   .. py:attribute:: paused
      :canonical: pyfivetran.endpoints.connector.Connector.paused
      :type: bool
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.paused

   .. py:attribute:: sync_frequency
      :canonical: pyfivetran.endpoints.connector.Connector.sync_frequency
      :type: int
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.sync_frequency

   .. py:attribute:: pause_after_trial
      :canonical: pyfivetran.endpoints.connector.Connector.pause_after_trial
      :type: bool
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.pause_after_trial

   .. py:attribute:: group_id
      :canonical: pyfivetran.endpoints.connector.Connector.group_id
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.group_id

   .. py:attribute:: connected_by
      :canonical: pyfivetran.endpoints.connector.Connector.connected_by
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.connected_by

   .. py:attribute:: service_version
      :canonical: pyfivetran.endpoints.connector.Connector.service_version
      :type: int
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.service_version

   .. py:attribute:: created_at
      :canonical: pyfivetran.endpoints.connector.Connector.created_at
      :type: datetime.datetime | str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.created_at

   .. py:attribute:: data_delay_senstivity
      :canonical: pyfivetran.endpoints.connector.Connector.data_delay_senstivity
      :type: typing.Literal[LOW, NORMAL, HIGH, CUSTOM]
      :value: 'NORMAL'

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.data_delay_senstivity

   .. py:attribute:: setup_tests
      :canonical: pyfivetran.endpoints.connector.Connector.setup_tests
      :type: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.setup_tests

   .. py:attribute:: source_sync_details
      :canonical: pyfivetran.endpoints.connector.Connector.source_sync_details
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.source_sync_details

   .. py:attribute:: data_delay_threshold
      :canonical: pyfivetran.endpoints.connector.Connector.data_delay_threshold
      :type: typing.Optional[int]
      :value: 0

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.data_delay_threshold

   .. py:attribute:: connect_card
      :canonical: pyfivetran.endpoints.connector.Connector.connect_card
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.connect_card

   .. py:attribute:: status
      :canonical: pyfivetran.endpoints.connector.Connector.status
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.status

   .. py:attribute:: daily_sync_time
      :canonical: pyfivetran.endpoints.connector.Connector.daily_sync_time
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.daily_sync_time

   .. py:attribute:: succeeded_at
      :canonical: pyfivetran.endpoints.connector.Connector.succeeded_at
      :type: typing.Optional[datetime.datetime | str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.succeeded_at

   .. py:attribute:: failed_at
      :canonical: pyfivetran.endpoints.connector.Connector.failed_at
      :type: typing.Optional[str | datetime.datetime]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.failed_at

   .. py:attribute:: schedule_type
      :canonical: pyfivetran.endpoints.connector.Connector.schedule_type
      :type: typing.Literal[auto, manual]
      :value: 'auto'

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.schedule_type

   .. py:attribute:: connect_card_config
      :canonical: pyfivetran.endpoints.connector.Connector.connect_card_config
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.connect_card_config

   .. py:attribute:: config
      :canonical: pyfivetran.endpoints.connector.Connector.config
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.config

   .. py:attribute:: _is_deleted
      :canonical: pyfivetran.endpoints.connector.Connector._is_deleted
      :type: bool
      :value: False

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector._is_deleted

   .. py:property:: as_url
      :canonical: pyfivetran.endpoints.connector.Connector.as_url
      :type: str

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.as_url

   .. py:property:: raw
      :canonical: pyfivetran.endpoints.connector.Connector.raw
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.raw

   .. py:method:: modify(config: typing.Optional[typing.Dict[str, typing.Any]] = None, auth: typing.Optional[typing.Dict[str, typing.Any]] = None, paused: typing.Optional[bool] = None, trust_certificates: typing.Optional[bool] = None, trust_fingerprints: typing.Optional[bool] = None, daily_sync_time: typing.Optional[str] = None, run_setup_tests: typing.Optional[bool] = None, sync_frequency: typing.Optional[int] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.Connector.modify

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.modify

   .. py:method:: modify_state(state: typing.Dict[str, typing.Any]) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.Connector.modify_state

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.modify_state

   .. py:method:: delete() -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.Connector.delete

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.delete

   .. py:method:: resync(scope: typing.Optional[typing.Dict[str, typing.List[str]]] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.Connector.resync

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.resync

   .. py:method:: run_setup_tests(trust_certificates: typing.Optional[bool] = None, trust_fingerprints: typing.Optional[bool] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.Connector.run_setup_tests

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.run_setup_tests

   .. py:method:: sync(force: typing.Optional[bool] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.Connector.sync

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector.sync

   .. py:method:: _from_dict(endpoint, d: typing.Dict[str, typing.Any]) -> pyfivetran.endpoints.connector.Connector
      :canonical: pyfivetran.endpoints.connector.Connector._from_dict
      :classmethod:

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.Connector._from_dict

.. py:class:: ConnectorEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.ConnectorEndpoint.BASE_URL

   .. py:method:: connect_card(connector_id: str, redirect_uri: str, hide_setup_guide: typing.Optional[bool] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint.connect_card

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.ConnectorEndpoint.connect_card

   .. py:method:: get_config_metadata(service: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint.get_config_metadata

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.ConnectorEndpoint.get_config_metadata

   .. py:method:: get_connector(connector_id: str) -> pyfivetran.endpoints.connector.Connector
      :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint.get_connector

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.ConnectorEndpoint.get_connector

   .. py:method:: get_connector_state(connector_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint.get_connector_state

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.ConnectorEndpoint.get_connector_state

   .. py:method:: get_source_metadata(limit: typing.Optional[int] = None) -> typing.List[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.connector.ConnectorEndpoint.get_source_metadata

      .. autodoc2-docstring:: pyfivetran.endpoints.connector.ConnectorEndpoint.get_source_metadata
