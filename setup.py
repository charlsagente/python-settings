from distutils.core import setup


setup(
    name='python_settings',
    version='0.1',
    packages=['python_settings.conf'],
    url='https://github.com/charlsagente/python-settings-module',
    license='MIT',
    author='Carlos Perez',
    include_package_data=True,
    author_email='charlsagente@gmail.com',
    long_description=open("README.md", "r").read(),
    description='Simple module to have easy access to settings variables in all your python modules with no need of 3rd party libs',
    classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python'
        ]
)
