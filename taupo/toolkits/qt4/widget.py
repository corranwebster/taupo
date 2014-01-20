# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.


from ...widgets.base_widget import BaseWidget
from .qt.QtGui import QWidget

class Widget(BaseWidget):

    def _create_control(self, parent):
        return QWidget(parent)

    def _bind_events(self):
        pass

    def _destroy_control(self):
        """ Destroy the underlying toolkit widget and disconnect Traits """
        self.control.hide()
        self.control.deleteLater()
        self.control = None

    def _update_parent(self, parent):
        self.control.setParent(parent)

    def _update_visible(self, visible):
        self.control.setVisible(visible)

    def _update_enabled(self, enabled):
        self.control.setEnabled(enabled)
