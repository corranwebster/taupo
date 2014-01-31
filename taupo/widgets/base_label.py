# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from traits.api import Any, Bool, HasTraits, Instance, Property, provides

from .base_widget import BaseWidget
from .i_label import ILabel

@provides(ILabel)
class BaseLabel(BaseWidget):
    """ Base class for static label widgets """
    
    visible = True

    def _initialize_control(self):
        self._update_text(self.text)
        self._update_alignment()
        super(BaseLabel, self)._initialize_control()

    def _connect_listeners(self, remove=False):
        super(BaseLabel, self)._connect_listeners(remove)
        self.on_trait_change(self._update_text, 'text', remove=remove)
        self.on_trait_change(self._update_alignment, 'vertical_alignment', remove=remove)
        self.on_trait_change(self._update_alignment, 'horizontal_alignment', remove=remove)
