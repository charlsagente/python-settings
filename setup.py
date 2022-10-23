import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-settings',
    version='0.2.3',
    packages=setuptools.find_packages(),
    url='https://github.com/charlsagente/python-settings',
    license='MIT',
    author='Carlos Perez',
    author_email='charlsagente@gmail.com',
    long_description=long_description,
    long_description_content_type="text/markdown",
    description='This utility provides you easy access to your config/settings CONSTANTS from all your python modules',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Utilities',
        'Programming Language :: Python',
    ]
)
