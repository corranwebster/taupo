# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Object

This module provides the base implementation of the Qt-specific object proxy
functionality.  Note that an Object may be proxying something which is not a
QObject.

"""

from __future__ import absolute_import, division, print_function

from ...common.abstract_object import AbstractObject

class Object(AbstractObject):
    """ Qt object proxy base class """

    def _destroy_object(self):
        """ Destroy the underlying toolkit object and disconnect Traits """
        self.object.deleteLater()
        self.object = None

    def _bind_events(self):
        super(Object, self)._bind_events()
