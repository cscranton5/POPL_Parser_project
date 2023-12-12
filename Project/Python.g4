grammar Python;

// Define the root rule
prog: (statement+ | NEWLINE)+;

// Define what a statement can be (just expression in our case)
statement:
	expr (NEWLINE|EOF)
	| assignment (NEWLINE|EOF)
    | ifBlock
    | forStatement
    | whileStatement
    // | ifstatement
	| NEWLINE;

// Define an expression with arithmetic operators
expr:
	expr op = ('*' | '/') expr		# MulDiv
	| expr op = ('+' | '-') expr	# AddSub
    | '-' (INT|FLOAT)               # negExpr
	| expr '%' expr					# Mod
    | expr relationalOp expr        # relOp
    | 'not' expr                    # NotExpr
    | expr 'and' expr               # AndExpr
    | expr 'or' expr                # OrExpr
    | VAR '('paramExpr')'           # FuncExpr
	| INT							# Int
	| FLOAT							# Float
	| STRING						# String
    | BOOL                          # Boolean
	| list_expr						# List
	| variable						# VarExpr
	| '(' expr ')'					# Parens;

// Define assignment expressions
assignment: variable assignment_operator expr;

// Define the possible assignment operators
assignment_operator: '=' | '+=' | '-=' | '*=' | '/=';

list_expr: '[' elements? ']';
elements: expr (',' expr)*;


//conditionals with indenting
ifBlock: 
    'if' expr ':' NEWLINE block (elifBlock)* (elseBlock)?;

elifBlock:
    INDENT* 'elif' expr ':' NEWLINE block ;

elseBlock:
    INDENT* 'else' ':' NEWLINE block ;

//loops
forStatement:
    'for' expr 'in' expr ':' NEWLINE block ; 
whileStatement:
    'while' expr ':' NEWLINE block ; 
 
blockStatement: INDENT+ statement ;
block: blockStatement+;


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
AND: 'and';
OR: 'or';
NOT: 'not';

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
BOOL: 'True' | 'False';
// SPACE: ' ' | '\t';

// Tokens for variable names (simple for our example) -- NOTE: the rules for var and function names are same in Python, so use for funcs too
VAR: [a-zA-Z_][a-zA-Z_0-9]*;

paramExpr: expr (',' expr)* ;

// Ignore spaces and tabs
WS: [ ]+ -> skip;

COLON: ':';
INDENT: '\t';
//comments
SINGLE_LINE_COMMENT:
    '#' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: ('\'\'\'' | '"""') .*? ('\'\'\'' | '"""') -> skip;