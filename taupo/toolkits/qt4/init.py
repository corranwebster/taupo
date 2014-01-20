# Taupo library code.
#
# Copyright (C) 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.
"""
Init Module
-----------

This module provides initialzation code for the Taupo `qt4` backend.

"""

from __future__ import absolute_import

import sys

def initialize():
    """ Initialize the Qt4 Taupo backend

    In particular this ensures that a QApplication exists.  If one does not
    exist, it will be passed `sys.argv`.  If you need more control over the
    creation of the QApplication, use `.support.get_app` before importing any
    other toolkit objects.

    """
    from .support import get_app
    get_app(sys.argv)
