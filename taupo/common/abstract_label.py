# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from traits.api import Unicode, provides

from ..trait_types import Attribute
from ..interfaces.i_label import ILabel

from .abstract_widget import AbstractWidget

@provides(ILabel)
class AbstractLabel(AbstractWidget):
    """ Base class for static label widgets """
    
    visible = True

    #: the text to display in the label
    text = Attribute(Unicode)
