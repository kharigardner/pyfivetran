:py:mod:`pyfivetran.endpoints.webhook`
======================================

.. py:module:: pyfivetran.endpoints.webhook

.. autodoc2-docstring:: pyfivetran.endpoints.webhook
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`WebhookEndpoint <pyfivetran.endpoints.webhook.WebhookEndpoint>`
     -

API
~~~

.. py:class:: WebhookEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.webhook.WebhookEndpoint.BASE_URL

   .. py:method:: create_webhook(url: str, events: typing.Optional[typing.List[str]] = None, active: typing.Optional[bool] = None, secret: typing.Optional[str] = None, webhook_type: typing.Literal[account, group] = 'account') -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint.create_webhook

      .. autodoc2-docstring:: pyfivetran.endpoints.webhook.WebhookEndpoint.create_webhook

   .. py:method:: delete_webhook(webhook_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint.delete_webhook

      .. autodoc2-docstring:: pyfivetran.endpoints.webhook.WebhookEndpoint.delete_webhook

   .. py:method:: list_webhook(limit: typing.Optional[int] = None) -> typing.Sequence[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint.list_webhook

      .. autodoc2-docstring:: pyfivetran.endpoints.webhook.WebhookEndpoint.list_webhook

   .. py:method:: get_webhook(webhook_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint.get_webhook

      .. autodoc2-docstring:: pyfivetran.endpoints.webhook.WebhookEndpoint.get_webhook

   .. py:method:: test_webhook(webhook_id: str, event: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.webhook.WebhookEndpoint.test_webhook

      .. autodoc2-docstring:: pyfivetran.endpoints.webhook.WebhookEndpoint.test_webhook
