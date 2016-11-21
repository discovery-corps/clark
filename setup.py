from distutils.core import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='clark',
    version='0.1dev',
    packages=['clark', ],
    license='Apache License, Version 2.0',
    install_requires=requirements,
)
