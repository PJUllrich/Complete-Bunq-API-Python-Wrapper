import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="bunq_api_sdk",
    version="0.1.0",
    author="Peter Ullrich",
    author_email="peter.j.ullrich@gmail.com",
    description=("A SDK for the Bunq API through which all HTTP "
                 "requests can be made in a simple manner."),
    install_requires=[
        "cryptography",
        "requests",
        "Faker"
    ],
    license="MIT",
    keywords="bunq api wrapper sdk",
    url="https://github.com/PJUllrich/Complete-Bunq-API-Python-Wrapper",
    packages=['apiwrapper', 'tests'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
