# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Button Widget

The IButton interface is the base class for all user interface widgets
provided by the Taupo library.

"""

from __future__ import absolute_import, division, print_function

from traits.api import Any, Enum, Event, Unicode

from .i_widget import IWidget


class IButton(IWidget):
    
    #: the text to display in the label
    text = Unicode

    #: the font to use for the label
    font = Any # XXX Instance(IFont)
    
    #: the horizontal alignment of the text in the label
    horizontal_alignment = Enum('left', 'center', 'right', 'justify')

    #: the vertical alignment of the text in the label
    vertical_alignment = Enum('top', 'center', 'bottom')

    #: event when the button is pressed down
    pressed = Event

    #: event when the button is released
    released = Event

