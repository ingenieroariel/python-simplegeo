#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="simplegeo",
      version="0.0.1",
      description="Library for interfacing with SimpleGeo's API",
      author="Joe Stump",
      author_email="joe@simplegeo.com",
      url="http://github.com/simplegeo/python-simplegeo",
      packages = find_packages(),
      license = "MIT License",
      keywords="simplegeo",
      zip_safe = True,
      tests_require=['nose', 'coverage'])