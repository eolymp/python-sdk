import os
import setuptools
import pathlib


for root, dirs, files in os.walk("./eolymp"):
    if os.path.basename(root) == "__pycache__":
        continue
    pathlib.Path(root + os.sep + "__init__.py").touch()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eolymp",
    version=os.getenv("RELEASE_VERSION"),
    author="Sergey Kolodyazhnyy",
    author_email="sergey@eolymp.com",
    description="Eolymp SDK for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eolymp/contracts",
    packages=setuptools.find_packages(),
    package_data={package: ["py.typed", "*.pyi", "**/*.pyi"] for package in setuptools.find_packages()},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
