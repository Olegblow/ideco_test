from setuptools import setup


install_requires = [
    'aiofiles',
    'aiohttp',
    'uvloop',
]


setup(
    name='aiohttp-simple-project',
    version='0.1',
    install_requires=install_requires,
)