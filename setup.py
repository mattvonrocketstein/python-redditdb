#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PACKAGE_NAME = 'redditdb'
REQUIREMENTS = [
    'praw', 'python-dotenv', "click",
    'memoized-property',
    'loggable==0.2.0',
    # "smartsheet-python-sdk==10.1.3.3",

]
GITHUB_REQUIREMENTS = [
    # 'https://github.com/dmfigol/smartsheet-python-sdk/archive/no-setuptools-scm.zip#egg=smartsheet-python-sdk-10.1.3.3',
    'https://github.com/mattvonrocketstein/python-loggable/archive/master.zip#egg=loggable-0.2.0',
]

setup(
    name=PACKAGE_NAME,
    version='0.1.0',
    author="mvr",
    description="use a subreddit as a database backend",
    author_email='no-reply@example.com',
    url='https://github.com/mattvonrocketstein/redditdb',
    packages=find_packages(),
    install_requires=REQUIREMENTS,
    dependency_links=GITHUB_REQUIREMENTS,
    zip_safe=False,
    entry_points={
        'console_scripts':
        ['redditdb = {0}.bin.main:entry'.format(PACKAGE_NAME), ]},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
