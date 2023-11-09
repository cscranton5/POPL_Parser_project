grammar Python;

// Define the root rule
prog: (statement+ | NEWLINE)+;

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

// Tokens for the arithmetic operators
MULT: '*';
DIV: '/';
ADD: '+';
SUB: '-';
MOD: '%';

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