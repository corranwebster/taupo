# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import, division, print_function

from taupo.widget import Widget
from taupo.field import Field
from taupo.toolkits.qt4.support import start_event_loop

def listener(obj, name, old, new):
    print('updated:', old, '->', new)
        

def main():
    w = Widget()
    w.create()
    l = Field(
        parent=w,
        text="Hello World",
        horizontal_alignment='center',
        vertical_alignment='center',
        echo_mode='password',
    )
    l.on_trait_change(listener, 'selected_range')
    l.create()
    w.visible = True
    l.text = 'Foo'
    l.selected_range = (2, 2)
    start_event_loop()

if __name__ == '__main__':
    main()
    

