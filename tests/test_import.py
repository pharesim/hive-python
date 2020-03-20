# -*- coding: utf-8 -*-
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from hive import *  # noqa
from hivebase import *  # noqa


# pylint: disable=unused-import,unused-variable
def test_import():
    _ = Hive()
    _ = account.PasswordKey
