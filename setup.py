#!/usr/bin/python
from setuptools import setup, find_packages
setup(
    name = 'docker-hica',
    version = '0.5',
    packages = find_packages() + ['injectors/'],
    scripts = ['docker-hica'],
    install_requires = ['docker-py'],
    package_data = {
    	'': ['LICENSE', 'README.md', 'VERSION', 'CONTRIBUTORS']
    },
    author = 'Pavel Odvody',
    author_email = 'podvody@redhat.com',
    description = 'None',
    license = 'MIT',
    keywords = 'docker host integrated container application',
    url = 'https://github.com/shaded-enmity/docker-hica'
)
