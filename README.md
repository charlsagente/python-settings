# python-settings
This module provides you easy access to your **config/settings** properties from all your python modules, it supports normal and lazy initialization for each property. It is based on 
 [django.conf.settings](https://github.com/django/django/blob/stable/1.11.x/django/conf/__init__.py#L58').
 
 ## Installation
 From pip
 ```bash
 pip install python-settings
```

Or

Clone this repo and type
```bash
python setup.py install
```

 ## Usage
 There are two ways to initialize this library
 *  **Manual configuration**. Using python modules
 
    ```python
    # Avoid this way after installing python_settings
    from python_settings.tests.settings.base_settings import URL_CONFIG 
    from python_settings.tests.settings import base_settings
    
    #Using this module
    from python_settings import settings
    settings.configure(base_settings) # configure() receives a python module
    assert settings.configured
    assert settings.URL_CONFIG == URL_CONFIG # now you can use settings in all your project
 
    ```  
 * Using an **environment variable**. You must have an environment variable called **SETTINGS_MODULE** pointing to your settings module in the format {module}.
 {settings}. With no .py extension.
 
    Example:
   ```bash
    export SETTINGS_MODULE='myproject.settings' 
   ```
    or
    
   ```python
   import os
   os.environ["SETTINGS_MODULE"] = 'myproject.settings' 
   ```

Example of the settings.py, it must contain variables in capital letter format:
```python
# settings.py
from python_settings import LazySetting

DATABASE_HOST = '10.0.0.1'

DATABASE_NAME = 'DATABASENAME'

LAZY_INITIALIZATION = LazySetting(HeavyInitializationClass, "127.0.0.1:4222") 
# LazySetting(Class, *args, **kwargs)
```
 
And from any module in your code, you should call your settings variables like this example:
 ```python
from python_settings import settings 

print(settings.DATABASE_HOST)
print(settings.DATABASE_NAME)
# The initialization of the object will happen only once
settings.LAZY_INITIALIZATION.instantiated_object_fn() 
``` 

## Example for different environments
You can use as many settings files as you need for different environments.
Example for development environment settings:
```python
# development_settings.py
import os

from .base_settings import *


TOKEN_API = os.environ.get("TOKEN_API")


```
 
 Example for testing environment
 ```python
# testing_settings.py
import os

from .settings import *

DATABASE_HOST = '10.0.0.1'

TOKEN_API = os.environ.get("TOKEN_API")
```

And update your **SETTINGS_MODULE** variable 
 ```bash
export SETTINGS_MODULE = 'myproject.settings.testing_settings'
```
or using the manual config

TODO LIST: 
*   Add compatibility with Python 2.7 in the LazyInitializer 

