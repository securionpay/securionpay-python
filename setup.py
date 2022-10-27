import pathlib

from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
exec(open(HERE / "securionpay/__version__.py").read())
INSTALL_REQUIRES = (HERE / "requirements.txt").read_text().splitlines()


setup(
    name="securionpay",
    version=__version__,
    description="Python library for SecurionPay API",
    long_description="Python library for SecurionPay API",
    url="https://github.com/securionpay/securionpay-python",
    author="SecurionPay Team",
    author_email="support@securionpay.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="payment",
    packages=find_packages(exclude=["tests*"]),
    install_requires=INSTALL_REQUIRES,
    test_suite="tests",
)
