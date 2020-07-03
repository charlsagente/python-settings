import os
import sys
import unittest

DEFAULT_PYTHON_SETTINGS = 'python_settings.tests.settings.base_settings'


class TestPythonSettings(unittest.TestCase):

    def tearDown(self):
        try:
            del sys.modules['python_settings']
            del sys.modules['python_settings.conf']
            del sys.modules['python_settings.conf.exceptions']
            del sys.modules['python_settings.conf.tests']
            del sys.modules['python_settings.conf.tests.settings']
            del sys.modules[DEFAULT_PYTHON_SETTINGS]

        except KeyError:
            pass

    @classmethod
    def setUpClass(cls):
        os.environ['SETTINGS_MODULE'] = DEFAULT_PYTHON_SETTINGS

    def test_config_compare_defaults_a(self):
        from python_settings import settings
        from python_settings.tests.settings.base_settings import URL_CONFIG, DEFAULT_VALUE, DEFAULT_CONSTANT
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertEqual(settings.DEFAULT_VALUE, DEFAULT_VALUE)
        self.assertEqual(settings.DEFAULT_CONSTANT, DEFAULT_CONSTANT)

    def test_config_compare_defaults_b(self):
        from python_settings import settings
        from python_settings.tests.settings.base_settings import URL_CONFIG, DEFAULT_VALUE, DEFAULT_CONSTANT
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertEqual(settings.DEFAULT_VALUE, DEFAULT_VALUE)
        self.assertEqual(settings.DEFAULT_CONSTANT, DEFAULT_CONSTANT)

    def test_attribute_error(self):
        from python_settings import settings
        # make sure AttributeError is thrown for missing Attribute
        with self.assertRaises(AttributeError) as a:
            print(settings.NOT_A_SETTING)
        # make sure we get the default value out of getattr
        self.assertEqual(getattr(settings, 'NOTHING', 'default'), 'default')

    def test_config_environment(self):
        from python_settings.tests.settings.base_settings import URL_CONFIG
        from python_settings import settings

        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(os.environ.get('SETTINGS_MODULE'), DEFAULT_PYTHON_SETTINGS)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)

    def test_config_new_environment(self):
        from python_settings.tests.settings.development_settings import URL_CONFIG
        from python_settings import settings
        development_settings = 'python_settings.tests.settings.development_settings'
        try:
            os.environ['SETTINGS_MODULE'] = development_settings
        except Exception:
            raise BaseException('Error: Trying to set the environment')
        self.assertEqual(os.environ.get('SETTINGS_MODULE'), development_settings)
        self.assertIsNotNone(settings.URL_CONFIG)
        self.assertEqual(settings.URL_CONFIG, URL_CONFIG)
        self.assertTrue(settings.configured)

    def test_lazy_config(self):

        from python_settings import settings

        try:
            os.environ['SETTINGS_MODULE'] = 'python_settings.tests.settings.lazy_settings'
        except Exception:
            raise BaseException('Error: Trying to set the environment')

        self.assertTrue(type(settings.LAZY_TASK))
        self.assertTrue(type(settings.LAZY_TASK))  # For debugging purposes to check lazy initializer behavior

        self.assertTrue(settings.configured)

    def test_lazy_initialization(self):
        from python_settings import settings
        from python_settings.tests.settings import lazy_settings
        try:
            os.environ['SETTINGS_MODULE'] = 'python_settings.tests.settings.lazy_settings'
        except Exception:
            raise BaseException('Error: Trying to set the environment')

        settings.configure(default_settings=lazy_settings)
        self.assertTrue(settings.configured)
        self.assertTrue(settings.LAZY_TASK)
        self.assertTrue(settings.LAZY_TASK_HEAVY_INITIALIZATION)

    def test_wrong_settings_module(self):
        from python_settings import settings
        from python_settings import ImproperlyConfigured
        try:
            os.environ['SETTINGS_MODULE'] = 'python_settings.tests.wrong_settings_module'
        except Exception:
            raise BaseException('Error: Trying to set the environment')
        with self.assertRaises(ImproperlyConfigured) as c:
            print(settings.CONFIG)
