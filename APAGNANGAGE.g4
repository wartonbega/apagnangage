grammar APAGNANGAGE;

// Lexer

ID: ('AP' | 'AGN' | 'AN')+;

fragment DECIMAL_SEPARATOR: 'P' | 'GN' | 'N';
INT: 'A'+ | ('AA' | DECIMAL_SEPARATOR) ('A'* DECIMAL_SEPARATOR)*; // using decimal separators requires at least two A or a DECIMAL_SEPARATOR at the beginning

PRINT: 'POV';

fragment WS: [ \t\r\n];

ASSIGN: 'DANS';

FUNCTION_DEF: 'QUOI' WS* 'FEUR';
FUNCTION_CALL: 'QUOI';
RETURN: 'FEUR';

BLOCK_START: 'FAIT';
BLOCK_END: 'BELECK';

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

fragment INPUT: 'EH' WS* '!';

// no "DANS" or "BELECK" allowed in string
fragment CHARS_NOT_ALLOWED_COMPLETIONS: 'D' ~[A\n] | 'DA' ~[N\n] | 'DAN' ~[S\n]
                                      | 'B' ~[E\n] | 'BE' ~[L\n] | 'BEL' ~[E\n] | 'BELE' ~[C\n] | 'BELEC' ~[K\n];
fragment CHARS: ~[DB\n] | CHARS_NOT_ALLOWED_COMPLETIONS;

STRING_LINE: STRING_START CHARS* BLOCK_END?; // last BLOCK_END for inline string
STRING_ASSIGN: STRING_START CHARS*? ' '? ASSIGN;
STRING_INPUT: INPUT CHARS*? ' '? ASSIGN;

LIST: 'OB';
LIST_POP: 'SG';
LIST_INDEX: 'LE' | 'LA';

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
    | input_assign_string
    | loop
    | if
    | BREAK
    | return
    | increment
    | list_def
    | list_append
    | list_pop_or_get
    ;

assignment
    : expression ASSIGN ID
    | assign_string
    ;

assign_string
    : STRING_ASSIGN ID
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
      | list_pop_or_get
      | ID
      ) +
    ;

function_call
    : FUNCTION_CALL ID
    ;

print
    : PRINT (expression | STRING_LINE | assign_string)
    ;

input_assign_string
    : STRING_INPUT ID
    ;

loop_counter
    : LOOP_COUNTER * // 0 -> boucle infinie
    | ID
    ;

loop
    : LOOP ID? LOOP loop_counter block
    ;

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
    : RETURN (expression ? | STRING_LINE)
    ;

list_def
    : LIST ID
    ;

list_append
    : LIST (expression ASSIGN ID | assign_string)
    ;

list_pop_or_get // expression is the index
    : LIST ? // if LIST: get, else: pop
      LIST_POP ID (LIST_INDEX expression) ? (ASSIGN ID)?
    ;