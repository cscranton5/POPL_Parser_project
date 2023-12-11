from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser
from PythonListener import PythonListener
import sys
import os


def read_file(filename):
    file = open(filename, 'r')
    code = file.read()
    # print(code)
    file.close()
    return code


# Read your code from a file or from a string
if (len(sys.argv) != 2):
    test_file = "../TestCases/project_deliverable_3_testcase.py"
else:
    test_file = "../TestCases/" + sys.argv[1]
    default = False

print(test_file)
python_code = read_file(test_file)
input_stream = InputStream(python_code)

# Create a lexer and parser
lexer = PythonLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = PythonParser(stream)

#indentation

# Parse the code
tree = parser.prog()

# Create a parse tree walker and listener
walker = ParseTreeWalker()
listener = PythonListener()

# Walk the parse tree
walker.walk(listener, tree)

# Get the string representation of the parse tree
tree_str = tree.toStringTree(recog=parser)

# Print the parse tree
# print(tree_str)

# Generates parse tree as a GUI

os.system(
    'antlr4-parse Python.g4 prog -gui < ' + test_file)
os.system('Ctrl + D')
