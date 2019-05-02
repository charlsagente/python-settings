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

 ## How to start

Define a python module like settings.py in your project, the variable names must be Capital Letters (A-Z), example:
```python
# settings.py

# Variables definition
DATABASE_HOST = '10.0.0.1'

DATABASE_NAME = 'DATABASENAME'

```

## Initializing the library

 There are two ways to initialize this library
 
 * **Automatic config** and preferred way, using an **environment variable**. You must have an environment variable called **SETTINGS_MODULE** pointing to your settings module in the format {module}.
 {name}. With no .py extension.
 
    Example in bash:
   ```bash
    export SETTINGS_MODULE='myproject.base_settings' 
   ```
   
    Example in Python
    
   ```python
   import os
   os.environ["SETTINGS_MODULE"] = 'myproject.base_settings' 
   ```
   
 *  **Manual configuration**. Passing directly your python module to configure()
 
    ```python
    # Avoid this way after installing python_settings
    from python_settings.tests.settings.base_settings import URL_CONFIG 
    from python_settings.tests.settings import base_settings
    
    #Initializing manually
    from python_settings import settings
    settings.configure(base_settings) # configure() receives a python module
    assert settings.configured
    assert settings.URL_CONFIG == URL_CONFIG # now you can use settings in all your project
 
    ```  
 
   
##Usage

And from any module in your code, you should call your settings variables like this example:
 ```python
from python_settings import settings 

print(settings.DATABASE_HOST) # Will print '10.0.0.1'
print(settings.DATABASE_NAME) # Will print 'DATABASENAME'
``` 

## Lazy Initialization 

This saves too much time when you are starting your project, if you are dealing with heavy to instantiate objects like
database connections or similar network calls. 
In your python settings module, you have to import our LazySetting class located in python_settings.


```python
from python_settings import LazySetting
from my_awesome_library import HeavyInitializationClass # Heavy to initialize object

LAZY_INITIALIZATION = LazySetting(HeavyInitializationClass, "127.0.0.1:4222") 
# LazySetting(Class, *args, **kwargs)

```
Only the first time you call this property, the HeavyInitializationClass will be instantiated and the 
*args and **kwargs parameters will be passed. Every time you call this property the same instance will be returned.  

And now from any place in your code, you have to call the property
 ```python
from python_settings import settings 

object_initialized = settings.LAZY_INITIALIZATION # Will return an instance of your object

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
*   Add compatibility with Python 2.7 in the LazyInitializer (maybe)

