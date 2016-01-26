#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


def required(fname):
    return filter(lambda x: not x.startswith('-'), open(fname).readlines())

setup(
    name='YOUR_PACKAGE_NAME',
    version='0.0.0',
    description='',
    long_description='',
    author='patillacode@gmail.com',
    author_email='patillacode@gmail.com',
    packages=find_packages('src', exclude=[
        "*.tests", "*.tests.*", "tests.*", "tests",
        "*.ez_setup", "*.ez_setup.*", "ez_setup.*", "ez_setup",
        "*.examples", "*.examples.*", "examples.*", "examples",
    ]),
    namespace_packages=[
        'NAMESPACE_PACKAGE',
    ],
    package_dir={
        '': 'src'
    },
    include_package_data=True,
    install_requires=required('requirements.txt'),
    license="",
    zip_safe=False,
    keywords='',
    classifiers=[
        "Programming Language :: Python",
    ],
    test_suite='nose.collector',
    tests_require=required('requirements-dev.txt')
)
