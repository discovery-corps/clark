from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='antelope',
    version='0.1dev',
    packages=['antelope', ],
    license='Apache License, Version 2.0',
    install_requires=requirements,
)
