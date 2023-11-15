grammar Python;

// Define the root rule
prog: (statement | ifBlock | NEWLINE)+;

// Define what a statement can be (just expression in our case)
statement:
	expr NEWLINE
	| assignment NEWLINE
	| NEWLINE; //in case new line for formatting

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


// Define conditional statements
ifBlock: 'if' expr ':' NEWLINE INDENT block DEDENT (elifBlock)* (elseBlock)?;
elifBlock: 'elif' expr ':' NEWLINE INDENT block DEDENT;
elseBlock: 'else' ':' NEWLINE INDENT block DEDENT;

// Define a block of statements
block: (statement | ifBlock | NEWLINE)+;

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


// Tokens for indentation
INDENT: ' ' {getCharPositionInLine() == 0}? -> skip;
DEDENT: '\n' {getCharPositionInLine() == 0}? -> skip;

// Possible alternative for Tokens for indentation
// INDENT: [ \t]+ -> skip;
// DEDENT: '\r'? '\n' [ \t]* {getCharPositionInLine() == 0}? -> skip;


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
