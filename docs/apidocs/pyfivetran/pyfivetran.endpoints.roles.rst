:py:mod:`pyfivetran.endpoints.roles`
====================================

.. py:module:: pyfivetran.endpoints.roles

.. autodoc2-docstring:: pyfivetran.endpoints.roles
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`RoleEndpoint <pyfivetran.endpoints.roles.RoleEndpoint>`
     -

API
~~~

.. py:class:: RoleEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.roles.RoleEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.roles.RoleEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.roles.RoleEndpoint.BASE_URL

   .. py:method:: list_roles(limit: typing.Optional[int] = None) -> typing.List[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.roles.RoleEndpoint.list_roles

      .. autodoc2-docstring:: pyfivetran.endpoints.roles.RoleEndpoint.list_roles
