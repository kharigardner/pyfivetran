:py:mod:`pyfivetran.endpoints.certificate`
==========================================

.. py:module:: pyfivetran.endpoints.certificate

.. autodoc2-docstring:: pyfivetran.endpoints.certificate
   :allowtitles:

Module Contents
---------------

Classes
~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`CertificateEndpoint <pyfivetran.endpoints.certificate.CertificateEndpoint>`
     -

API
~~~

.. py:class:: CertificateEndpoint(client: pyfivetran.endpoints.base.Client)
   :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint

   Bases: :py:obj:`pyfivetran.endpoints.base.Endpoint`

   .. py:attribute:: BASE_URL
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.BASE_URL
      :type: str
      :value: None

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.BASE_URL

   .. py:method:: approve_certificate(hash: str, encoded_cert: str | bytes, destination_id: typing.Optional[str] = None, connector_id: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.approve_certificate

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.approve_certificate

   .. py:method:: approve_fingerprint(hash: str, public_key: str | bytes, connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.approve_fingerprint

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.approve_fingerprint

   .. py:method:: get_certificate_details(hash: str | bytes, connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.get_certificate_details

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.get_certificate_details

   .. py:method:: get_fingerprint_details(hash: str | bytes, connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.get_fingerprint_details

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.get_fingerprint_details

   .. py:method:: get_fingerprints(connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None, limit: typing.Optional[int] = None) -> typing.List[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.get_fingerprints

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.get_fingerprints

   .. py:method:: get_certificates(connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None, limit: typing.Optional[int] = None) -> typing.List[pyfivetran.shed.PaginatedApiResponse]
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.get_certificates

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.get_certificates

   .. py:method:: revoke_certificate(hash: str | bytes, connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.revoke_certificate

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.revoke_certificate

   .. py:method:: revoke_fingerprint(hash: str | bytes, connector_id: typing.Optional[str] = None, destination_id: typing.Optional[str] = None) -> pyfivetran.shed.GeneralApiResponse
      :canonical: pyfivetran.endpoints.certificate.CertificateEndpoint.revoke_fingerprint

      .. autodoc2-docstring:: pyfivetran.endpoints.certificate.CertificateEndpoint.revoke_fingerprint
