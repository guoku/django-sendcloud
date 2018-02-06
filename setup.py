from setuptools import setup, find_packages
# import os
# import platform

DESCRIPTION = "A Django email backend for SendCloud"

LONG_DESCRIPTION = None

try:
    LONG_DESCRIPTION = open('README.md').read()
except:
    LONG_DESCRIPTION = "django send cloud"

CLASSIFIERS = [
    'Development Status :: 5 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

install_requires = [
                    'Django >= 1.11',
                    'requests >= 2.1',
                   ],

setup(
    name='django-sendcloud',
    version='0.5',
    packages=['sendcloud'],
    author='jiaxin',
    author_email='edison7500@gmail.com',
    url='https://github.com/edison7500/django-sendcloud',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    install_requires=install_requires,
    classifiers=CLASSIFIERS,
    zip_safe = False,
)

__author__ = 'edison7500'
