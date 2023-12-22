:py:mod:`pyfivetran.endpoints.group`
====================================

.. py:module:: pyfivetran.endpoints.group

.. autodoc2-docstring:: pyfivetran.endpoints.group
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`Group <pyfivetran.endpoints.group.Group>`
     -
   * - :py:obj:`GroupEndpoint <pyfivetran.endpoints.group.GroupEndpoint>`
     -

API
~~~

.. py:class:: Group
   :canonical: pyfivetran.endpoints.group.Group

   Bases: :py:obj:`pyfivetran.endpoints.base.ApiDataclass`

   .. py:attribute:: fivetran_id
      :canonical: pyfivetran.endpoints.group.Group.fivetran_id
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.fivetran_id

   .. py:attribute:: name
      :canonical: pyfivetran.endpoints.group.Group.name
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.name

   .. py:attribute:: created_at
      :canonical: pyfivetran.endpoints.group.Group.created_at
      :type: datetime.datetime
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.created_at

   .. py:attribute:: _is_deleted
      :canonical: pyfivetran.endpoints.group.Group._is_deleted
      :type: bool
      :value: False

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group._is_deleted

   .. py:property:: as_url
      :canonical: pyfivetran.endpoints.group.Group.as_url
      :type: str

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.as_url

   .. py:property:: raw
      :canonical: pyfivetran.endpoints.group.Group.raw
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.raw

   .. py:property:: public_key
      :canonical: pyfivetran.endpoints.group.Group.public_key
      :type: str

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.public_key

   .. py:property:: service_account
      :canonical: pyfivetran.endpoints.group.Group.service_account
      :type: str

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.service_account

   .. py:method:: _from_dict(endpoint, d: typing.Dict[str, typing.Any]) -> pyfivetran.endpoints.group.Group
      :canonical: pyfivetran.endpoints.group.Group._from_dict
      :classmethod:

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group._from_dict

   .. py:method:: delete() -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.group.Group.delete

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.delete

   .. py:method:: modify(name: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.group.Group.modify

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.modify

   .. py:method:: add_user(email: typing.Optional[str] = None, role: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.group.Group.add_user

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.add_user

   .. py:method:: list_connectors(schema: typing.Optional[str] = None, limit: typing.Optional[int] = None) -> typing.List[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.group.Group.list_connectors

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.list_connectors

   .. py:method:: list_users(limit: typing.Optional[int] = None) -> typing.List[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.group.Group.list_users

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.list_users

   .. py:method:: remove_user(user_id: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.group.Group.remove_user

      .. autodoc2-docstring:: pyfivetran.endpoints.group.Group.remove_user

.. py:class:: GroupEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.group.GroupEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.group.GroupEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.group.GroupEndpoint.BASE_URL

   .. py:method:: create_group(name: str) -> pyfivetran.endpoints.group.Group
      :canonical: pyfivetran.endpoints.group.GroupEndpoint.create_group

      .. autodoc2-docstring:: pyfivetran.endpoints.group.GroupEndpoint.create_group

   .. py:method:: list_groups(limit: typing.Optional[int] = None) -> typing.List[pyfivetran.endpoints.group.Group]
      :canonical: pyfivetran.endpoints.group.GroupEndpoint.list_groups

      .. autodoc2-docstring:: pyfivetran.endpoints.group.GroupEndpoint.list_groups

   .. py:method:: get_group(group_id: str) -> pyfivetran.endpoints.group.Group
      :canonical: pyfivetran.endpoints.group.GroupEndpoint.get_group

      .. autodoc2-docstring:: pyfivetran.endpoints.group.GroupEndpoint.get_group
