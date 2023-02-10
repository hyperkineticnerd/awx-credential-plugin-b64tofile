#!/usr/bin/env python

from setuptools import setup

requirements = []  # add Python dependencies here
# e.g., requirements = ["PyYAML"]

setup(
    name='awx-credential-plugin-b64tofile',
    version='0.1',
    author='Sean Nelson',
    author_email='hyperkineticnerd@gmail.com',
    description='',
    long_description='',
    license='Apache License 2.0',
    keywords='ansible',
    url='http://github.com/hyperkineticnerd/awx-credential-plugin-b64tofile',
    packages=['awx_credential_plugin_b64tofile'],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=requirements,
    entry_points = {
        'awx.credential_plugins': [
            'b64tofile_plugin = b64tofile_credential_plugin:b64tofile_plugin',
        ]
    }
)
