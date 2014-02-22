# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.


from .qt.QtGui import QLabel
from .qt.QtCore import Qt

from ...common.c_label import CLabel
from .widget import Widget

horizontal_alignments = {
    'left': Qt.AlignLeft,
    'center': Qt.AlignCenter,
    'right': Qt.AlignRight,
    'justify': Qt.AlignJustify,
}
vertical_alignments = {
    'top': Qt.AlignTop,
    'center': Qt.AlignCenter,
    'bottom': Qt.AlignBottom,
}

class Label(CLabel, Widget):

    def _create_control(self, parent):
        control = QLabel(parent)
        return control

    def _update_text(self, text):
        self.control.setText(text)
