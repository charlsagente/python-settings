import os
import unittest
from conf import settings


class TestPythonSettings(unittest.TestCase):
    def test_config_environment(self):
        from conf.tests.settings.base_settings import URL_CONFIG
        os.environ.setdefault("SETTINGS_MODULE", "conf.tests.settings.base_settings")
        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)

    def test_config_new_environment(self):
        from conf.tests.settings.development_settings import URL_CONFIG
        os.environ.setdefault("SETTINGS_MODULE", "conf.tests.settings.development")
        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)


