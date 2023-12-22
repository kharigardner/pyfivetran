:py:mod:`pyfivetran.client`
===========================

.. py:module:: pyfivetran.client

.. autodoc2-docstring:: pyfivetran.client
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`AuthenticationTuple <pyfivetran.client.AuthenticationTuple>`
     - .. autodoc2-docstring:: pyfivetran.client.AuthenticationTuple
          :summary:
   * - :py:obj:`FivetranClient <pyfivetran.client.FivetranClient>`
     - .. autodoc2-docstring:: pyfivetran.client.FivetranClient
          :summary:

API
~~~

.. py:class:: AuthenticationTuple
   :canonical: pyfivetran.client.AuthenticationTuple

   Bases: :py:obj:`typing.NamedTuple`

   .. autodoc2-docstring:: pyfivetran.client.AuthenticationTuple

   .. py:attribute:: basic
      :canonical: pyfivetran.client.AuthenticationTuple.basic
      :type: httpx.BasicAuth
      :value: None

      .. autodoc2-docstring:: pyfivetran.client.AuthenticationTuple.basic

   .. py:attribute:: mapping
      :canonical: pyfivetran.client.AuthenticationTuple.mapping
      :type: typing.Dict[str, str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.client.AuthenticationTuple.mapping

.. py:class:: FivetranClient(api_key: str, api_secret: str)
   :canonical: pyfivetran.client.FivetranClient

   .. autodoc2-docstring:: pyfivetran.client.FivetranClient

   .. rubric:: Initialization

   .. autodoc2-docstring:: pyfivetran.client.FivetranClient.__init__

   .. py:property:: authentication
      :canonical: pyfivetran.client.FivetranClient.authentication
      :type: pyfivetran.client.AuthenticationTuple

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.authentication

   .. py:property:: client
      :canonical: pyfivetran.client.FivetranClient.client
      :type: httpx.Client

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.client

   .. py:method:: connector_endpoint() -> pyfivetran.endpoints.ConnectorEndpoint
      :canonical: pyfivetran.client.FivetranClient.connector_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.connector_endpoint

   .. py:method:: connector_schema_endpoint() -> pyfivetran.endpoints.ConnectorSchemaEndpoint
      :canonical: pyfivetran.client.FivetranClient.connector_schema_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.connector_schema_endpoint

   .. py:method:: certificate_endpoint() -> pyfivetran.endpoints.CertificateEndpoint
      :canonical: pyfivetran.client.FivetranClient.certificate_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.certificate_endpoint

   .. py:method:: destination_endpoint() -> pyfivetran.endpoints.DestinationEndpoint
      :canonical: pyfivetran.client.FivetranClient.destination_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.destination_endpoint

   .. py:method:: group_endpoint() -> pyfivetran.endpoints.GroupEndpoint
      :canonical: pyfivetran.client.FivetranClient.group_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.group_endpoint

   .. py:method:: logs_endpoint() -> pyfivetran.endpoints.LogEndpoint
      :canonical: pyfivetran.client.FivetranClient.logs_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.logs_endpoint

   .. py:method:: role_endpoint() -> pyfivetran.endpoints.RoleEndpoint
      :canonical: pyfivetran.client.FivetranClient.role_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.role_endpoint

   .. py:method:: user_endpoint() -> pyfivetran.endpoints.UserEndpoint
      :canonical: pyfivetran.client.FivetranClient.user_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.user_endpoint

   .. py:method:: webhook_endpoint() -> pyfivetran.endpoints.WebhookEndpoint
      :canonical: pyfivetran.client.FivetranClient.webhook_endpoint

      .. autodoc2-docstring:: pyfivetran.client.FivetranClient.webhook_endpoint
