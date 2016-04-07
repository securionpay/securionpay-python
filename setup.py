from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='securionpay',

    version='0.0.1',

    description='SecurionPay Python wrapper',
    long_description=long_description,

    url='https://securionpay.com',

    author='Grzegorz Terlikowski',
    author_email='terlikowski.grzegorz@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='payment',

    packages=find_packages(exclude=['tests']),

    install_requires=['requests'],

    # $ pip install -e .[dev,test]
    extras_require={
        # 'dev': ['check-manifest'],
        'test': ['coverage', 'mock', 'nose'],
    },
    test_suite="tests",

    package_data={
        # 'sample': ['package_data.dat'],
    },

    # data_files=[('my_data', ['data/data_file'])],

    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
