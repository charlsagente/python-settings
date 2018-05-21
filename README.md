# python-settings
Simple module to have easy access to settings variables in all your python modules. It is based on 
 [django.conf.settings](https://github.com/django/django/blob/stable/1.11.x/django/conf/__init__.py#L58').
 
 ## Installation
 From test.pypi
 ```bash
 python -m pip install --index-url https://test.pypi.org/project/ python_settings==0.1.2
```

Or

Clone this repo and type
```bash
python setup.py install
```

 ## Usage
 You must have an environment variable called **SETTINGS_MODULE** pointing to your settings module in the format {module}.
 {settings}. With no .py extension. 
 
 Example:
 ```bash
export SETTINGS_MODULE='myproject.settings'
```

And the settings.py must contain variables in capital letter format:
```python
# settings.py

DATABASE_HOST = '127.0.0.1'

DATABASE_NAME = 'DATABASENAME'
...
```

 
 And from any module in your code, you should call your settings variables like this example:
 ```python
from python_settings.conf import settings 

print(settings.DATABASE_HOST)
print(settings.DATABASE_NAME)
``` 


You can use as many settings files as you need for different environments.
Example for development environment settings:
```python
# development_settings.py
import os

from .settings import *


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