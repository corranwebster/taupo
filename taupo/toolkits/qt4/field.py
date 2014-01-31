# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.


from .qt.QtGui import QLineEdit
from .qt.QtCore import Qt

from ...widgets.base_field import BaseField
from ...widgets.base import protect
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
echo_modes = {
    'normal': QLineEdit.Normal,
    'password': QLineEdit.Password,
    'no_echo': QLineEdit.NoEcho,
}

class Field(BaseField, Widget):

    def _create_control(self, parent):
        control = QLineEdit(parent)
        return control

    @protect
    def _update_text(self, text):
        self.control.setText(text)

    @protect
    def _update_cursor_position(self, cursor_position):
        self.control.setCursorPosition(cursor_position)

    @protect
    def _update_selected_range(self, selected_range):
        start, end = selected_range
        self.control.setSelection(start, end-start)

    @protect
    def _update_read_only(self, read_only):
        self.control.setReadOnly(read_only)

    @protect
    def _update_echo_mode(self, echo_mode):
        self.control.setEchoMode(echo_modes[echo_mode])

    @protect
    def _update_vertical_alignment(self, vertical_alignment):
        self._update_alignment()

    @protect
    def _update_horizontal_alignment(self, horizontal_alignment):
        self._update_alignment()

    def _update_alignment(self):
        vertical = vertical_alignments[self.vertical_alignment]
        horizontal = horizontal_alignments[self.horizontal_alignment]
        self.control.setAlignment(vertical | horizontal)

    def _bind_events(self):
        self.control.textEdited.connect(self._text_updated)
        self.control.cursorPositionChanged.connect(self._cursor_position_updated)
        self.control.selectionChanged.connect(self._selection_updated)
        self.control.editingFinished.connect(self._editing_finished_updated)
        self.control.returnPressed.connect(self._return_pressed_updated)
    
    def _text_updated(self, text):
        self._attribute_set(text=text)
    
    def _cursor_position_updated(self, cursor_position):
        self._attribute_set(cursor_position=cursor_position)
    
    def _selection_updated(self):
        text = self.control.selectedText()
        start = self.control.selectionStart()
        end = start + len(text)
        self._attribute_set(selected_text=text, selected_range=(start, end))
