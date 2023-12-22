:py:mod:`pyfivetran.endpoints.logs`
===================================

.. py:module:: pyfivetran.endpoints.logs

.. autodoc2-docstring:: pyfivetran.endpoints.logs
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`LogEndpoint <pyfivetran.endpoints.logs.LogEndpoint>`
     -

API
~~~

.. py:class:: LogEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.logs.LogEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.logs.LogEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.logs.LogEndpoint.BASE_URL

   .. py:method:: create_service(group_id: typing.Optional[str] = None, service: typing.Optional[str] = None, enabled: typing.Optional[bool] = None, **kwargs) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.logs.LogEndpoint.create_service

      .. autodoc2-docstring:: pyfivetran.endpoints.logs.LogEndpoint.create_service

   .. py:method:: delete_service(log_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.logs.LogEndpoint.delete_service

      .. autodoc2-docstring:: pyfivetran.endpoints.logs.LogEndpoint.delete_service

   .. py:method:: get_service(log_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.logs.LogEndpoint.get_service

      .. autodoc2-docstring:: pyfivetran.endpoints.logs.LogEndpoint.get_service

   .. py:method:: test_service(log_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.logs.LogEndpoint.test_service

      .. autodoc2-docstring:: pyfivetran.endpoints.logs.LogEndpoint.test_service

   .. py:method:: update_service(log_id: str, enabled: typing.Optional[bool] = None, **kwargs) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.logs.LogEndpoint.update_service

      .. autodoc2-docstring:: pyfivetran.endpoints.logs.LogEndpoint.update_service
