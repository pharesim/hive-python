Low Level
~~~~~~~~~

HttpClient
----------

A fast ``urllib3`` based HTTP client that features:

* Connection Pooling
* Concurrent Processing
* Automatic Node Failover

The functionality of ``HttpClient`` is encapsulated by ``Hive`` class. You shouldn't be using ``HttpClient`` directly,
unless you know exactly what you're doing.

.. autoclass:: hivebase.http_client.HttpClient
   :members:

-------------

hivebase
---------

HiveBase contains various primitives for building higher level abstractions.
This module should only be used by library developers or people with deep domain knowledge.

**Warning:**
Not all methods are documented. Please see source.

.. image:: https://i.imgur.com/A9urMG9.png

Account
=======

.. automodule:: hivebase.account
   :members:

--------

Base58
======

.. automodule:: hivebase.base58
   :members:

--------

Bip38
=====

.. automodule:: hivebase.bip38
   :members:


--------

Memo
====

.. automodule::hivebase.memo
   :members:


--------

Operations
==========

.. automodule:: hivebase.operations
   :members:


--------

Transactions
============

.. automodule:: hivebase.transactions
   :members:



--------

Types
=====

.. automodule:: hivebase.types
   :members:

--------

Exceptions
==========

.. automodule:: hivebase.exceptions
   :members:
