from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = "A Django email backend for SendCloud"

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='django-sendcloud',
    version='0.4',
    packages=['sendcloud'],
    author='jiaxin',
    author_email='jiaxin@guoku.com',
    url='http://github.com/guoku/django-sendcloud/',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    install_requires=['requests==2.6.0', 'django==1.11.23'],
    classifiers=CLASSIFIERS,
    zip_safe = False,
)

__author__ = 'edison7500'
