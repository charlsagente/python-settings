import os
import unittest

from python_settings.conf.tests.settings.base_settings import URL_CONFIG, DEFAULT_VALUE, DEFAULT_CONSTANT
from python_settings.conf import settings


class TestPythonSettingsModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['SETTINGS_MODULE'] = 'python_settings.conf.tests.settings.base_settings'

    def test_config_a(self):
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertEqual(settings.DEFAULT_VALUE, DEFAULT_VALUE)
        self.assertEqual(settings.DEFAULT_CONSTANT, DEFAULT_CONSTANT)

    def test_config_b(self):
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertEqual(settings.DEFAULT_VALUE, DEFAULT_VALUE)
        self.assertEqual(settings.DEFAULT_CONSTANT, DEFAULT_CONSTANT)
