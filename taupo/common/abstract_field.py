# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from abc import abstractmethod

from traits.api import Any, Bool, Event, Int, Tuple, Unicode, provides

from ..trait_types import (Attribute, EchoMode)
from ..interfaces.i_field import IField

from .abstract_widget import AbstractWidget

@provides(IField)
class AbstractField(AbstractWidget):
    """ Base class for editable text field widgets """
    
    visible = True

    #: the text displayed in the field
    text = Attribute(Unicode)
    
    #: the text which is currently selected (read-only)
    selected_text = Unicode
    
    #: the range of text which is currently selected
    selected_range = Attribute(Tuple(Int, Int))
    
    #: whether the field is read-only or not
    read_only = Attribute(Bool)
    
    #: whether and how the obscures entered text
    echo_mode = Attribute(EchoMode)

    #: the user has pressed the Return or Enter key
    return_pressed = Event

    #: the user has finished editing the field
    editing_finished = Event

    @abstractmethod
    def insert(self, text):
        raise NotImplementedError