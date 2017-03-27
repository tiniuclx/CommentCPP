"""Contains the various dictionaries usable by the commenter class

"""
std_CPP = {
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