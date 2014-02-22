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

from traits.api import Bool, Enum, Event, Int, Tuple, Unicode

from .i_widget import IWidget

class IField(IWidget):
    """ Interface for editable text field widgets"""

    #: the text to display in the field
    text = Unicode
    
    #: the text which is currently selected
    selected_text = Unicode
    
    #: the range of text which is currently selected
    selected_range = Tuple(Int, Int)
    
    #: whether the field is read-only or not
    read_only = Bool
    
    #: whether and how the obscures entered text
    echo_mode = Enum('normal', 'password', 'no_echo')

    #: the user has pressed the Return or Enter key
    return_pressed = Event

    #: the user has finished editing the field
    editing_finished = Event

    def insert(self, text):
        """ Delete the current selection and insert text in its place """