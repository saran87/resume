#!/usr/bin/python

"""
Takes yaml resume input source, escapes it, and feeds it to the Cheetah
templating engine
"""

from Cheetah.Template import Template
from datetime import datetime
import sys
import yaml
import escape
import functools

# TODO: rename template.txt to template.txt.tmpl
# TODO: better directory structure

def escape_leaves(escape_func, contents):
    """Escapes all leaves in the contents dict with escape_func"""
    if isinstance(contents, list):
        return map(functools.partial(escape_leaves, escape_func), contents)
    elif isinstance(contents, dict):
        return dict(map(lambda x: (x[0], escape_leaves(escape_func, x[1])), contents.items()))
    else:
        return escape_func(str(contents))

if __name__ == '__main__':
    extension = sys.argv[1]

    # TODO: cmd line argument
    contents = yaml.load(open('resume.yaml', 'r').read())

    escape_func = getattr(escape, 'escape_' + extension, lambda x: x)
    escaped_contents = escape_all(escape_func, contents)
    template = Template(file='template.' + extension, searchList=[escaped_contents])

    open('resume.' + extension, 'w').write(str(template))
