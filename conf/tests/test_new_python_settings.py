import os
import unittest
from conf import settings


class TestNewPythonSettings(unittest.TestCase):
    def test_case_settings(self):
        from conf.tests.settings.development_settings import URL_CONFIG
        os.environ.setdefault("SETTINGS_MODULE", "conf.tests.settings.development")
        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)