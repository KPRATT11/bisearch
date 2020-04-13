from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup (
    name='bisearch',
    version = '0.0.1',
    descriptions='Implements Binary Search Functions',
    py_modules=["bisearch"],
    package_dir={'': 'src'},

    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],

    long_description = long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/KPRATT11/bisearch",
    author_email = "pratt.keegan@gmail.com"
)