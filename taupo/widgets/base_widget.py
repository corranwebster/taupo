# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Base Class for GUI Widget Proxies

The BaseWidget class is the base class for all user interface widgets
provided by the Taupo library.  It provides a stubbed out implementation of
the IWidget interface that toolkits can subclass from.

"""

from __future__ import absolute_import, division, print_function

from traits.api import Any, Bool, HasTraits, Instance, Property, provides

from .i_widget import IWidget

@provides(IWidget)
class BaseWidget(HasTraits):
    """ Base class for GUI Widget Proxies """

    #: the underlying toolkit widget object
    control = Any

    #: the parent IWidget object, or None
    parent = Instance(IWidget)

    #: whether or not the widget is visible
    visible = Bool

    #: whether or not the widget is enabled for use interaction
    enabled = Bool

    #: the parent's control, or None
    _parent_control = Property(Any)
    def _get__parent_control(self):
        if self.parent is not None:
            return self.parent.control
        return None

    def create(self):
        """ Create the underlying toolkit widget and connect Traits """
        if self.control is None:
            self.control = self._create_control(self._parent_control)
            self._initialize_control()
            self._bind_events()
            self._connect_listeners()

    def reparented(self):
        if self.control is not None:
            self._reparent_control(self._parent_control)

    def destroy(self):
        """ Destroy the underlying toolkit widget and disconnect Traits """
        if self.control is not None:
            self._connect_listeners(remove=True)
            self._destroy_control()

    def _create_control(self, parent):
        raise NotImplementedError

    def _initialize_control(self):
        self._update_enabled(self.enabled)
        self._update_visible(self.visible)

    def _bind_events(self):
        raise NotImplementedError

    def _connect_listeners(self, remove=False):
        self.on_trait_change(self._update_parent, 'parent', remove=remove)
        self.on_trait_change(self._update_visible, 'visible', remove=remove)
        self.on_trait_change(self._update_enabled, 'enabled', remove=remove)

    def _destroy_control(self):
        raise NotImplementedError

    def _update_parent(self, parent):
        raise NotImplementedError

    def _update_visible(self, visible):
        raise NotImplementedError

    def _update_enabled(self, enabled):
        raise NotImplementedError
