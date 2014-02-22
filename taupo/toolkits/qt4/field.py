# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.


from .qt.QtGui import QLineEdit
from .qt.QtCore import Qt

from ...common.c_field import CField
from ...base import protect
from .widget import Widget

echo_modes = {
    'normal': QLineEdit.Normal,
    'password': QLineEdit.Password,
    'no_echo': QLineEdit.NoEcho,
}

class Field(CField, Widget):
    
    def insert(self, text):
        self.object.insert(text)

    def _create_control(self, parent):
        object = QLineEdit(parent)
        return object

    @protect
    def _update_text(self, text):
        self.object.setText(text)

    @protect
    def _update_selected_range(self, selected_range):
        start, end = selected_range
        self.object.setSelection(start, end-start)

    @protect
    def _update_read_only(self, read_only):
        self.object.setReadOnly(read_only)

    @protect
    def _update_echo_mode(self, echo_mode):
        self.object.setEchoMode(echo_modes[echo_mode])

    def _bind_events(self):
        self.object.textEdited.connect(self._text_updated)
        self.object.selectionChanged.connect(self._selection_updated)
    
    def _text_updated(self, text):
        self._attribute_set(text=text)
    
    def _selection_updated(self):
        text = self.object.selectedText()
        start = self.object.selectionStart()
        end = start + len(text)
        self._attribute_set(selected_text=text, selected_range=(start, end))
