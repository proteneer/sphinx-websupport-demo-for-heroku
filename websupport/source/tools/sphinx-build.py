# -*- coding: utf-8 -*-
"""
    Sphinx - Python documentation toolchain
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: 2007 by Georg Brandl.
    :license: Python license.
"""

import os
import sys

_sphinx_path = os.path.dirname(os.path.abspath(__file__)) + '/sphinx'
if os.path.isdir(_sphinx_path):
    sys.path.insert(0, _sphinx_path)

if __name__ == '__main__':

    if sys.version_info[:3] < (2, 4, 0):
        print >>sys.stderr, """\
Error: Sphinx needs to be executed with Python 2.4 or newer
(If you run this from the Makefile, you can set the PYTHON variable
to the path of an alternative interpreter executable, e.g.,
``make html PYTHON=python2.5``).
"""
        sys.exit(1)

    from sphinx import main
    sys.exit(main(sys.argv))
