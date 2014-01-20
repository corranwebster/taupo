# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

import os.path
from setuptools import setup

info = {}
execfile(os.path.join('taupo', '__init__.py'), info)

setup(
    name='taupo',
    version=info['__version__'],
    url='http://www.github.com/corranwebster/taupo',
    author='Corran Webster',
    description="Traits-based generic GUI library wrapper",
    install_requires=info['__requires__'],
    license='BSD',
    packages=['taupo'],
)
