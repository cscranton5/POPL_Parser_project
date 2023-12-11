grammar Python;

tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from PythonParser import PythonParser
}
@lexer::members {
class MyCoolDenter(DenterHelper):
    def __init__(self, lexer, NEWLINE_token, indent_token, dedent_token, ignore_eof):
        super().__init__(NEWLINE_token, indent_token, dedent_token, ignore_eof)
        self.lexer: PythonLexer = lexer

    def pull_token(self):
        return super(PythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.MyCoolDenter(self, self.NEWLINE, PythonParser.INDENT, PythonParser.DEDENT, True)
    return self.denter.next_token()

}

// NL: ('\r'? '\n' ' '*); //For tabs just switch out ' '* with '\t'*

// Define the root rule
prog: (statement+ | NEWLINE)+;

// Define what a statement can be (just expression in our case)
statement:
	expr NEWLINE
	| assignment NEWLINE
	| NEWLINE
    | expr EOF
    | assignment EOF; //in case new line for formatting

// Define an expression with arithmetic operators
expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
	| expr '%' expr					# Mod
	| INT							# Int
	| FLOAT							# Float
	| STRING						# String
	| list_expr						# List
	| variable						# VarExpr
	| '(' expr ')'					# Parens;

// Define assignment expressions
assignment: variable assignment_operator expr;

// Define the possible assignment operators
assignment_operator: '=' | '+=' | '-=' | '*=' | '/=';

list_expr: '[' elements? ']';
elements: expr (',' expr)*;


//Atul Pseudocode for conditional statements, don't think they work yet
ifBlock: INDENT 'if' expr ':' NEWLINE block (elifBlock)* (elseBlock)? DEDENT ;
elifBlock: INDENT 'elif' expr ':' NEWLINE block DEDENT ;
elseBlock: INDENT 'else' ':' NEWLINE block DEDENT ;

block: (statement | ifBlock | NEWLINE)+ ;

// Tokens for the arithmetic operators
MULT: '*';
DIV: '/';
ADD: '+';
SUB: '-';
MOD: '%';
GT:   '>' ;
LT:   '<' ;
EQ:   '==' ;
NEQ:  '!=' ;
GTEQ: '>=' ;
LTEQ: '<=' ;


// INDENT: ' ' { getCharPositionInLine() == 0 } -> channel(HIDDEN) ;
// DEDENT: '\n' { getCharPositionInLine() == 0 } -> channel(HIDDEN) ;

relationalOp
    : GT
    | LT
    | EQ
    | NEQ
    | GTEQ
    | LTEQ
    ;

// Define what a variable is
variable: VAR;

// Tokens for var types and newline
INT: [0-9]+;
STRING: '"' ( ~["\r\n])* '"' | '\'' ( ~['\\\r\n])* '\'';
FLOAT: [0-9]+ '.' [0-9]+;
NEWLINE: '\r'? '\n';

// Tokens for variable names (simple for our example)
VAR: [a-zA-Z_][a-zA-Z_0-9]*;

// Ignore spaces and tabs
WS: [ \t]+ -> skip;