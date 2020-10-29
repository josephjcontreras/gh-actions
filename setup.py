from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()
description = 'test github actions/workflows'

setup(
    name='actions',
    version='0.0.1a1',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Joseph Contreras',
    author_email='',
    url='',
    packages=find_packages(),
    classifiers=['Development Status::3 - Alpha'],
    include_package_data=True,
    license='MIT')
