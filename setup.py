from setuptools import setup


install_requires = [
    'aiohttp==3.6.2',
    'uvloop==0.14.0',
    'aiohttp-jinja2==1.2.0',
    'pytest==5.4.2',
    'pytest-aiohttp==0.3.0',
    'pytest-asyncio==0.12.0',
]


setup(
    name='aiohttp-test-aideco',
    version='0.1',
    install_requires=install_requires,
)
