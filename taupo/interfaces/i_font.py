# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" IFont Object

A Font specifies a font for displaying text.  This is an abstract definition,
and the actual font which is displayed will depend upon the capabilities of the
toolkit and the fonts available in the OS.

"""

from __future__ import absolute_import, division, print_function

from traits.api import Enum, Event, Int, Unicode

from .i_object import IObject

class IFont(IObject):

    #: the font family to use, if available
    family = Unicode('sanserif')
    
    #: the size of the font, in points
    size = Int
    
    #: the style of the font to use, if possible
    style = Enum("normal", "italic", "oblique")
    
    #: the weight of the font to use, if possible
    weight = Enum("normal", "light", "demibold", "bold", "black")
