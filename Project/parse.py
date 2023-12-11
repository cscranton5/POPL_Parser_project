import subprocess
from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser
from PythonListener import PythonListener
import sys


def read_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
    return code


if len(sys.argv) != 2:
    test_file = "../TestCases/project_deliverable_3_testcase.py"
else:
    test_file = "../TestCases/" + sys.argv[1]

print(test_file)
python_code = read_file(test_file)
input_stream = InputStream(python_code)

lexer = PythonLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = PythonParser(stream)

tree = parser.prog()

walker = ParseTreeWalker()
listener = PythonListener()

walker.walk(listener, tree)

tree_str = tree.toStringTree(recog=parser)

# Display the parse tree in a GUI
with open(test_file, 'rb') as file:
    subprocess.run(['antlr4-parse', 'Python.g4', 'prog', '-gui'], stdin=file)
