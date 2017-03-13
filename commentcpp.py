r"""Makes & adds unhelpful comments to C++ files.
Created on 11 Mar 2017

@author: Alexandru Valentin Tiniuc
"""
import argparse
import re
import tracery


def gen_sl_comment():
    """Procedurally generates a single-line comment, different for every call.
    """
    # TODO: Implement this
    string = r'// Placeholder single-line comment'
    return string


def gen_ml_comment():
    """Procedurally generates a multi-line comment, different for every call.
    """
    # TODO: Implement this
    return r'/* Placeholder multi \n   line comment \n */'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='File to add comments to')
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
ml_regex = re.compile(r'/\*(.*?)\*/', re.RegexFlag.DOTALL)
# List of multi line comment matches
ml_coms = ml_regex.finditer(contents)

# idea: to keep indentation consistent between code and inserted comment:
# make regex that searches for start of line, followed by 0 or more whitespace
# followed by non-whitespace character

# for line in sl_coms:
#     print(line.group())
# for comment in ml_coms:
#     print(comment.group(1))
# group() returns the whole match, group(1) returns only the comments

output = ml_regex.sub(gen_ml_comment(), contents)
output = sl_regex.sub(gen_sl_comment(), output)
print(output)