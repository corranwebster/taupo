# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from traits.api import Enum, Tuple

def Attribute(trait_type, *args, **kwargs):
    """ Factory for creating taupo-aware traits
    
    Traits created with the Attribute factory have listeners which automatically
    push changes to the underlying widget.  Each attribute should have a
    corresponding ``_update_<name>`` method defined which performs the
    toolkit-specific operations.
    
    """
    kwargs['taupo_attribute'] = True
    return trait_type(*args, **kwargs)


#: an trait which represents a horizontal alignment
HorizontalAlignment = Enum('left', 'center', 'right', 'justify')

#: a trait which represents a vertical alignment
VerticalAlignment = Enum('top', 'center', 'bottom')

#: a trait which represents a combined horizontal and vertical alignment
Alignment = Tuple(HorizontalAlignment, VerticalAlignment)

#: a trait describing how to echo text in a field
EchoMode = Enum('normal', 'password', 'no_echo')