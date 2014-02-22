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
    
    #: the text to display in the button
    text = Unicode
    
    #: the icon to display in the button
    icon = Unicode

    #: event when the button is clicked (occurs on mouse up)
    clicked = Event

