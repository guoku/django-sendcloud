from setuptools import setup
from sendcloud import version

DESCRIPTION = "A Django email backend for SendCloud"

LONG_DESCRIPTION = None

VERSION = version.__version__

try:
    LONG_DESCRIPTION = open("README.md").read()
except:
    pass


install_requires = (["requests>=2.1"],)

CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "Framework :: Django",
    "Framework :: Django :: 1.11",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(
    name="django-sendcloud",
    version=VERSION,
    packages=["sendcloud"],
    author="jiaxin",
    author_email="edison7500@gmail.com",
    url="https://github.com/edison7500/django-sendcloud",
    license="MIT",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    # platforms=['any'],
    install_requires=['requests >= 2.10'],
    include_package_data=True,
    keywords="django-sendcloud",
    classifiers=CLASSIFIERS,
    zip_safe=False,
)

__author__ = "edison7500"
