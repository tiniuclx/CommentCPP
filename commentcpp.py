r"""Makes & adds unhelpful comments to C++ files.
Created on 11 Mar 2017

@author: Alexandru Valentin Tiniuc
"""
import argparse
import re
import tracery
from tracery.modifiers import base_english

rules = {
    # The comments are generated by expanding the tree by starting from
    # origin and going through every #expansion_term# recursively.
    # A single branch of this tree can be printed as output.
    'origin': ['The #object# is #act.ed# by the #object_attr#.',
               '#act.s.capitalize# the #object_attr#',
               '#act.ed#', '#object_attr#', '#act.s#',
               '#act.ed.capitalize# from #object_attr# #location#',
               'Crashes when compiled with #compiler#',
               'TODO: #problem# with #compiler#',
               'fix for #problem# #location#',
               'FIXME: #problem#',
               'Explained #location#',
               '#act.s.capitalize# the #object#. Fix for #problem#' +
               ' due to #object_attr#',
               '#object_attr.capitalize# #act.s#; see #location#',
               '#object_attr# is actually #trait#, check #location#',
               'Adding this #object_attr# caused #problem#',
               'Removing this #object# causes #problem#',
               '#trait#, yet #trait#',
               '#object.capitalize# is #trait#. Maybe consider #act#ing?',
               'if #problem#: try #solution#',
               '#solution.capitalize# works, no idea why',
               'Why?',
           ],
    'object': ['function', 'argument', 'parameter', 'class', 'instance',
               'constructor', 'destructor', 'variable', 'factory',
               'friend function', 'template', 'memory', 'array', 'list', 'tree',
               'vector', 'horrible hack', 'thing', 'stuff', 'thread',
               'feature', 'bug', 'type', 'bugfix', 'fix #location#',
               'bug #location#', 'parent', 'child', 'ancestor', 'descendant',
               'carrot','typecast'],
    'trait': ['polymorphic', 'virtual', 'inline', 'member', 'binary',
              'hashed', 'obfuscated', 'encrypted', 'simple', 'multi-threaded',
              'robust', 'thread-safe', 'immutable', 'argument','x86','x64',
              'cryptographic', 'memory-safe', 'null', 'orange'],
    'object_attr': ['#object#', '#trait# #object#', '#trait# #trait# #object#', '#object#'],
    'act': ['overload', 'inherit', 'parse', 'modify', 'reference',
            'return', 'generate', 'auto-generate', 'point', 'store', 'fix',
            'patch', 'hack', 'overflow', 'crash', 'delete', 'quit',
            'free', 'deallocate', 'refactor', 'typecast'],
    'location': ['in header', 'in declaration', 'in definition',
                 'in library', 'above', 'below', 'in another file',
                 'in #compiler# source', 'in standard template library',
                 'in assembly bytecode', 'in sample from The C Programming Language',
                 'in code mentioned in The C++ Programming Language', 'in test server',
                 'in production', 'in class interface', 'in the documentation',
                 'in the #object# #object#', 'in the #trait# code #location#',
                 'in the #object_attr#'
                 ],
    'problem': ['crash', 'typo', 'side effect', 'unintended consequence',
                'overflow', 'stack overflow', 'memory leak', 'threading issue',
                'data race', 'deadlock', 'synchronisation error', 'a load of shit',
                'code smell', 'bluescreen, #solution# doesn\'t work',
                'issues because whoever wrote this was drunk','it\'s broken, help'],
    'solution': ['rebooting', 'restarting', 'turning it off and on again',
                 'compiling with #compiler#', 'fixing #problem# #location#',
                 'reinstancing the #object_attr#'],
    'compiler': ['gcc', 'g++', 'Apple C++', 'Cygwin', 'IBM C++',
                 'Microsoft Visual C++ Express', 'Oracle C++',
                 'my homebrew C++ interpreter', 'CPython', 'Visual C\\#', 'javac',
                 'AVR GCC optimised for #object_attr.s#', 'clang'],
    }


def gen_sl_comment(match):
    """Procedurally generates a single-line comment, different for every call.
    """
    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    return "// " + grammar.flatten('#origin#')


def gen_ml_comment(match):
    """Procedurally generates a multi-line comment, different for every call.
    """
    # TODO: Implement this
    return '/* Placeholder multi \n   line comment \n */'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='file to add comments to')
    parser.add_argument('-ow','--overwrite',action='store_true', help='overwrite the input file')
    parser.add_argument('-d','--destination', help='destination of output file')
    args = parser.parse_args()
    file = open(args.path)
    contents = file.read()
    file.close()
else:
    contents = r'//Placeholder'

# Single-line comment regular expression
sl_regex = re.compile(r'//(.*)')
# List of single line comment matches
sl_coms = sl_regex.finditer(contents)
# Multi-line comment regular expression
# 16 is DOTALL regex flag
ml_regex = re.compile(r'/\*(.*?)\*/', 16)
# List of multi line comment matches
ml_coms = ml_regex.finditer(contents)

# idea: to keep indentation consistent between code and inserted comment:
# make regex that searches for start of line, followed by 0 or more whitespace
# followed by non-whitespace character

output = ml_regex.sub(gen_ml_comment, contents)
output = sl_regex.sub(gen_sl_comment, output)

# repeated code, consider refactoring?
if args.overwrite:
    with open(args.path, 'w') as f:
        f.write(output)
        f.close()
elif args.destination:
    # does not work with folders
    # e.g. -d tests_folder/output2.cpp gives file not found error
     with open(args.destination, 'w') as f:
        f.write(output)
        f.close()
else:
     with open('output.cpp', 'w') as f:
        f.write(output)
        f.close()
