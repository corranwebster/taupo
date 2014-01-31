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

    #: the font to use for the label
    font = Any # XXX Instance(IFont)

    #: the horizontal alignment of the text in the label
    horizontal_alignment = Enum('left', 'center', 'right', 'justify')

    #: the vertical alignment of the text in the label
    vertical_alignment = Enum('top', 'center', 'bottom')

    #: amount to indent the text in the label
    indent = Int
