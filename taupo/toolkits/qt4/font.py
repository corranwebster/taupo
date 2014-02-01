# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Font Object

A Font specifies a font for displaying text.  This is an abstract definition,
and the actual font which is displayed will depend upon the capabilities of the
toolkit and the fonts available in the OS.

"""

from __future__ import absolute_import, division, print_function

from traits.api import Enum, Int, Interface, Unicode

from ...common.c_font import CFont

class Font(CFont):

    def get_toolkit_font(self):
        """ Return a toolkit font that matches as well as possible """
        raise NotImplementedError
