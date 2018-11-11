#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

PACKAGE_NAME = 'redditdb'
REQUIREMENTS = [
    'praw', 'python-dotenv', "click",
    'memoized-property',
]
GITHUB_REQUIREMENTS = [
    'http://github.com/mattvonrocketstein/python-loggable/tarball/master#egg=loggable',
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
