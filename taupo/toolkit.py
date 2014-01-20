# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.
"""
Toolkit Module
--------------

This module provides code that attempts to initialize a backend and makes
available a function :py:func:`toolkit_object` that imports an object from the
appropriate backend.

"""

from __future__ import absolute_import, division, print_function

# Standard library imports
import warnings
import importlib

# Enthought library imports.
from traits.etsconfig.api import ETSConfig

_toolkit_package = None
_known_toolkits = ('qt4', 'null')

def _initialize_toolkit(toolkit):
    """ Attempt to import the :py:mod:`init` module of a toolkit """
    _toolkit_package = __name__+'s.'+toolkit
    module = importlib.import_module(_toolkit_package+'.init')
    initialize = getattr(module, 'initialize')
    initialize()
    return _toolkit_package

if ETSConfig.toolkit:
    _toolkit_package = _initialize_toolkit(ETSConfig.toolkit)
else:
    # try each of these in order
    for toolkit in _known_toolkits:
        try:
            _toolkit_package = _initialize_toolkit(toolkit)
        except ImportError:
            import traceback
            tb = traceback.format_exc().strip().replae('\n', '\n    ')
            warnings.warn(('Unable to import the "%s" backend ' +
                           'for taupo due to traceback: %s\n') % (toolkit, tb))
        else:
            ETSConfig.toolkit = toolkit
            break
    else:
        raise ImportError(("Unable to import a taupo backend for any of the" +
                           "known backends (%s)") % ', '.join(_known_toolkits))


def toolkit_object(name):
    """ Return the toolkit-specific version of a class

    Parameters
    ----------

    name :
        A string of the form "module_path:object".  The module_path is a
        path relative to the appropriate toolkit module.

    Returns
    -------

    toolkit_object :
        The requested toolkit object.

    Raises
    ------

    ImportError :
        If the appropriate module cannot be imported.

    AttributeError :
        If the object cannot be found in the imported module.

    Example
    -------

    ::
        PushButton = toolkit_object("push_button:PushButton")

    """
    # XXX for the time being, do no error-checking
    module_name, object_name = name.split(':')
    module = importlib.import_module(_toolkit_package+'.'+module_name)
    toolkit_object = getattr(module, object_name)
    return toolkit_object

all = ['toolkit_object']
