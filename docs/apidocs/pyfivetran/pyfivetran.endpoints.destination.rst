:py:mod:`pyfivetran.endpoints.destination`
==========================================

.. py:module:: pyfivetran.endpoints.destination

.. autodoc2-docstring:: pyfivetran.endpoints.destination
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Region <pyfivetran.endpoints.destination.Region>`
     -
   * - :py:obj:`Destination <pyfivetran.endpoints.destination.Destination>`
     -
   * - :py:obj:`DestinationEndpoint <pyfivetran.endpoints.destination.DestinationEndpoint>`
     -

API
~~~

.. py:class:: Region(*args, **kwds)
   :canonical: pyfivetran.endpoints.destination.Region

   Bases: :py:obj:`enum.Enum`

   .. py:attribute:: GCP_US_EAST4
      :canonical: pyfivetran.endpoints.destination.Region.GCP_US_EAST4
      :value: 'GCP_US_EAST4'

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Region.GCP_US_EAST4

   .. py:attribute:: GCP_US_WEST1
      :canonical: pyfivetran.endpoints.destination.Region.GCP_US_WEST1
      :value: 'GCP_US_WEST1'

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Region.GCP_US_WEST1

.. py:class:: Destination
   :canonical: pyfivetran.endpoints.destination.Destination

   Bases: :py:obj:`pyfivetran.endpoints.base.ApiDataclass`

   .. py:attribute:: fivetran_id
      :canonical: pyfivetran.endpoints.destination.Destination.fivetran_id
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.fivetran_id

   .. py:attribute:: service
      :canonical: pyfivetran.endpoints.destination.Destination.service
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.service

   .. py:attribute:: region
      :canonical: pyfivetran.endpoints.destination.Destination.region
      :type: pyfivetran.endpoints.destination.Region
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.region

   .. py:attribute:: setup_status
      :canonical: pyfivetran.endpoints.destination.Destination.setup_status
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.setup_status

   .. py:attribute:: group_id
      :canonical: pyfivetran.endpoints.destination.Destination.group_id
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.group_id

   .. py:attribute:: time_zone_offset
      :canonical: pyfivetran.endpoints.destination.Destination.time_zone_offset
      :type: str | int | datetime.tzinfo
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.time_zone_offset

   .. py:attribute:: setup_tests
      :canonical: pyfivetran.endpoints.destination.Destination.setup_tests
      :type: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.setup_tests

   .. py:attribute:: config
      :canonical: pyfivetran.endpoints.destination.Destination.config
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.config

   .. py:attribute:: _is_deleted
      :canonical: pyfivetran.endpoints.destination.Destination._is_deleted
      :type: bool
      :value: False

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination._is_deleted

   .. py:property:: as_url
      :canonical: pyfivetran.endpoints.destination.Destination.as_url
      :type: str

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.as_url

   .. py:property:: raw
      :canonical: pyfivetran.endpoints.destination.Destination.raw
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.raw

   .. py:method:: delete() -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.destination.Destination.delete

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.delete

   .. py:method:: modify(region: typing.Optional[str | pyfivetran.endpoints.destination.Region] = None, config: typing.Optional[typing.Dict[str, typing.Any]] = None, trust_certificates: typing.Optional[bool] = None, trust_fingerprints: typing.Optional[bool] = None, run_setup_tests: typing.Optional[bool] = None, time_zone_offset: typing.Optional[str | int | datetime.tzinfo] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.destination.Destination.modify

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.modify

   .. py:method:: run_setup_tests(trust_certificates: typing.Optional[bool] = None, trust_fingerprints: typing.Optional[bool] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.destination.Destination.run_setup_tests

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination.run_setup_tests

   .. py:method:: _from_dict(endpoint, d: typing.Dict[str, typing.Any]) -> pyfivetran.endpoints.destination.Destination
      :canonical: pyfivetran.endpoints.destination.Destination._from_dict
      :classmethod:

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.Destination._from_dict

.. py:class:: DestinationEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.destination.DestinationEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.destination.DestinationEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.DestinationEndpoint.BASE_URL

   .. py:method:: get_destination(destination_id: str) -> pyfivetran.endpoints.destination.Destination
      :canonical: pyfivetran.endpoints.destination.DestinationEndpoint.get_destination

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.DestinationEndpoint.get_destination

   .. py:method:: create_destination(group_id: str, service: str, time_zone_offset: str | int | datetime.tzinfo, config: typing.Dict[str, typing.Any], trust_certificates: bool = False, trust_fingerprints: bool = False, run_setup_tests: typing.Optional[bool] = None, region: typing.Optional[str | pyfivetran.endpoints.destination.Region] = None) -> pyfivetran.endpoints.destination.Destination
      :canonical: pyfivetran.endpoints.destination.DestinationEndpoint.create_destination

      .. autodoc2-docstring:: pyfivetran.endpoints.destination.DestinationEndpoint.create_destination
