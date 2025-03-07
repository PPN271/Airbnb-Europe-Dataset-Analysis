# A minimal setup.py file to make a Python project installable.
#
# Note that while we are following modern packaging practices
# with setuptools metadata being declaratively stored in setup.cfg
# and build configuration listed in pyproj.toml, pip/setuptools
# as of this writing (early 2022) still require a minimal setup.py
# file in order to support editable development installs (pip install -e .)

from setuptools import setup, find_packages

setup(
    name="utils",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.10",
)