#!/usr/bin/env python

"""The setup script."""
import os
from setuptools import setup, find_packages

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


requirements = ['requests', 'openpyxl']

test_requirements = ['pytest']

setup(
    author="Han Zhichao",
    author_email='superhin@126.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Excel http api test",
    install_requires=requirements,
    license="MIT license",
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=['excel runner', 'excel http runner', 'excel http test', 'excel api test'],
    name='excel-runner',
    packages=find_packages(include=['excel_runner', 'excel_runner.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/hanzhichao/excel-runner',
    version='0.1.2',
    zip_safe=False,
)
