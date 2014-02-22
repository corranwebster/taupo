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
from .qt.QtGui import QFont

class Font(CFont):

    def _create_object(self, parent):
        object = QFont()
        return object

    def _bind_events(self):
        pass

    def _destroy_object(self):
        raise NotImplementedError
