# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from traits.api import Any, Enum, Int, Unicode, provides

from ..trait_types import Attribute
from .c_widget import CWidget
from ..interfaces.i_label import ILabel

@provides(ILabel)
class CLabel(CWidget):
    """ Base class for static label widgets """
    
    visible = True

    #: the text to display in the label
    text = Attribute(Unicode)

    #: the font to use for the label
    font = Attribute(Any) # XXX Instance(IFont)

    #: the horizontal alignment of the text in the label
    horizontal_alignment = Attribute(Enum('left', 'center', 'right', 'justify'))

    #: the vertical alignment of the text in the label
    vertical_alignment = Attribute(Enum('top', 'center', 'bottom'))

    #: amount to indent the text in the label
    indent = Attribute(Int)
