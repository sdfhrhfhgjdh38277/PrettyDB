from setuptools import setup, find_packages

setup(
    name='PyDb',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PrettyTable',
        'cryptography',
        'loguru'
    ],
)