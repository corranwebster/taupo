# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.


from .qt.QtGui import QLabel
from .qt.QtCore import Qt

from ...widgets.base_label import BaseLabel
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

class Label(BaseLabel, Widget):

    def _create_control(self, parent):
        control = QLabel(parent)
        return control

    def _update_text(self, text):
        self.control.setText(text)

    def _update_alignment(self):
        vertical = vertical_alignments[self.vertical_alignment]
        horizontal = horizontal_alignments[self.horizontal_alignment]
        self.control.setAlignment(vertical | horizontal)