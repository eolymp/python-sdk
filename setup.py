import os
import sys
import setuptools

# create __init__ in each namespace and export everything
source = "." + os.sep + "eolymp"
for module in os.listdir(source):
    path = source + os.sep + module
    if not os.path.isdir(path):
        continue

    init = path + os.sep + "__init__.py"

    print("creating", init, "file")
    with open(init, "w", encoding="utf-8") as fh:
        for file in os.listdir(path):
            name = os.path.splitext(file)
            ext = name[1] if len(name) > 1 else ''

            if os.path.isdir(path + os.sep + file) or ext != '.py' or name[0] == '__init__':
                continue

            fh.write("from .{} import *\n".format(name[0]))


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
