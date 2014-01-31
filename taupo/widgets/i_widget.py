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

As a guiding design principle, the IWidget implementation is completely
responsible for controlling the underlying toolkit widget, and only needs to
respond do changes in the widget's state driven by the user or OS, not from
other code which may attempt to manipulate the widget state directly.  If
something causes the state of the toolkit widget to diverge from the state
held by the IWidget implementation, then that is a bug, and the IWidget
implementation should be considered to hold the true state of the values
in question.

If there is some state which is ephemeral (for example, whether or not a
given widget has focus) it should be represented by methods on the class
rather than an attribute holding state (ie. `has_focus()` and `get_focus()` vs.
`has_focus = Bool`).  A test which may help developers distinguish these sort
of state values from more typical state is whether or not it would make sense
for these values to be serialized or be part of a template for the widget.

The other design principle is that the IWidget interface represents only the
state required to represent the operation of the widget.  There may be
additional state on the underlying control, but if it is not relevant, it
should not be exposed.  If there is some question about whether the state is
needed, a mixin or auxilliary class may be an appropriate way to let a developer
access these features.

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
    visible = Bool(True)

    #: whether or not the widget is enabled for use interaction
    enabled = Bool(True)

    def create(self):
        """ Create the underlying toolkit widget and connect Traits """

    def reparented(self):
        """ Handle reparenting a Widget """

    def destroy(self):
        """ Destroy the underlying toolkit widget and disconnect Traits """

    def focus(self):
        """ Make this widget have the focus, if possible """
        