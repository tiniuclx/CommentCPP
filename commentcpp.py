r"""Makes & adds unhelpful comments to C++ files.
Created on 11 Mar 2017

@author: Alexandru Valentin Tiniuc
"""
import argparse
import re
import tracery
from tracery.modifiers import base_english
import dictionaries


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



parser = argparse.ArgumentParser()
parser.add_argument('path', help='file to add comments to')
parser.add_argument('-ow','--overwrite',action='store_true', help='overwrite the input file')
parser.add_argument('-d','--destination', help='destination of output file')
args = parser.parse_args()
file = open(args.path)
contents = file.read()
file.close()


# Single-line comment regular expression
sl_regex = re.compile(r'//(.*)')
# List of single line comment matches
sl_coms = sl_regex.finditer(contents)
# Multi-line comment regular expression
# 16 is DOTALL regex flag
ml_regex = re.compile(r'/\*(.*?)\*/', 16)
# List of multi line comment matches
ml_coms = ml_regex.finditer(contents)

# added a comment somewhere else

# idea: to keep indentation consistent between code and inserted comment:
# make regex that searches for start of line, followed by 0 or more whitespace
# followed by non-whitespace character
# can also be done by keeping track of line number and line location

# other idea: write a c++ parser (or, to reduce the scope, a c parser) as outlined in
# CraftingInterpreters.com
# using this parser, add contextually-sensitive comments (i.e. referring to specific
# variables in the source file) to make everything extra-confusing!

# change 1: hello melissa

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
