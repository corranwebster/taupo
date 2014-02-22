# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Interface for Slider Widgets

ISlider specifies the interface for all Slider widgets provided by the Taupo
library.

"""
from __future__ import absolute_import, division, print_function

from traits.api import Int

from .i_widget import IWidget

class ISlider(IWidget):
    """ Interface for sliders, dials and similar widgets """
    
    #: the current value of the slider
    value = Int

    #: the maximum value
    maximum = Int

    #: the minimum value
    minimum = Int
