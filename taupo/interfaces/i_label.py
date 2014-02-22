# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Interface for Label Widgets

ILabel specifies the interface for all Label widgets provided by the Taupo
library.

"""
from __future__ import absolute_import, division, print_function

from traits.api import Any, Enum, Int, Unicode

from .i_widget import IWidget

class ILabel(IWidget):
    """ Interface for static text label widgets"""

    #: the text to display in the label
    text = Unicode
