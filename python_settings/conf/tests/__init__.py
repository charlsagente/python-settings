import unittest
import sys


class BaseSettingsTest(unittest.TestCase):
    def tearDown(self):
        try:
            del sys.modules['python_settings']
        except Exception as e:
            pass
