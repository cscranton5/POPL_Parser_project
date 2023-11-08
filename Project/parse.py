from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser
from PythonListener import PythonListener

# Read your code from a file or from a string
python_code = "yo = 3\n"
input_stream = InputStream(python_code)

# Create a lexer and parser
lexer = PythonLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = PythonParser(stream)

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
print(tree_str)