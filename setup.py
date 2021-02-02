from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="restricted_input",
    version="0.2.0",
    description="Alternative to classic input with support for restricting certain characters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FuturisticGoo/restricted_input",
    author="Aman Anifer",
    author_email="fgoo.edu@hash.fyi",
    license="MIT",
    python_requires=">= 3.6",
    keywords=["input","filter input", "restricted","getpass","integer","filter","smart"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Terminals",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    packages=["restricted_input"],
    include_package_data=True,
    install_requires=[],
    
)