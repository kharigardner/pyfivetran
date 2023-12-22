:py:mod:`pyfivetran.endpoints.users`
====================================

.. py:module:: pyfivetran.endpoints.users

.. autodoc2-docstring:: pyfivetran.endpoints.users
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`User <pyfivetran.endpoints.users.User>`
     -
   * - :py:obj:`UserEndpoint <pyfivetran.endpoints.users.UserEndpoint>`
     -

API
~~~

.. py:class:: User
   :canonical: pyfivetran.endpoints.users.User

   Bases: :py:obj:`pyfivetran.endpoints.base.ApiDataclass`

   .. py:attribute:: fivetran_id
      :canonical: pyfivetran.endpoints.users.User.fivetran_id
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.fivetran_id

   .. py:attribute:: email
      :canonical: pyfivetran.endpoints.users.User.email
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.email

   .. py:attribute:: verified
      :canonical: pyfivetran.endpoints.users.User.verified
      :type: bool
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.verified

   .. py:attribute:: role
      :canonical: pyfivetran.endpoints.users.User.role
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.role

   .. py:attribute:: active
      :canonical: pyfivetran.endpoints.users.User.active
      :type: bool
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.active

   .. py:attribute:: created_at
      :canonical: pyfivetran.endpoints.users.User.created_at
      :type: datetime.datetime
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.created_at

   .. py:attribute:: logged_in_at
      :canonical: pyfivetran.endpoints.users.User.logged_in_at
      :type: datetime.datetime
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.logged_in_at

   .. py:attribute:: family_name
      :canonical: pyfivetran.endpoints.users.User.family_name
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.family_name

   .. py:attribute:: given_name
      :canonical: pyfivetran.endpoints.users.User.given_name
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.given_name

   .. py:attribute:: invited
      :canonical: pyfivetran.endpoints.users.User.invited
      :type: typing.Optional[bool]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.invited

   .. py:attribute:: picture
      :canonical: pyfivetran.endpoints.users.User.picture
      :type: typing.Optional[str | bytes]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.picture

   .. py:attribute:: phone
      :canonical: pyfivetran.endpoints.users.User.phone
      :type: typing.Optional[str]
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.phone

   .. py:attribute:: _is_deleted
      :canonical: pyfivetran.endpoints.users.User._is_deleted
      :type: bool
      :value: False

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User._is_deleted

   .. py:property:: as_url
      :canonical: pyfivetran.endpoints.users.User.as_url
      :type: str

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.as_url

   .. py:property:: raw
      :canonical: pyfivetran.endpoints.users.User.raw
      :type: typing.Dict[str, typing.Any]

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.raw

   .. py:property:: connector_memberships
      :canonical: pyfivetran.endpoints.users.User.connector_memberships
      :type: typing.Sequence[pyfivetran.shed.PaginatedApiResponse]

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.connector_memberships

   .. py:property:: group_memberships
      :canonical: pyfivetran.endpoints.users.User.group_memberships
      :type: typing.Sequence[pyfivetran.shed.PaginatedApiResponse]

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.group_memberships

   .. py:method:: delete() -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.users.User.delete

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.delete

   .. py:method:: add_connector_membership(connector_id: str, role: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.users.User.add_connector_membership

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.add_connector_membership

   .. py:method:: add_group_membership(group_id: str, role: str) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.users.User.add_group_membership

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User.add_group_membership

   .. py:method:: _from_dict(endpoint, d: typing.Dict[str, typing.Any]) -> pyfivetran.endpoints.users.User
      :canonical: pyfivetran.endpoints.users.User._from_dict
      :classmethod:

      .. autodoc2-docstring:: pyfivetran.endpoints.users.User._from_dict

.. py:class:: UserEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.users.UserEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.users.UserEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.users.UserEndpoint.BASE_URL

   .. py:method:: invite_user(email: str, family_name: str, given_name: str, phone: typing.Optional[str] = None, picture: typing.Optional[str] = None, role: typing.Optional[str] = None) -> pyfivetran.endpoints.users.User
      :canonical: pyfivetran.endpoints.users.UserEndpoint.invite_user

      .. autodoc2-docstring:: pyfivetran.endpoints.users.UserEndpoint.invite_user

   .. py:method:: get_users(limit: typing.Optional[int] = None) -> typing.Sequence[pyfivetran.endpoints.users.User]
      :canonical: pyfivetran.endpoints.users.UserEndpoint.get_users

      .. autodoc2-docstring:: pyfivetran.endpoints.users.UserEndpoint.get_users
