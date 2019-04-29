"""
Based on Django Settings https://github.com/django/django/blob/stable/1.11.x/django/conf/__init__.py

"""
import os
import importlib
import logging
from .exceptions import ImproperlyConfigured

ENVIRONMENT_VARIABLE = "SETTINGS_MODULE"
empty = object()


class LazyProxy(object):
    def __init__(self, cls, *params, **kwargs):
        self.__dict__["_cls"] = cls
        self.__dict__["_params"] = params
        self.__dict__["_kwargs"] = kwargs

        self.__dict__["_obj"] = None

    def __init_obj(self):
        self.__dict__["_obj"] = self.__dict__["_cls"](*self.__dict__["_params"], **self.__dict__["_kwargs"])

    def __call__(self):
        """
        Initializes expensive object and returns it
        :return: Your custom object with parameters from LazySetting initializer
        """
        return self.__dict__["_cls"](*self.__dict__["_params"], **self.__dict__["_kwargs"])


class LazyInit(object):
    def __new__(cls, new_object, *args, **kwargs):
        return LazyProxy(new_object, *args, **kwargs)


class LazySetting(LazyInit):

    def __init__(self, obj, *args, **kwargs):
        print("Init")


class BaseSettings(object):
    """
    Common logic for settings whether set by a module or by the user
    """

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)


class Settings(BaseSettings):
    def __init__(self, settings_module):
        """
        Configures all the settings overriding the provided by the user
        :param settings_module: User provided settings module (settings.py)
        """
        #  update this dict from global settings but only for CAPITALS settings
        try:
            self.SETTINGS_MODULE = settings_module
            mod = importlib.import_module(
                self.SETTINGS_MODULE)
        except ImportError:
            logging.error("We can't import your SETTINGS_MODULE, it must be a python module, "
                          "check the format \{module\}.\{settings\} (no .py extension)")
            raise ImproperlyConfigured("Cannot import SETTINGS_MODULE")
        except Exception as e:
            logging.error("Error trying to import your settings module")

        self._explicit_settings = set()
        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)
                self._explicit_settings.add(setting)

    def is_overridden(self, setting):
        return setting in self._explicit_settings

    def __repr__(self):
        return '<%(cls)s "%(settings_module)s">' % {
            'cls': self.__class__.__name__,
            'settings_module': self.SETTINGS_MODULE
        }


class SetupSettings(object):

    def __init__(self):
        self._wrapped = empty

    def _setup(self, name=None):
        """
        Load the settings module pointed to by the env variable.

        """
        settings_module = os.environ.get(ENVIRONMENT_VARIABLE)
        if not settings_module:
            desc = ("setting %s" % name) if name else "settings"
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable %s "
                "or call settings.configure() before accessing settings"
                % (desc, ENVIRONMENT_VARIABLE)
            )
        self._wrapped = Settings(settings_module)

    def __getattr__(self, item):  # TODO: Implement lazy pattern and quit this functionallity
        if self._wrapped is empty:
            self._setup(item)
        get_attr = getattr(self._wrapped, item)
        if isinstance(get_attr, LazyProxy):
            try:
                get_attr = get_attr()
            except Exception as ex:
                raise ImproperlyConfigured(
                    "You didn't set your object properly"
                    "You must use the LazySetting and pass your object without initializing it"
                    "LazySetting(MyCustomClass, [params])"
                    "Exception: %s - %s" % (type(ex), ex.__repr__())
                )
        return get_attr

    def configure(self, default_settings, **options):
        """
        Called to manually configure the settings. The 'default_settings'
        parameter sets where to retrieve any unspecified values from
        (its arguments must support attribute access (__getattr__))
        :param default_settings:
        :param options:
        :return:
        """
        if self._wrapped is not empty:
            raise RuntimeError('Settings already configured.')
        else:
            for setting in dir(default_settings):
                if setting.isupper():
                    setattr(self, setting, getattr(default_settings, setting))

    @property
    def configured(self):
        """
        Returns True if the settings have already been configured
        :return: True/False
        """
        return self._wrapped is not empty


settings = SetupSettings()
