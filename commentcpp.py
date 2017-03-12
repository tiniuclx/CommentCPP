r"""Adds unhelpful comments to C++ files.
Created on 11 Mar 2017

@author: Alexandru Valentin Tiniuc
"""
import argparse
import re
import tracery
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

# for line in sl_coms:
#     print(line.group())
# for comment in ml_coms:
#     print(comment.group(1))
# group() returns the whole match, group(1) returns only the comments

output = ml_regex.sub(r'/* Placeholder \n   multiline \n   comment \n */', contents)
output = sl_regex.sub(r'//placeholder single-line comment', output)
print(output)

print('hello')