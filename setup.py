from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in thirvu_app/__init__.py
from thirvu_app import __version__ as version

setup(
	name="thirvu_app",
	version=version,
	description="apps for all ",
	author="manikanda prabhu",
	author_email="prabhukennedy1999@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
