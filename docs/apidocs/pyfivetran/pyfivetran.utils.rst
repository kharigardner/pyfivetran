:py:mod:`pyfivetran.utils`
==========================

.. py:module:: pyfivetran.utils

.. autodoc2-docstring:: pyfivetran.utils
   :allowtitles:

Module Contents
---------------

Functions
~~~~~~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`deserialize_timestamp <pyfivetran.utils.deserialize_timestamp>`
     - .. autodoc2-docstring:: pyfivetran.utils.deserialize_timestamp
          :summary:
   * - :py:obj:`serialize_timezone <pyfivetran.utils.serialize_timezone>`
     - .. autodoc2-docstring:: pyfivetran.utils.serialize_timezone
          :summary:

Data
~~~~

.. list-table::
   :class: autosummary longtable
   :align: left

   * - :py:obj:`logger <pyfivetran.utils.logger>`
     - .. autodoc2-docstring:: pyfivetran.utils.logger
          :summary:

API
~~~

.. py:data:: logger
   :canonical: pyfivetran.utils.logger
   :value: 'getLogger(...)'

   .. autodoc2-docstring:: pyfivetran.utils.logger

.. py:function:: deserialize_timestamp(dt_str: str) -> datetime.datetime
   :canonical: pyfivetran.utils.deserialize_timestamp

   .. autodoc2-docstring:: pyfivetran.utils.deserialize_timestamp

.. py:function:: serialize_timezone(tz: str | datetime.tzinfo) -> int
   :canonical: pyfivetran.utils.serialize_timezone

   .. autodoc2-docstring:: pyfivetran.utils.serialize_timezone
