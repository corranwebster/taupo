# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from ...common.c_widget import CWidget
from ...base import protect

from .qt.QtGui import QWidget
from .object import Object

class Widget(CWidget, Object):
    
    def _create_control(self, parent):
        return QWidget(parent)

    def _destroy_control(self):
        """ Destroy the underlying toolkit widget and disconnect Traits """
        self.object.hide()
        super(Widget.self)._destroy_control()

    def _update_parent(self, parent):
        self.object.setParent(parent)

    def _update_visible(self, visible):
        self.object.setVisible(visible)

    @protect
    def _update_enabled(self, enabled):
        self.object.setEnabled(enabled)
