# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" BaseFont Object

A Font specifies a font for displaying text.  This is an abstract definition,
and the actual font which is displayed will depend upon the capabilities of the
toolkit and the fonts available in the OS.

"""

from __future__ import absolute_import, division, print_function

from traits.api import ABCHasTraits, Enum, Int, Unicode, provides

from ..trait_types import Attribute
from ..interfaces.i_font import IFont

@provides(IFont)
class AbstractFont(ABCHasTraits):

    #: the font family to use, if available
    family = Attribute(Unicode('sanserif'))
    
    #: the size of the font, in points
    size = Attribute(Int(12))
    
    #: the style of the font to use, if possible
    style = Attribute(Enum("normal", "italic", "oblique"))
    
    #: the weight of the font to use, if possible
    weight = Attribute(Enum("normal", "light", "demibold", "bold", "black"))
