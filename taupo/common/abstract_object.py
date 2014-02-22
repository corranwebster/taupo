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

from traits.api import ABCHasTraits, Any, Bool, Instance, Property, Set, Trait, provides

from ..trait_types import Attribute
from ..interfaces.i_object import IObject

@provides(IObject)
class AbstractObject(ABCHasTraits):
    """ Abstract base class for toolkit object proxies """
    
    # ------------------------------------------------------------------------
    # 'IObject' interface
    # ------------------------------------------------------------------------

    #: the underlying toolkit object
    object = Any
    
    def create(self):
        """ Create the underlying toolkit widget and connect Traits """
        if self.object is None:
            self.object = self._create_object()
            self._initialize_object()
            self._wrap_object()

    def destroy(self):
        """ Destroy the underlying toolkit widget and disconnect Traits """
        if self.object is not None:
            self._connect_listeners(remove=True)
            self._destroy_object()

    # ------------------------------------------------------------------------
    # 'CObject' interface
    # ------------------------------------------------------------------------

    @abstractmethod
    def _create_object(self):
        raise NotImplementedError

    @abstractmethod
    def _destroy_object(self):
        raise NotImplementedError
    
    @abstractmethod
    def _bind_events(self):
        pass

    # ------------------------------------------------------------------------
    # Private interface
    # ------------------------------------------------------------------------

    #: tracks attributes which are being updated to avoid loopback
    _updating = Set

    def _initialize_object(self):
        for name in self.traits(taupo_attribute=True):
            method = getattr(self, '_update_'+name)
            method(getattr(self, name))
    
    def _wrap_object(self):
            self._connect_listeners()
            self._bind_events()

    def _connect_listeners(self, remove=False):
        self.on_trait_change(self._update_parent, 'parent', remove=remove)
        for name in self.traits(taupo_attribute=True):
            method = getattr(self, '_update_'+name)
            self.on_trait_change(method, name, remove=remove)

    def _attribute_set(self, **kwargs):
        actual_updates = set(kwargs) - self._updating
        self._updating |= actual_updates
        try:
            for name in actual_updates:
                setattr(self, name, kwargs[name])
        finally:
            self._updating -= actual_updates
