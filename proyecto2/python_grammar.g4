grammar python_grammar;

parse
 : from_input | from_file
 ;

from_input
 : stat NEWLINE
 ;

from_file
 : (stat|NEWLINE)* EOF
 ;

stat
 : simple_stat
 | compound_stat
 ;

compound_stat
 : if_stat
 | while_stat
 | for_stat
 | funcion
 ;

simple_stat
 : assignment
 | log
 | importar
 | retornar
 | atom NEWLINE
 | OTHER
 ;

assignment
 : variable (POINTS type_anotation)?ASSIGN (assignment|expr) 
 ;

if_stat
 : IF condition_block (ELIF condition_block)* (ELSE POINTS stat_block)?
 ;

while_stat
 : WHILE expr POINTS stat_block
 ;

for_stat
 : FOR ID IN expr POINTS stat_block
 ;

log
 : LOG OPAR expr CPAR
 ;

funcion
 : FUNCION ID OPAR ((parametro (POINTS type_anotation)?)  (COMMA (parametro (POINTS type_anotation)?))*)?
 CPAR (MINUS GT type_anotation)? POINTS (NEWLINE|stat)+
 ;

importar
 : IMPORT ID (POINT ID)*
 | FROM ID IMPORT ID
 ;

call_function
 : (variable | TYPES | ID) OPAR ((INT | FLOAT | STRING | variable | expr) (COMMA (INT | FLOAT | STRING | variable | expr))*)?
 (((ID ASSIGN)?(INT | FLOAT | STRING | variable | expr)) (COMMA ((ID ASSIGN)?(INT | FLOAT | STRING | variable | expr)))*)? CPAR ;

retornar
 : RETORNO OPAR? expr CPAR? NEWLINE
 ;

condition_block
 : expr POINTS NEWLINE? stat_block
 ;

stat_block
 : (stat|NEWLINE)* 
 | stat NEWLINE
 ;

array
 : OKEY (expr (COMMA expr)*)? CKEY
 | OKEY start=expr POINTS (step=expr POINTS)? end=expr CKEY
 ;

tuple
 : OPAR (expr (COMMA expr)*)? CPAR
 | OPAR start=expr POINTS (step=expr POINTS)? end=expr CPAR
 ; 

accessarray
 : variable OKEY expr CKEY
 ;

type_anotation : (TYPES | OKEY (TYPES (COMMA TYPES)*)? CKEY | 'dict' OKEY (TYPES (COMMA TYPES)*)? CKEY | 'list' OKEY (TYPES (COMMA TYPES)*)? CKEY | 'tuple' OKEY (TYPES (COMMA TYPES)*)? CKEY);

variable
 : ID (POINT ID)* (OPAR (expr (COMMA expr)*)? CPAR)?
 | ID (POINT ID)* OKEY expr CKEY
 ;

parametro
 : ID (ASSIGN expr)?
 ;

expr
 : <assoc=right>left=expr POW right=expr        #powExpr
 | MINUS expr                                   #unaryMinusExpr
 | NOT expr                                     #notExpr
 | left=expr op=(MULT|DIV|MOD) right=expr       #multiplicationExpr
 | left=expr op=(PLUS|MINUS) right=expr         #additiveExpr
 | left=expr op=(LTEQ|GTEQ|LT|GT) right=expr    #relationalExpr
 | left=expr op=(EQ|NEQ) right=expr             #equalityExpr
 | left=expr AND right=expr                     #andExpr
 | left=expr OR right=expr                      #orExpr
 | OPAR expr CPAR 						        #parExpr
 | atom                                         #atomExpr
 ;

atom 
 : call_function #callAtom
 | (TRUE|FALSE) #booleanAtom
 | STRING       #stringAtom
 | array		#arrayAtom
 | tuple        #tupleAtom
 | objeto		#objetoAtom
 | accessarray  #accessToarray
 | variable		#accessVariable
 | NULL          #NULLAtom
 | (INT|FLOAT)  #numberAtom
 | lambda_func #lambdaAtom
 ;

lambda_func
 : (variable (COMMA variable)*)? ASSIGN LAMBDA (variable (COMMA variable)*)? POINTS expr;

objeto
 : OBRACE (keyvalue (COMMA keyvalue)*)? CBRACE
 | OBRACE ((ID | STRING | INT) (COMMA (ID | STRING | INT))*)? CBRACE
 | OBRACE (expr (COMMA expr)*)? CBRACE
 | OBRACE start=expr POINTS (step=expr POINTS)? end=expr CBRACE
 ; 

keyvalue
 : ID POINTS expr
 | STRING POINTS expr
 | INT POINTS expr
 ;

LAMBDA : 'lambda';
OR : 'or';
AND : 'and';
EQ : '==';
NEQ : '!=';
GT : '>';
LT : '<';
GTEQ : '>=';
LTEQ : '<=';
PLUS : '+';
MINUS : '-';
MULT : '*';
DIV : ('/' | '//');
MOD : '%';
POW : '**';
NOT : 'not';

TYPES : ('int' | 'float' | 'double' | 'str' | 'bool');
ASSIGN : '=';
OPAR : '(';
CPAR : ')';
OBRACE : '{';
CBRACE : '}';
OKEY : '[';
CKEY : ']';
COMMA : ',';
POINTS: ':';

TRUE : 'True';
FALSE : 'False';
NULL : 'None';
IF : 'if';
ELSE : 'else';
ELIF : 'elif';
WHILE : 'while';
LOG : 'print';
FOR : 'for';
IN : 'in';
FUNCION: 'def';
RETORNO: 'return';
IMPORT: 'import';
FROM: 'from';
ASTERISC: 'todo';
POINT: '.';

ID
 : [a-zA-Z_] [a-zA-Z_0-9]*
 ;

INT
 : [0-9]+
 ;

FLOAT
 : [0-9]+ '.' [0-9]*
 | '.' [0-9]+
 ;

STRING
 : '"' (~["\r\n] | '""')* '"'
 | '\'' (~["\r\n] | '""')* '\''
 ;
COMMENT
 : '#' ~[\r\n]* -> skip
 ;
SPACE
 : [ \t\r] -> skip
 ;
NEWLINE
 : [\n]
 ;
OTHER
 : .
 ;

