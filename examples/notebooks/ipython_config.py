# Configuration file for ipython-notebook.

c = get_config()

# XXX FROM THE HOWTO ON IPYTHON'S HOMEPAGE
# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always
# Notebook config
c.NotebookApp.open_browser = False

# XXX MODIFIED SYMPY CONFIG
app = c.InteractiveShellApp
lines = """
from __future__ import division
from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
"""
if hasattr(app, 'exec_lines'):
    app.exec_lines.append(lines)
else:
    app.exec_lines = [lines]
# Load the sympy_printing extension to enable nice printing of sympy expr's.
if hasattr(app, 'extensions'):
    app.extensions.append('sympyprinting')
else:
    app.extensions = ['sympyprinting']
app.pylab_import_all = False
