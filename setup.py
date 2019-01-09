from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='vector-controller',
    version='0.5.1',
    description='A webpage-based controller for Anki Vector',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/krconv/vector-controller',
    author='Kodey Converse',
    author_email='kodey@krconv.com',
    packages=find_packages(exclude=['tests']),
)