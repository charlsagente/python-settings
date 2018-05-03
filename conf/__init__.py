import os
import importlib
from .exceptions import ImproperlyConfigured

ENVIRONMENT_VARIABLE = "SETTINGS_MODULE"
empty = object()


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
        self.SETTINGS_MODULE = settings_module
        mod = importlib.import_module(self.SETTINGS_MODULE)

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
            'settings_module':self.SETTINGS_MODULE
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
            desc = ("setting %s"% name) if name else "settings"
            raise ImproperlyConfigured(
                "Requested %s, but settings are not configured. "
                "You must either define the environment variable %s "
                "or call settings.configure() before accessing settings"
                % (desc, ENVIRONMENT_VARIABLE)
            )
        self._wrapped = Settings(settings_module)

    def __getattr__(self, item):
        if self._wrapped is empty:
            self._setup(item)
        return getattr(self._wrapped, item)

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
