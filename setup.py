from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ipcore",
    version="0.1.2",
    description="A Python library to query IP addresses using ipquery.io API",
    author="IPQuery",
    author_email="admin@ipquery.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ipqwery/ipapi-py",
    packages=find_packages(),
    install_requires=[
        "httpx>=0.24.0",
        "pydantic>=2.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
