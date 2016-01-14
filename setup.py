#!/usr/bin/python
from setuptools import setup, find_packages
import os, glob

hica_lib = '/var/lib/docker-hica'
injectors = os.path.join(hica_lib, 'injectors')

if not os.path.exists(hica_lib):
    os.mkdir(hica_lib)

if not os.path.exists(injectors):
    os.mkdir(injectors)
setup(
    name = 'docker-hica',
    version = '0.5',
    packages = find_packages(),
    scripts = ['docker-hica'],
    install_requires = ['docker-py'],
    package_data = {
    	'': ['LICENSE', 'README.md', 'VERSION', 'CONTRIBUTORS']
    },
    author = 'Pavel Odvody',
    author_email = 'podvody@redhat.com',
    description = 'The goal of this project is to define a set of image label metadata and launcher tooling that understands said metadata to provide for smooth experience running containerized applications with tight integration with the host operating system.',
    license = 'MIT',
    keywords = 'docker host integrated container application',
    url = 'https://github.com/shaded-enmity/docker-hica',
    data_files=[(injectors, glob.glob('injectors/*'))]
)
