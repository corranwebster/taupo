# Taupo library code.
#
# Copyright (C) 2014, Corran Webster.
# Copyright (C) 2008-2010, The IPython Development Team
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

from __future__ import absolute_import

""" Utility methods

"""

# these methods are based on code from IPython's guisupport utility module

def get_app(*args, **kwargs):
    """Create a new qt4 app or return an existing one."""
    from .qt import QtGui
    app = QtGui.QApplication.instance()
    if app is None:
        if not args:
            args = ([''],)
        app = QtGui.QApplication(*args, **kwargs)
    return app

def is_event_loop_running(app=None):
    """Is the qt4 event loop running."""
    if app is None:
        app = get_app([''])
    if hasattr(app, '_in_event_loop'):
        return app._in_event_loop
    else:
        # Does qt4 provide a other way to detect this?
        return False

def start_event_loop(app=None):
    """Start the qt4 event loop in a consistent manner."""
    if app is None:
        app = get_app([''])
    if not is_event_loop_running(app):
        app._in_event_loop = True
        app.exec_()
        app._in_event_loop = False
    else:
        app._in_event_loop = True
