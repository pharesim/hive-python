Transactions and Accounts
~~~~~~~~~~~~~~~~~~~~~~~~~

Commit
======

The Commit class contains helper methods for `posting, voting, transferring funds, updating witnesses` and more.
You don't have to use this class directly, all of its methods are accessible trough main ``Hive`` class.

.. code-block:: python

   # accessing commit methods trough Hive
   h = Hive()
   h.commit.transfer(...)

   # is same as
   c = Commit(hive=Hive())
   c.transfer(..)

.. autoclass:: hive.hive.Commit
   :members:

--------


TransactionBuilder
==================

.. autoclass:: hive.transactionbuilder.TransactionBuilder
   :members:

--------

Wallet
======

Wallet is a low-level utility.
It could be used to create 3rd party cli and GUI wallets on top of ``hive-python``'s infrastructure.

.. automodule:: hive.wallet
   :members:
