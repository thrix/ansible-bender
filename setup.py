#!/usr/bin/python3

import os

from setuptools import find_packages, setup

# https://packaging.python.org/guides/single-sourcing-package-version/
version = {}
with open("./ab/version.py") as fp:
    exec(fp.read(), version)

long_description = ''.join(open('README.md').readlines())

setup(
    name='ab',
    version=version["__version__"],
    description="Proof of concept implementation of a tool which builds container images using Ansible playbooks.",
    long_description=long_description,
    # long_description_content_type='text/markdown',
    packages=find_packages(exclude=['tests']),
    install_requires=[],
    entry_points='''
        [console_scripts]
        ab=ab.cli:main
    ''',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    keywords='containers,ansible,buildah',
    author='Red Hat',
    author_email='tomas@tomecek.net',
    url='https://github.com/TomasTomecek/ab',
    include_package_data=True,
)