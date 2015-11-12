# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='wikimedia_thumbor_result_storage',
    version='0.1.1',
    url='https://github.com/wikimedia/thumbor-result-storage',
    license='MIT',
    author='Gilles Dubuc, Wikimedia Foundation',
    description='Thumbor result file storage',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'thumbor',
    ],
    extras_require={
        'tests': [
            'pyvows',
            'coverage',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
