:py:mod:`pyfivetran.endpoints.base`
===================================

.. py:module:: pyfivetran.endpoints.base

.. autodoc2-docstring:: pyfivetran.endpoints.base
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Endpoint <pyfivetran.endpoints.base.Endpoint>`
     -
   * - :py:obj:`ApiDataclass <pyfivetran.endpoints.base.ApiDataclass>`
     -

API
~~~

.. py:class:: Endpoint(client: httpx.Client)
   :canonical: pyfivetran.endpoints.base.Endpoint

   Bases: :py:obj:`abc.ABC`

   .. py:method:: _request(**kwargs) -> httpx.Response
      :canonical: pyfivetran.endpoints.base.Endpoint._request

      .. autodoc2-docstring:: pyfivetran.endpoints.base.Endpoint._request

   .. py:method:: _paginate(first_response: httpx.Response, endpoint: str, limit: typing.Optional[int] = None) -> typing.List[httpx.Response]
      :canonical: pyfivetran.endpoints.base.Endpoint._paginate

      .. autodoc2-docstring:: pyfivetran.endpoints.base.Endpoint._paginate

.. py:class:: ApiDataclass
   :canonical: pyfivetran.endpoints.base.ApiDataclass

   Bases: :py:obj:`abc.ABC`

   .. py:attribute:: endpoint
      :canonical: pyfivetran.endpoints.base.ApiDataclass.endpoint
      :type: pyfivetran.endpoints.base.Endpoint
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.base.ApiDataclass.endpoint

   .. py:method:: _from_dict(endpoint, d: typing.Dict[str, typing.Any]) -> pyfivetran.endpoints.base.ApiDataclass
      :canonical: pyfivetran.endpoints.base.ApiDataclass._from_dict
      :abstractmethod:
      :classmethod:

      .. autodoc2-docstring:: pyfivetran.endpoints.base.ApiDataclass._from_dict
