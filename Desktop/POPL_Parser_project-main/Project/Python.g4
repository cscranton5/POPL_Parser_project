grammar Python;

// NL: ('\r'? '\n' ' '*); //For tabs just switch out ' '* with '\t'*

// Define the root rule
prog: (statement+ | NEWLINE)+;

// Define what a statement can be (just expression in our case)
statement:
	expr NEWLINE
	| assignment NEWLINE
	| NEWLINE
	| ifBlock
	| forStatement
	| whileStatement
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
ifBlock:
	INDENT 'if' expr COLON NEWLINE block (elifBlock)* (elseBlock)?;
elifBlock: INDENT 'elif' expr COLON NEWLINE block;
elseBlock: INDENT 'else' COLON NEWLINE block;

block: (statement | ifBlock | NEWLINE)+;

forStatement: 'for' expr 'in' expr COLON NEWLINE block;
whileStatement: 'while' expr COLON NEWLINE block;

// Tokens for the arithmetic operators
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

// INDENT: ' ' { getCharPositionInLine() == 0 } -> channel(HIDDEN) ; DEDENT: '\n' {
// getCharPositionInLine() == 0 } -> channel(HIDDEN) ;

relationalOp: GT | LT | EQ | NEQ | GTEQ | LTEQ;

// Define what a variable is
variable: VAR;

// Tokens for var types and newline
COLON: ':';

INT: [0-9]+;
STRING: '"' ( ~["\r\n])* '"' | '\'' ( ~['\\\r\n])* '\'';
FLOAT: [0-9]+ '.' [0-9]+;
NEWLINE: '\r'? '\n';

//SPACE: [' ' | \t]+ -> skip;

SINGLE_LINE_COMMENT: '#' ~[\r\n]* -> skip;

// Multi-line comment starts and ends with triple single or double quotes
MULTI_LINE_COMMENT_TRIPLE: '"""' .*? '"""' -> skip;

INDENT: '\t';
// Tokens for variable names (simple for our example)
VAR: [a-zA-Z_][a-zA-Z_0-9]*;

// Ignore spaces and tabs
WS: [ ]+ -> skip;