from distutils.core import setup


setup(
    name='python_settings',
    version='0.2',
    packages=['python_settings.conf'],
    url='https://github.com/charlsagente/python-settings-module',
    license='MIT',
    author='Carlos Perez',
    include_package_data=True,
    author_email='charlsagente@gmail.com',
    long_description=open("README.md", "r").read(),
    description='Simple module to have easy access to settings variables in all your python modules ',
    classifiers=[
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python'
        ]
)
