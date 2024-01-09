# The MIT License (MIT)
# Copyright © 2023 Yuma Rao

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

import re
from os import path
from io import open
from setuptools import setup, find_namespace_packages

def read_requirements(path):
    with open(path, 'r') as f:
        requirements = f.read().splitlines()
        processed_requirements = []
        
        for req in requirements:
            # For git or other VCS links
            if req.startswith('git+') or '@' in req:
                pkg_name = re.search(r'(#egg=)([\w\-_]+)', req)
                if pkg_name:
                    processed_requirements.append(pkg_name.group(2))
                else:
                    # You may decide to raise an exception here, 
                    # if you want to ensure every VCS link has an #egg=<package_name> at the end
                    continue
            else:
                processed_requirements.append(req)
        return processed_requirements


requirements = read_requirements('requirements/bittranslate.txt')
here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


with open(path.join(here, 'VERSION'), encoding='utf-8') as f:
    __version__ = f.read().strip()

setup(
    name='bittranslate',
    version=__version__,
    description='A subnet for machine translation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LucrosusCapital/bittranslate',
    author='Lucrosus Capital LPS',
    packages=find_namespace_packages(),
    include_package_data=True,
    author_email='contact@bittranslate.io',
    license='Apache 2.0 License',
    data_files=[(
        'requirements', ['requirements/bittranslate.txt']
    )],
    python_requires='>=3.9',
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish
        "License :: OSI Approved :: Apache Software License",
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
