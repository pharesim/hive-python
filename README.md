# A Python Hive Library

`hive-python` is a Hive library for Python. It comes with a
BIP38 encrypted wallet and a practical CLI utility called `hivepy`.

This library currently works on Python 2.7, 3.5 and 3.6. Python 3.3 and 3.4 support forthcoming.

# Installation

With pip:

```
pip3 install hivepy      # pip install hivepy for 2.7
```

From Source:

```
git clone https://github.com/pharesim/hive-python.git
cd hive-python
python3 setup.py install        # python setup.py install for 2.7
```

## Homebrew Build Prereqs

If you're on a mac, you may need to do the following first:

```
brew install openssl
export CFLAGS="-I$(brew --prefix openssl)/include $CFLAGS"
export LDFLAGS="-L$(brew --prefix openssl)/lib $LDFLAGS"
```

# CLI tools bundled

The library comes with a few console scripts.

* `hivepy`:
    * rudimentary blockchain CLI (needs some TLC and more TLAs)
* `hivetail`:
    * useful for e.g. `hivetail -f -j | jq --unbuffered --sort-keys .`

# Documentation

Documentation is available at **http://hive.readthedocs.io**

# Tests

Some tests are included.  They can be run via:

* `python setup.py test`

# TODO

* more unit tests
* 100% documentation coverage, consistent documentation
* migrate to click CLI library

# Notice

This library is *under development*.  Beware.
