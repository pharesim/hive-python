Hive - Your Starting Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick Start
-----------
You can start using the library with just a few lines of code, as seen in this quick example:

.. code-block:: python

   # first, we initialize Hive class
   from hive import Hive
   h = Hive()

.. code-block:: python

   # check @pharesim's balance
   >>> h.get_account('pharesim')['hbd_balance']
   '980.211 HBD'

   # lets send $1.0 HBD to @pharesim
   >>> h.commit.transfer(to='pharesim', amount=1, asset='HBD', account='furion')
   {'expiration': '2017-03-12T17:54:43',
    'extensions': [],
    'operations': [['transfer',
      {'amount': '1.000 HBD', 'from': 'furion', 'memo': '', 'to': 'pharesim'}]],
    'ref_block_num': 23008,
    'ref_block_prefix': 961695589,
    'signatures': ['1f1322be9ca0c22b27c0385c929c9863901ac78cdaedea2162024ea040e22c4f8b542c02d96cbc761cbe4a188a932bc715bb7bcaf823b6739a44bb29fa85f96d2f']}

   # yup, its there
   >>> h.get_account('pharesim')['hbd_balance']
   '981.211 HBD'

Importing your Hive Account
============================
`hive-python` comes with a BIP38 encrypted wallet, which holds your private keys.



Alternatively, you can also pass required WIF's to ``Hive()`` initializer.

::

    from hive import Hive
    h = Hive(keys=['<private_posting_key>', '<private_active_key>'])

Using the encrypted wallet is however a recommended way.

Please check :doc:`cli` to learn how to set up the wallet.

Interfacing with hived
=======================
``Hive()`` inherits API methods from ``Hived``, which can be called like so:

.. code-block:: python

   h = Hive()

   h.get_account('pharesim')
   h.get_block(8888888)
   h.get_content('author', 'permlink')
   h.broadcast_transaction(...)
   # and many more

You can see the list of available methods by calling ``help(Hive)``.
If a method is not available trough the Python API, we can call it manually using ``h.exec()``:

.. code-block:: python

   h = Hive()

   # this call
   h.get_followers('furion', 'abit', 'blog', 10)

   # is same as
   h.exec('get_followers',
          'furion', 'abit', 'blog', 10,
           api='follow_api')

Commit and Wallet
=================
``Hive()`` comes equipped with ``Commit`` and ``Wallet``, accessible via dot-notation.

.. code-block:: python

   h = Hive()

   # accessing Commit methods
   h.commit.transfer(...)

   # accessing Wallet methods
   h.wallet.get_active_key_for_account(...)

Please check :doc:`core` documentation to learn more.


Hive
-----

As displayed in the `Quick Start` above, ``Hive`` is the main class of this library. It acts as a gateway to other components, such as
``Hived``, ``Commit``, ``Wallet`` and ``HttpClient``.

Any arguments passed to ``Hive`` as ``kwargs`` will naturally flow to sub-components. For example, if we initialize
Hive with ``hive = Hive(no_broadcast=True)``, the ``Commit`` instance is configured to not broadcast any transactions.
This is very useful for testing.

.. autoclass:: hive.hive.Hive
   :members:


Hived API
----------

Hived contains API generating utilities. ``Hived``'s methods will be automatically available to ``Hive()`` classes.
See :doc:`hive`.

.. _hived-reference:

.. automodule:: hive.hived
   :members:


Setting Custom Nodes
--------------------

There are 3 ways in which you can set custom ``hived`` nodes to use with ``hive-python``.

**1. Global, permanent override:**
You can use ``hivepy set nodes`` command to set one or more node URLs. The nodes need to be separated with comma (,)
and shall contain no whitespaces.

    ::

        ~ % hivepy config
        +---------------------+--------+
        | Key                 | Value  |
        +---------------------+--------+
        | default_vote_weight | 100    |
        | default_account     | furion |
        +---------------------+--------+
        ~ % hivepy set nodes https://api.hive.blog
        ~ % hivepy config
        +---------------------+-------------------------------+
        | Key                 | Value                         |
        +---------------------+-------------------------------+
        | default_account     | furion                        |
        | default_vote_weight | 100                           |
        | nodes               | https://api.hive.blog         |
        +---------------------+-------------------------------+
        ~ % hivepy set nodes https://api.hive.blog,https://api.hive.network
        ~ % hivepy config
        +---------------------+----------------------------------------------------------+
        | Key                 | Value                                                    |
        +---------------------+----------------------------------------------------------+
        | nodes               | https://api.hive.blog,https://api.hive.network           |
        | default_vote_weight | 100                                                      |
        | default_account     | furion                                                   |
        +---------------------+----------------------------------------------------------+
        ~ %


To reset this config run ``hivepy set nodes ''``.

**2. For Current Python Process:**
You can override default `Hived` instance for current Python process, by overriding the `instance` singleton.
You should execute the following code when your program starts, and from there on out, all classes (Blockchain, Account,
Post, etc) will use this as their default instance.

    ::

        from hive.hived import Hived
        from hive.instance import set_shared_hived_instance

        hived_nodes = [
            'https://api.hive.blog',
            'https://api.hive.network',
        ]
        set_shared_hived_instance(Hived(nodes=hived_nodes))


**3. For Specific Class Instance:**
Every class that depends on hived comes with a ``hived_instance`` argument.
You can override said hived instance, for any class you're initializing (and its children).

This is useful when you want to contain a modified ``hived`` instance to an explicit piece of code (ie. for testing).

    ::

        from hive.hived import Hived
        from hive.account import Account
        from hive.Blockchain import Blockchain

        hived_nodes = [
            'https://api.hive.blog',
            'https://api.hive.network',
        ]
        custom_instance = Hived(nodes=hived_nodes)

        account = Account('furion', hived_instance=custom_instance)
        blockchain = Blockchain('head', hived_instance=custom_instance)
