#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Qunfei Wu",
    author_email='qunfei.wu@outlook.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    description="A python package example with nexus ",
    entry_points={
        'console_scripts': [
            'ocr_package=ocr_package.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ocr_package',
    name='ocr_package',
    packages=find_packages(include=['ocr_package', 'ocr_package.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/qunfei-wu/ocr_package',
    version='0.1.4',
    zip_safe=False,
)
