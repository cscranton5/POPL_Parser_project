from antlr4 import *
from PythonLexer import PythonLexer
from PythonParser import PythonParser
from PythonListener import PythonListener

class Main:
    @staticmethod
    def test(input_str):
        def contains_tabs(code):
            return '\t' in code
        if(contains_tabs(input_str)): print('CONTAINS TABS')
        else: print("NO TABS")
        lexer = PythonLexer(InputStream(input_str))
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()

        print(f"input: `{input_str}`")
        print("\n")

        for token in token_stream.tokens:
            if token.type != Token.EOF:
                # print(token.type)
                print(f"  {token.type}: {PythonLexer.ruleNames[token.type-1]:20} {token.text}")

        print()

def read_file(filename):
    file = open(filename, 'r')
    code = file.read()
    # print(code)
    file.close()
    return code


if __name__ == "__main__":
    test_file = "../TestCases/project_deliverable_2_testcase.py"
    # test_file = "../TestCases/test.py"

    python_code = read_file(test_file) + '\r\n'
    # input_stream = InputStream(python_code)
    Main.test(python_code)
    print(python_code[len(python_code)-1])
