# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from traits.api import Any, Bool, Enum, Event, Int, Tuple, Unicode, provides

from .trait_types import Attribute, Alignment, EchoMode
from .base_widget import BaseWidget
from .i_field import IField

@provides(IField)
class BaseField(BaseWidget):
    """ Base class for editable text field widgets """
    
    visible = True

    #: the text displayed in the field
    text = Attribute(Unicode)

    #: the location of the cursor in the field
    cursor_position = Attribute(Int)
    
    #: the text which is currently selected (read-only)
    selected_text = Attribute(Unicode)
    
    #: the range of text which is currently selected
    selected_range = Attribute(Tuple(Int, Int))
    
    #: whether the field is read-only or not
    read_only = Attribute(Bool)
    
    #: whether and how the obscures entered text
    echo_mode = Attribute(EchoMode)

    #: the font to use for the field
    font = Attribute(Any) # XXX Instance(IFont)

    #: the alignment of the text in the field
    alignment = Attribute(Alignment)

    #: the alignment of the text in the field
    horizontal_alignment = Attribute(HorizontalAlignment)

    #: the alignment of the text in the field
    vertical_alignment = Attribute(VerticalAlignment)

    #: the user has pressed the Return or Enter key
    return_pressed = Event

    #: the user has finished editing the field
    editing_finished = Event
        