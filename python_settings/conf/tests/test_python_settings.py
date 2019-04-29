import os
import sys
import unittest


class TestPythonSettings(unittest.TestCase):

    def tearDown(self):
        try:
            del sys.modules['python_settings']
            del sys.modules['python_settings.conf']
            del sys.modules['python_settings.conf.exceptions']
            del sys.modules['python_settings.conf.tests']
            del sys.modules['python_settings.conf.tests.settings']
            del sys.modules['python_settings.conf.tests.settings.base_settings']

        except KeyError:
            pass

    def test_config_environment(self):
        from python_settings.conf.tests.settings.base_settings import URL_CONFIG
        from python_settings.conf import settings
        try:

            os.environ["SETTINGS_MODULE"] = "python_settings.conf.tests.settings.base_settings"
        except Exception:
            raise BaseException('Error: Trying to set environment')

        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(os.environ.get("SETTINGS_MODULE"), "python_settings.conf.tests.settings.base_settings")
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)

    def test_config_new_environment(self):
        from python_settings.conf.tests.settings.development_settings import URL_CONFIG
        from python_settings.conf import settings
        try:
            os.environ["SETTINGS_MODULE"] = "python_settings.conf.tests.settings.development_settings"
        except Exception:
            raise BaseException('Error: Trying to set the environment')
        self.assertEqual(os.environ.get("SETTINGS_MODULE"), "python_settings.conf.tests.settings.development_settings")
        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)

    def test_lazy_config(self):

        from python_settings.conf import settings

        try:
            os.environ["SETTINGS_MODULE"] = "python_settings.conf.tests.settings.lazy_settings"
        except Exception:
            raise BaseException('Error: Trying to set the environment')
        self.assertTrue(type(settings.LAZY_TASK))

        self.assertTrue(settings.configured)
