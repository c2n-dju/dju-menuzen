#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from dju_menuzen import __version__

REQUIREMENTS = [
    'django-cms>=3.4',
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU AFFERO GPL 3',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='dju_menuzen',
    version=__version__,
    description=('Add menuzen to Django-CMS.'),
    author='Fabrice Pardo',
    author_email='fabrice.pardo@c2n.upsaclay.fr',
    url='https://github.com/fp4code/dju-menuzen',
    license='GNU AFFERO GPL 3',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    # test_suite='tests.settings.run',
)
