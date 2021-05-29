# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in masar_collection/__init__.py
from masar_collection import __version__ as version

setup(
	name='masar_collection',
	version=version,
	description='Masar Collection',
	author='KCSC',
	author_email='info@kcsc.com.jo',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
