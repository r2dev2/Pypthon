import sys

import setuptools

# Thank you @KentoNishi for this setup.py

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = ""

try:
    with open("requirements.txt", "r") as reqs:
        requirements = reqs.read().split("\n")
except:
    requirements = ""

with open("pypthon/__main__.py", 'r') as fin:
    main_module = fin.read()

with open("pypthon/__init__.py", 'r') as fin:
    previous_init = fin.read()

with open("pypthon/__init__.py", 'w+') as fout:
    fout.write(main_module)

try:
    if "refs/tags/v" in sys.argv[1]:
        versionName = sys.argv[1].replace("refs/tags/v", "")
        del sys.argv[1]
    else:
        raise Exception
except:
    versionName = "0.1.0"

setuptools.setup(
    name="pypthon",
    version=versionName,
    author="Ronak Badhe",
    author_email="ronak.badhe@gmail.com",
    description=long_description.split("\n")[1],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r2dev2bb8/Pypthon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["pyp=pypthon:main"]},
    python_requires=">=3.5",
    install_requires=requirements,
)

with open("pypthon/__init__.py", 'w+') as fout:
    fout.write(previous_init)
