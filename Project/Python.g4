grammar Python;



//   https://github.com/yshavit/antlr-denter

tokens {INDENT, DEDENT}

@lexer::header{
    from antlr_denter.DenterHelper import DenterHelper
    from MyCoolParser import MyCoolParser
}

@lexer::members{
    class MyCoolDenter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: MyCoolLexer = lexer

        def pull_token(self):
            return super(MyCoolLexer, self.lexer).nextToken()
    
    denter = none

    def nextToken(self):
        if not self.denter:
            self.denter = self.MyCoolDenter(self, self.NL, MyCoolParser.INDENT, MyCoolParser.DEDENT, True)
        return self.denter.next_token()
}



// Define the root rule
prog: (statement | NEWLINE)+;

// Define what a statement can be (just an expression in our case)
statement:
    expr NEWLINE
    | expr EOF
    | assignment NEWLINE
    | assignment EOF
    | ifStatement NEWLINE        // Include if statements
    | whileLoop NEWLINE          // Include while loops
    | forLoop NEWLINE            // Include for loops
    | NEWLINE;                   // in case of a new line for formatting

// Define an expression with arithmetic operators
expr:
    expr op = (MULT | DIV) expr        # MulDiv
    | expr op = (ADD | SUB) expr       # AddSub
    | expr MOD expr                    # Mod
    | expr relationalOp expr           # conditional
    | expr AND expr                    # and
    | expr OR expr                     # OR
    | NOT expr                         # not
    | INT                              # Int
    | FLOAT                            # Float
    | STRING                           # String
    | list_expr                        # List
    | variable                         # VarExpr
    | '(' expr ')'                     # Parens;

// Define assignment expressions
assignment: variable assignment_operator expr;

// Define what a variable is
variable: VAR;

// Define [] lists
list_expr: '[' elements? ']';
elements: expr (',' expr)*;

// Define conditional statements
ifStatement:
    IF expr ':' block (elifStatement)* (elseStatement)?;

elifStatement: 'elif' expr ':' block;

elseStatement: 'else' ':' block;

block: INDENT (statement | whileLoop | forLoop | NEWLINE)* DEDENT;

// Define while loop
whileLoop: 'while' expr ':' block;

// Define for loop
forLoop: 'for' VAR 'in' rangeExpr ':' block;
rangeExpr: '(' expr ',' expr ')';

// Operators
arithmetic_operator: MULT | DIV | ADD | SUB | MOD;
assignment_operator: EQU | PLUSEQU | SUBEQU | MULTEQU | DIVEQU;
relationalOp: GT | LT | EQ | NEQ | GTEQ | LTEQ;

// General tokens
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
COLON: ':';
EQU: '=';
PLUSEQU: '+=';
SUBEQU: '-=';
MULTEQU: '*=';
DIVEQU: '/=';
MULT: '*';
DIV: '/';
ADD: '+';
SUB: '-';
MOD: '%';
GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';
GTEQ: '>=';
LTEQ: '<=';
AND: 'and';
OR: 'or';
NOT: 'not';
INT: [0-9]+;
STRING: '"' ( ~["\r\n])* '"' | '\'' ( ~['\\\r\n])* '\'';
FLOAT: [0-9]+ '.' [0-9]+;
NEWLINE: '\r'? '\n' | '\r';
VAR: [a-zA-Z_][a-zA-Z_0-9]*;
WS: [ \t\r\n]+ -> skip;

NL:('\r'? '\n' ' '*); //for denter
