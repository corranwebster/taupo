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

from traits.api import Any, Bool, Enum, Event, Unicode

from .i_widget import IWidget

class IField(IWidget):
    """ Interface for editable text field widgets"""

    #: the text to display in the field
    text = Unicode
    
    #: the text which is currently selected
    selected_text = Unicode
    
    #: the range of text which is currently selected
    selected_range = Unicode
    
    #: whether the field is read-only or not
    read_only = Bool
    
    #: whether and how the obscures entered text
    echo_mode = Enum('normal', 'password', 'no_echo')

    #: the font to use for the field
    font = Any # XXX Instance(IFont)

    #: the horizontal alignment of the text in the field
    horizontal_alignment = Enum('left', 'center', 'right', 'justify')

    #: the vertical alignment of the text in the field
    vertical_alignment = Enum('top', 'center', 'bottom')

    #: the user has pressed the Return or Enter key
    return_pressed = Event

    #: the user has finished editing the field
    editing_finished = Event

