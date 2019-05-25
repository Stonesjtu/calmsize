from setuptools import setup, find_packages
import os

long_description = (
    open('README.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n' +
    'Download\n'
    '========\n'
    )

setup(
    name="calmsize",
    version="0.9.1",
    description="Fork from hurry.filesize, A simple Python library for human readable file sizes (or anything sized in bytes).",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='file size bytes',
    author='Kaiyu Shi',
    author_email='skyisno.1@gmail.com',
    url='',
    license='ZPL 2.1',
    packages=find_packages('calmsize'),
    package_dir= {'': 'calmsize'},
    # namespace_packages=['calmsize'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
    ],
)
