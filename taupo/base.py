# Taupo library code.
#
# Copyright 2014, Corran Webster.
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD license
# in the LICENSE file.

""" Basic module to support widget implementations

"""

from __future__ import absolute_import, division, print_function

from functools import wraps

_binding_hook_doc = """Safely update {name}"""

def protect(fn):
    """ Protects an update function against re-entrant updates """
    name = fn.func_name[8:]
    @wraps(fn)
    def protected_method(self, value):
        if name in self._updating:
            return
        print(name, self, value)
        return fn(self, value)
    return protected_method


