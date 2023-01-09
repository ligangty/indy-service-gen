"""
Copyright (C) 2023 Red Hat, Inc. 

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

         http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

# !/usr/bin/env python

import re

from setuptools import setup, find_packages

version = "0.0.1"

# f = open('README.md')
# long_description = f.read().strip()
# long_description = long_description.split('split here', 1)[1]
# f.close()
long_description = """
This tool is used to generate a skeleton of indy service maven project.
"""

def _get_requirements(path):
    try:
        with open(path, encoding="utf-8") as f:
            packages = f.read().splitlines()
    except (IOError, OSError) as ex:
        raise RuntimeError(f"Can't open file with requirements: {ex}") from ex
    packages = (p.strip() for p in packages if not re.match(r'^\s*#', p))
    packages = list(filter(None, packages))
    return packages


setup(
    zip_safe=True,
    name="indy_service_gen",
    version=version,
    long_description=long_description,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Utilities",
    ],
    keywords="indy micro-service java maven",
    author="RedHat EXD SPMM",
    license="APLv2",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    install_requires=_get_requirements('requirements.txt'),
    package_data={'indy_service_gen': ['schemas/*.json']},
    test_suite="tests",
    entry_points={
        "console_scripts": ["indy_service_gen = indy_service_gen.cli:run"],
    },
)
