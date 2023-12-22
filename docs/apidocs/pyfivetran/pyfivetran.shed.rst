:py:mod:`pyfivetran.shed`
=========================

.. py:module:: pyfivetran.shed

.. autodoc2-docstring:: pyfivetran.shed
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`GeneralApiResponse <pyfivetran.shed.GeneralApiResponse>`
     -
   * - :py:obj:`PaginatedApiResponse <pyfivetran.shed.PaginatedApiResponse>`
     -

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`BASE_API_URL <pyfivetran.shed.BASE_API_URL>`
     - .. autodoc2-docstring:: pyfivetran.shed.BASE_API_URL
          :summary:
   * - :py:obj:`API_VERSION <pyfivetran.shed.API_VERSION>`
     - .. autodoc2-docstring:: pyfivetran.shed.API_VERSION
          :summary:

API
~~~

.. py:data:: BASE_API_URL
   :canonical: pyfivetran.shed.BASE_API_URL
   :value: 'https://api.fivetran.com'

   .. autodoc2-docstring:: pyfivetran.shed.BASE_API_URL

.. py:data:: API_VERSION
   :canonical: pyfivetran.shed.API_VERSION
   :value: 'v1'

   .. autodoc2-docstring:: pyfivetran.shed.API_VERSION

.. py:class:: GeneralApiResponse()
   :canonical: pyfivetran.shed.GeneralApiResponse

   Bases: :py:obj:`typing.TypedDict`

   .. py:attribute:: code
      :canonical: pyfivetran.shed.GeneralApiResponse.code
      :type: str | int
      :value: None

      .. autodoc2-docstring:: pyfivetran.shed.GeneralApiResponse.code

   .. py:attribute:: message
      :canonical: pyfivetran.shed.GeneralApiResponse.message
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.shed.GeneralApiResponse.message

   .. py:attribute:: data
      :canonical: pyfivetran.shed.GeneralApiResponse.data
      :type: typing.Optional[typing.Dict[str, typing.Any]]
      :value: None

      .. autodoc2-docstring:: pyfivetran.shed.GeneralApiResponse.data

.. py:exception:: ApiError()
   :canonical: pyfivetran.shed.ApiError

   Bases: :py:obj:`Exception`

   .. py:method:: __inti__(msg: str)
      :canonical: pyfivetran.shed.ApiError.__inti__

      .. autodoc2-docstring:: pyfivetran.shed.ApiError.__inti__

   .. py:method:: __str__()
      :canonical: pyfivetran.shed.ApiError.__str__

.. py:class:: PaginatedApiResponse()
   :canonical: pyfivetran.shed.PaginatedApiResponse

   Bases: :py:obj:`pyfivetran.shed.GeneralApiResponse`

   .. py:attribute:: next_cursor
      :canonical: pyfivetran.shed.PaginatedApiResponse.next_cursor
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.shed.PaginatedApiResponse.next_cursor
