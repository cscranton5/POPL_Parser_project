grammar Python;

// Define the root rule
prog: (statement | NEWLINE)+;
//prog: (statement | ifBlock | NEWLINE)+;		////////SWAP WITH ABOVE TO WORK ON IFBLOCKS/////////////////////

// Define what a statement can be (just expression in our case)
statement:
	expr NEWLINE
	| expr EOF
	| assignment NEWLINE
	| assignment EOF
	| NEWLINE; //in case new line for formatting

// Define an expression with arithmetic operators
expr:
	expr op = (MULT | DIV) expr		# MulDiv
	| expr op = (ADD | SUB) expr	# AddSub
	| expr MOD expr					# Mod
	| expr relationalOp expr		# conditional
	| expr AND expr					# and
	| expr OR expr					# OR
	| NOT expr						# not
	| INT							# Int
	| FLOAT							# Float
	| STRING						# String
	| list_expr						# List
	| variable						# VarExpr
	| '(' expr ')'					# Parens;

// Define assignment expressions
assignment: variable assignment_operator expr;

//Define [] lists
list_expr: '[' elements? ']';
elements: expr (',' expr)*;

//Define conditional statements
ifStatement:
	IF expr ':' block (elifStatement)* (elseStatement)?;

elifStatement: 'elif' expr ':' block;

elseStatement: 'else' ':' block;

block: INDENT statement* DEDENT;
/* /////////COMMENTED OUT TO TEST CONDITIONALS////////////////////
 //_________________________IF/ELSE_BLOCKS______________________//
 
 // Define conditional statements ifBlock: 'if' expr ':' NEWLINE INDENT block DEDENT (elifBlock)*
 (elseBlock)?; elifBlock: 'elif' expr ':' NEWLINE INDENT block DEDENT; elseBlock: 'else' ':' NEWLINE
 INDENT block DEDENT;
 
 // Define a block of statements block: (statement | ifBlock | NEWLINE)+;
 
 // Tokens for indentation INDENT: ' ' {getCharPositionInLine() == 0}? -> skip; DEDENT: '\n'
 {getCharPositionInLine() == 0}? -> skip;
 
 // Possible alternative for Tokens for indentation // INDENT: [ \t]+ -> skip; // DEDENT: '\r'? '\n'
 [ \t]* {getCharPositionInLine() == 0}? -> skip;
 

 */

//__________________OPERATORS______________________//

arithmetic_operator: MULT | DIV | ADD | SUB | MOD;

assignment_operator: EQU | PLUSEQU | SUBEQU | MULTEQU | DIVEQU;

relationalOp: GT | LT | EQ | NEQ | GTEQ | LTEQ;

//__________________GENERAL_TOKENS____________________________//

//tokens for conditional statements
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
COLON: ':';

//tokens for assignment operators
EQU: '=';
PLUSEQU: '+=';
SUBEQU: '-=';
MULTEQU: '*=';
DIVEQU: '/=';

// Tokens for the arithmetic operators
MULT: '*';
DIV: '/';
ADD: '+';
SUB: '-';
MOD: '%';

// Tokens for Conditional Statments
GT: '>';
LT: '<';
EQ: '==';
NEQ: '!=';
GTEQ: '>=';
LTEQ: '<=';

AND: 'and';
OR: 'OR';
NOT: 'not';

// Tokens for var types and newline
INT: [0-9]+;
STRING: '"' ( ~["\r\n])* '"' | '\'' ( ~['\\\r\n])* '\'';
FLOAT: [0-9]+ '.' [0-9]+;
NEWLINE: '\r'? '\n';
//SPACE: [ \t\r\n] -> skip;
INDENT: '\n' [ \t]+;
DEDENT: '\n' ~[ \t\n]+;

// Define what a variable is
variable: VAR;
// Tokens for variable names (simple for our example)
VAR: [a-zA-Z_][a-zA-Z_0-9]*;

// Ignore spaces and tabs
WS: [ \t\r\n]+ -> skip;

