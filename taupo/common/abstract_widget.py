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

from abc import abstractmethod

from traits.api import Any, Bool, HasTraits, Instance, Property, Set, Trait, provides

from ..trait_types import Attribute
from ..interfaces.i_widget import IWidget

from .abstract_object import AbstractObject

@provides(IWidget)
class AbstractWidget(AbstractObject):
    """ Base class for GUI Widget Proxies """
    
    # ------------------------------------------------------------------------
    # 'IWidget' interface
    # ------------------------------------------------------------------------

    #: the parent IWidget object, or None
    parent = Instance(IWidget)

    #: whether or not the widget is visible
    visible = Attribute(Bool(False))

    #: whether or not the widget is enabled for use interaction
    enabled = Attribute(Bool(True))
    
    def reparented(self):
        """ Handle reparenting a Widget """
        if self.object is not None:
            self._update_parent(self._parent_object)

    # ------------------------------------------------------------------------
    # 'CWidget' interface
    # ------------------------------------------------------------------------

    @abstractmethod
    def _create_control(self, parent):
        raise NotImplementedError

    @abstractmethod
    def _update_parent(self, parent):
        raise NotImplementedError
    
    # Taupo Attribute handlers

    @abstractmethod
    def _update_visible(self, visible):
        raise NotImplementedError

    @abstractmethod
    def _update_enabled(self, enabled):
        raise NotImplementedError
    
    # ------------------------------------------------------------------------
    # 'CObject' interface
    # ------------------------------------------------------------------------

    def _create_object(self):
        return self._create_control(self._parent_object)

    # ------------------------------------------------------------------------
    # Private interface
    # ------------------------------------------------------------------------

    #: utility trait providing the parent's object, or None
    _parent_object = Property(Any)
    def _get__parent_object(self):
        if self.parent is not None:
            if self.parent.object is None:
                self.parent.create()
            return self.parent.object
        return None
