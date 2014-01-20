# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Base interface for GUI Widget Proxies

The IWidget interface is the base class for all user interface widgets
provided by the Taupo library.

"""

from __future__ import absolute_import, division, print_function

from traits.api import Any, Bool, Interface, Instance

class IWidget(Interface):
    """ Base interface for GUI Widget Proxies """

    #: the underlying toolkit widget object
    control = Any

    #: the parent IWidget object, or None
    parent = Instance('IWidget')

    #: whether or not the widget is visible
    visible = Bool

    #: whether or not the widget is enabled for use interaction
    enabled = Bool

    def create(self):
        """ Create the underlying toolkit widget and connect Traits """

    def destroy(self):
        """ Destroy the underlying toolkit widget and disconnect Traits """
