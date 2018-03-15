import re
from setuptools import setup

def get_version():
    data = open('rpmbuild_chain/rpmbuild_chain.py', 'r').read()
    m = re.search('^__version__ = [\'"]([^\'"]+)[\'"]', data, re.M)
    if m:
        return m.group(1)
    else:
        raise RuntimeError('Unable to find version string')

setup(
    name='rpmbuild-chain',
    packages=['rpmbuild_chain'],
    install_requires=[
        ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        ],
    version=get_version(),
    entry_points={
        'console_scripts': [
            'rpmbuild-chain = rpmbuild_chain.rpmbuild_chain:cli'
            ]
        },
)
