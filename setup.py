import setuptools


setuptools.setup(
    name='pasteraw',
    version='1.3.0',
    long_description=__doc__,
    packages=['pasteraw'],
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    install_requires=[
        'flask',
        'flask-wtf',
        'blinker'])
