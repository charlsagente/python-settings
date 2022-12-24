[![CircleCI](https://circleci.com/gh/charlsagente/python-settings.svg?style=svg)](https://app.circleci.com/pipelines/github/charlsagente/python-settings)

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

 ## How to configure

Create a python file like **settings.py** in your project, the variable names must be in Capital Letters (A-Z), example:
```python
# settings.py

# Variables definition
DATABASE_HOST = '10.0.0.1'

DATABASE_NAME = 'DATABASENAME'

```

 Two optional patterns to initialize this library
 
 * Option 1. Using an **environment variable**. 
 You must have an environment variable called **SETTINGS_MODULE** and as a value your just created python settings file in the format {module}.
 {name}. With no .py extension.
 
    Example in bash:
   ```bash
    export SETTINGS_MODULE=settings
   ```
   
    Example in Python
    
   ```python
   import os
   os.environ["SETTINGS_MODULE"] = 'settings' 
   ```
   
 *  Option 2. Calling the configure function from our settings module and passing it your python file
 
    ```python
    from python_settings import settings
    from . import settings as my_local_settings
    
    settings.configure(my_local_settings) # configure() receives a python module
    assert settings.configured # now you are set
    ```  
 
   
## How to use

Import the settings module and access directly to your properties:
```python
from python_settings import settings 

print(settings.DATABASE_HOST) # Will print '10.0.0.1'
print(settings.DATABASE_NAME) # Will print 'DATABASENAME'
``` 

## Lazy Initialization 

Every time you start/restart your python project, 
all your defined variables are evaluated many times, 
if you are dealing with heavy to instantiate objects like
database connections or similar network calls you will expect some delay. 

Using Lazy Initialization increases the performance of this process, 
changing the behavior of evaluating the variables only when is needed.   

### Use the Lazy Initializer

In your python settings file, you have to import our LazySetting class located in python_settings.


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
or use the config function

TODO LIST: 
*   Add function to update default environment variable name

