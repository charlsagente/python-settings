class ImproperlyConfigured(Exception):
    """
    Something in the settings was not properly configured
    """


class LazyInitializationImproperlyConfigured(ImproperlyConfigured):
    """
    Something in the LazySetting instantiation was not properly configured
    """
