grammar APAGNANGAGE;

// Lexer

ID: ('AP' | 'AGN' | 'AN')+;

fragment DECIMAL_SEPARATOR: 'P' | 'GN' | 'N';
INT: 'A'+ | ('AA' | DECIMAL_SEPARATOR) ('A'* DECIMAL_SEPARATOR)*; // using decimal separators requires at least two A or a DECIMAL_SEPARATOR at the beginning

PRINT: 'POV';

ASSIGN: 'QUOI';

FUNCTION_CALL: 'FEUR';

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

STRING_ASSIGN: STRING_START (.*?) WS? 'DANS';
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
    | print
    | print_assign_string
    | loop
    | if
    | BREAK
    | increment
    ;

assignment
    : ID ASSIGN expression
    ;

expression 
    : (PLUS | MINUS | MULTIPLY | DIVIDE | EQUALS | function_call | INT | ID)+;

function_call
    : FUNCTION_CALL ID
    ;

print
    : PRINT (expression | STRING_LINE)
    ;

print_assign_string
    : PRINT ? STRING_ASSIGN ID
    ;

loop
    : LOOP ID? LOOP (ID | LOOP_COUNTER*) block
    ;

logic
    : expression EQUALS expression
    ;

if
    : IF logic block
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