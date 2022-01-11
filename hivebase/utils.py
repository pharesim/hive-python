import sys


def compat_bytes(item, encoding=None):
    """
    This method is required because Python 2.7 `bytes` is simply an alias for `str`. Without this method,
    code execution would look something like:

    class clazz(object):

        def __bytes__(self):
            return bytes(5)


    Python 2.7:

    c = clazz()
    bytes(c)
    >>'<__main__.clazz object at 0x105171a90>'

    In this example, when `bytes(c)` is invoked, the interpreter then calls `str(c)`, and prints the above string.
    the method `__bytes__` is never invoked.

    Python 3.6:
    c = clazz()
    bytes(c)
    >>b'\x00\x00\x00\x00\x00'

    This is the expected and necessary behavior across both platforms.

    w/ compat_bytes method, we will ensure that the correct bytes method is always invoked, avoiding the `str` alias in
    2.7.

    :param item: this is the object who's bytes method needs to be invoked
    :param encoding: optional encoding parameter to handle the Python 3.6 two argument 'bytes' method.
    :return: a bytes object that functions the same across 3.6 and 2.7
    """
    if hasattr(item, '__bytes__'):
        return item.__bytes__()
    else:
        if encoding:
            return bytes(item, encoding)
        else:
            return bytes(item)


def compat_chr(item):
    """
    This is necessary to maintain compatibility across Python 2.7 and 3.6.
    In 3.6, 'chr' handles any unicode character, whereas in 2.7, `chr` only handles
    ASCII characters. Thankfully, the Python 2.7 method `unichr` provides the same
    functionality as 3.6 `chr`.

    :param item: a length 1 string who's `chr` method needs to be invoked
    :return: the unichr code point of the single character string, item
    """
    if sys.version >= '3.0':
        return chr(item)
    else:
        return unichr(item)


def compat_json(data, ignore_dicts=False):
    """
    :param data: Json Data we want to ensure compatibility on.
    :param ignore_dicts: should only be set to true when first called.
    :return: Python compatible 2.7 byte-strings when encountering unicode.
    """
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byte-string values
    if isinstance(data, list):
        return [compat_json(item, ignore_dicts=True) for item in data]
    # if this is a dictionary, return dictionary of byte-string keys and values
    # but only if we haven't already byte-string it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            compat_json(key, ignore_dicts=True): compat_json(value, ignore_dicts=True)
            for key, value in data.items()
        }
    # if it's anything else, return it in its original form
    return data
