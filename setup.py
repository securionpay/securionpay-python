from setuptools import setup, find_packages

setup(
    name="securionpay",
    version="1.0.1",
    description="Python library for SecurionPay API",
    url="https://github.com/securionpay/securionpay-python",
    author="Grzegorz Terlikowski",
    author_email="terlikowski.grzegorz@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="payment",
    packages=find_packages(exclude=["tests"]),
    install_requires=["requests"],
    extras_require={"test": ["coverage", "mock", "nose"]},
    test_suite="tests",
)
