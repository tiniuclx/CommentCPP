r"""Makes & adds unhelpful comments to C++ files.
Created on 11 Mar 2017

@author: Alexandru Valentin Tiniuc
"""
import argparse
import re
import tracery
from tracery.modifiers import base_english
import dictionaries


class Commenter:
    """Comments your code according to the rules given."""
    def __init__(self):
        self.grammar = tracery.Grammar(dictionaries.std_CPP)
        self.grammar.add_modifiers(base_english)
        self.source_code = "Uninitialised source in instance of Commenter"
        # Token for single line comments
        self.sl_token = r'//'
        # Tokens for multi-line comment regexp
        self.ml_token_start_regex = r'/\*'
        self.ml_token_end_regex = r'\*/'
        # Token for multi-line comment used for textual replacement
        # Two different comment tokens are needed because the regex
        # is different from the actual comment syntax
        #
        # Edge case: what happens in languages with only one comment style?
        # e.g. Python does not have multi-line comments
        self.ml_token_start = r'/*'
        self.ml_token_end = r'*/'
        # Single-line comment regular expression
        self.sl_regex = re.compile(self.sl_token + r'(.*)')
        # Multi-line comment regular expression
        # 16 is DOTALL regex flag
        self.ml_regex = re.compile(self.ml_token_start_regex + r'(.*?)'
                                   + self.ml_token_end_regex, 16)

    def set_source(self, input_code):
        self.source_code = input_code

    def get_source(self):
        return self.source_code

    def gen_sl_comment(self, match):  # match argument yet unused
        """Procedurally generates a single-line comment, different for every call.
        """
        return self.sl_token + " " + self.grammar.flatten('#origin#')

    def gen_ml_comment(self, match):  # match argument yet unused
        """Procedurally generates a multi-line comment, different for every call.
        """
        # TODO: Implement this
        return (self.ml_token_start + ' Placeholder multi \n   line comment \n '
                + self.ml_token_end)

    def comment(self):
        self.source_code = self.ml_regex.sub(self.gen_ml_comment, self.source_code)
        self.source_code = self.sl_regex.sub(self.gen_sl_comment, self.source_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='file to add comments to')
    parser.add_argument('-ow', '--overwrite', action='store_true',
                        help='overwrite the input file')
    parser.add_argument('-d', '--destination', help='destination of output file')
    args = parser.parse_args()
    file = open(args.path)

    commenter = Commenter()
    commenter.set_source(file.read())
    file.close()

    commenter.comment()

    if args.overwrite:
        with open(args.path, 'w') as f:
            f.write(commenter.get_source())
            f.close()
    elif args.destination:
        # does not work with folders
        # e.g. -d tests_folder/output2.cpp gives file not found error
         with open(args.destination, 'w') as f:
            f.write(commenter.get_source())
            f.close()
    else:
         with open('output.cpp', 'w') as f:
            f.write(commenter.get_source())
            f.close()
else:
    pass

# idea: to keep indentation consistent between code and inserted comment:
# make regex that searches for start of line, followed by 0 or more whitespace
# followed by non-whitespace character
# can also be done by keeping track of line number and line location

# other idea: write a c++ parser (or, to reduce the scope, a c parser) as outlined in
# CraftingInterpreters.com
# using this parser, add contextually-sensitive comments (i.e. referring to specific
# variables in the source file) to make everything extra-confusing!

# instead of using enumerated type to store parsed information, consider using a
# dictionary where the key is the type of information (e.g. IF_STATEMENT, FUNCTION,
# VARIABLE), and the value is a list of objects corresponding to each type
