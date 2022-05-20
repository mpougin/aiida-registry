# -*- coding: utf-8 -*-
"""Setup for AiiDA registry."""

from __future__ import absolute_import

from setuptools import find_packages, setup

if __name__ == '__main__':
    setup(
        name='aiida-registry',
        packages=find_packages(),
        long_description=open('README.md', encoding='utf8').read(),  # pylint: disable=consider-using-with
        long_description_content_type='text/markdown',
        version='0.3.0',
        description='Registry of AiiDA plugins.',
        author='AiiDA Team',
        author_email='aiidateam@gmail.com',
        url='https://aiidateam.github.io/aiida-registry/',
        scripts=['bin/aiida-registry'],
        install_requires=[
            'jinja2~=2.11',
            'requests~=2.24',
            'requests-cache~=0.5.2',
            'requirements-parser~=0.2.0',
            'poetry~=1.1',
            'tomlkit',
            'click~=7.1',
            'pyyaml~=6.0',
            'docker~=5.0',
            # https://github.com/aws/aws-sam-cli/issues/3661
            'markupsafe~=2.0.1'
        ],
        license='MIT',
        extras_require={
            'pre-commit': [
                'pre-commit~=2.2',
                'pylint~=2.11.0',
            ],
            'testing': ['pytest', 'pytest-regressions'],
        },
        include_package_data=True,
    )