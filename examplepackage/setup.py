from setuptools import setup, find_packages

setup(
    name="examplepackage",
    version="0.1",
    packages=find_packages(),
    description="A simple greeting package",
    author="Christina A",
    author_email="christina@example.com",
    url="https://github.com/chriaa/python-examples",
    install_requires=[
        'pandas',
        'numpy',
    ],
)