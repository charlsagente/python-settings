import os

from python_settings.conf import settings
from python_settings.conf.tests import BaseSettingsTest


class TestPythonSettings(BaseSettingsTest):
    def tearDown(self):
        super().tearDown()
        


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()

    def test_config_environment(self):
        from python_settings.conf.tests.settings.base_settings import URL_CONFIG
        try:

            os.environ.setdefault("SETTINGS_MODULE", "python_settings.conf.tests.settings.base_settings")
        except Exception:
            raise BaseException('Error: Trying to set environment')

        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)

    def test_config_new_environment(self):
        from python_settings.conf.tests.settings.development_settings import URL_CONFIG
        try:
            os.environ.setdefault("SETTINGS_MODULE", "python_settings.conf.tests.settings.development_settings")
        except Exception:
            raise BaseException('Error: Trying to set the environment')

        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)
