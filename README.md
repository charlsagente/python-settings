[![Build Status](https://travis-ci.org/charlsagente/python-settings.svg?branch=master)](https://travis-ci.org/charlsagente/python-settings)

# python-settings
This utility provides you easy access to your **config/settings** properties from all your python modules, it supports regular and lazy instantiations. 

This project is based on 
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

 ## How to configure

Create a python file like **settings.py** in your project, all your constants must be defined using **UPPERCASE** 
like the following examples:

```python
# settings.py

# Creating constants

DATABASE_HOST = '10.0.0.1'

DATABASE_NAME = 'DATABASENAME'

```

Then you have two options:
 
 * Option 1. Using an **environment variable**. 
 You must have an environment variable named **SETTINGS_MODULE** and as a value the path of your python settings file (no .py extension).
 
    Example in bash:
   ```bash
    export SETTINGS_MODULE=settings
   ```
   
    Example in Python
    
   ```python
   import os
   os.environ["SETTINGS_MODULE"] = 'settings' 
   ```
   
 *  Option 2. Calling the **configure** method from our settings module and passing your python module
 
    ```python
    from python_settings import settings
    from . import settings as my_local_settings
    
    settings.configure(my_local_settings) # configure() receives a python module
    assert settings.configured # now you are set
    ```  
 
   
## How to use

Import our settings module and your CONSTANTS will be available in every part of your project:
```python
from python_settings import settings 

print(settings.DATABASE_HOST) # Will print '10.0.0.1'
print(settings.DATABASE_NAME) # Will print 'DATABASENAME'
``` 


Please be careful with your settings file. It should only contain CONSTANTS and not complex code, specially if you are importing third party libraries. 

## Lazy Initialization 

Every time you start/restart your python project, 
everything in your setting file is being loaded, you should keep this file fast but 
if you are dealing with heavy to instantiate objects like
database connections or similar network calls you will expect some performance issues at loading time. 

Using Lazy Initialization increases the performance of this process, 
changing the behavior of evaluating the CONSTANTS only when they are needed.   

### Use the Lazy Initializer

In your python settings file, you have to import our LazySetting class located in python_settings.


```python
from python_settings import LazySetting
from my_awesome_library import HeavyInitializationClass # Heavy to initialize object

LAZY_INITIALIZATION = LazySetting(HeavyInitializationClass, "127.0.0.1:4222") 
# LazySetting(Class, *args, **kwargs)

```

Only the first time you call LazySetting, the HeavyInitializationClass will be instantiated and the 
*args and **kwargs parameters will be passed. Every time you call the LazySetting your same instance will be returned.  

And now from any place in your code, you have to call your CONSTANT
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
or use the config function

TODO LIST: 
* Add function to update default environment variable name
* Keep this utility simple

