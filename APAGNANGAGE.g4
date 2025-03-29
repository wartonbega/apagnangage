grammar APAGNANGAGE;

// Lexer

ID: ('AP' | 'AGN' | 'AN')+;

fragment DECIMAL_SEPARATOR: 'P' | 'GN' | 'N';
INT: 'A'+ | ('AA' | DECIMAL_SEPARATOR) ('A'* DECIMAL_SEPARATOR)*; // using decimal separators requires at least two A or a DECIMAL_SEPARATOR at the beginning

PRINT: 'POV';

ASSIGN: 'DANS';

FUNCTION_DEF: 'QUOI' WS* 'FEUR';
FUNCTION_CALL: 'QUOI';
RETURN: 'FEUR';

BLOCK_START: 'FAIT';
BLOCK_END: 'BELECK';

fragment WS: [ \t\r\n];

EQUALS: 'C' WS* '\'' WS* 'EST';

PLUS: '+';
MINUS: '-';
MULTIPLY: '*';
DIVIDE: '/';

LOOP: 'GRAND' WS* 'SABLON';
LOOP_COUNTER: 'OUH';
BREAK: 'FF';

IF: 'GENRE';

fragment STRING_START: 'TU' WS* 'FAIS' WS* 'UN' WS?;
fragment STRING_CONTENT: (.*?);

STRING_ASSIGN: STRING_START (.*?) WS? ASSIGN;
STRING_LINE: STRING_START ((~[D\n] | 'D' ~'A' | 'DA' ~'N' | 'DAN' ~'S')*); // no 'DANS' allowed in string

COMMENT: 'CRARI' (~'\n')* -> skip;

WS_: WS+ -> skip;

// Parser

program
    : statement *
      EOF
    ;

statement
    : assignment
    | function_call
    | function_def
    | print
    | print_assign_string
    | loop
    | if
    | BREAK
    | return
    | increment
    ;

assignment
    : expression ASSIGN ID
    ;

expression_int
    : INT
    ;

operator
    : PLUS
    | MINUS
    | MULTIPLY
    | DIVIDE
    | EQUALS
    ;

expression 
    : ( operator
      | function_call
      | expression_int
      | ID
      ) +
    ;

function_call
    : FUNCTION_CALL ID
    ;

print
    : PRINT (expression | STRING_LINE)
    ;

print_assign_string
    : PRINT  STRING_ASSIGN ID
    ;

loop_counter
    : LOOP_COUNTER *
    | ID
    ;

loop
    : LOOP ID? LOOP loop_counter block
    ;


logic
    : expression EQUALS expression
    ;

// Je met plutot une expression qu'une logique 
if
    : IF expression block
    ;

block
    : BLOCK_START
      statement *
      BLOCK_END
    | BREAK
    ;

increment
    : LOOP_COUNTER ID
    ;

function_def
    : FUNCTION_DEF
      BLOCK_START
      statement *
      BLOCK_END ?
      ASSIGN
      ID
    ;

return
    : RETURN expression ?
    ;