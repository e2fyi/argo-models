#!/usr/bin/env python
"""The setup script."""

from setuptools import find_packages, setup

with open('version.txt', 'r') as filein:
    version = filein.read().strip()

with open('README.md', 'r') as filein:
    readme = filein.read().strip()

setup_requirements = []
test_requirements = []

setup(
    name='argo-models',
    author="william teo",
    author_email='eterna2@hotmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Generated openapi models for Argo objects.",
    long_description=readme,
    long_description_content_type='text/markdown',    
    url="https://github.com/e2fyi/argo-models",
    download_url="https://github.com/e2fyi/argo-models/archive/v%s.tar.gz" % version,
    include_package_data=True,
    package_data={'': ['version.txt']},
    keywords='argo openapi swagger kubeflow',
    packages=['argo', 'argo.models'],
    setup_requires=setup_requirements,
    python_requires='>=2.7, >=3.4',
    install_requires=['kubernetes'],
    test_suite='tests',
    tests_require=test_requirements,
    version=version,
    zip_safe=False,
)
