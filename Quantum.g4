grammar Quantum;

// ----------------------
// Reglas del parser
// ----------------------

prog
    : stmt* EOF
    ;

stmt
    : qubitDecl                        # stmtDeclareQubit
    | ID ':' type ASSIGN expr          # stmtUpdateSymbol
    | applyGateStmt                    # stmtApplyGate
    | measureStmt                      # stmtMeasure
    | groverBlock                      # stmtGrover
    | expr SEMI?                       # stmtExpr
    ;

qubitDecl
    : 'qubit' ID SEMI?
    ;


// applyGate:
// - gate(paramList?)               p.ej. h(q0) O rz(1.57,q1)
// - gate(paramList?)(idList)       p.ej. u3(theta,phi,lambda)(q0)

applyGate
    : gate LPAR argList? RPAR ( LPAR idList RPAR )?
    ;

applyGateStmt
    : applyGate SEMI?
    ;

measureStmt
    : 'measure' ID ARROW ID SEMI?
    ;

groverBlock
    : 'grover' ID block
    ;

block
    : LBRACE stmt* RBRACE
    ;

type
    : TINT
    | TFLOAT
    ;

// ----------------------
// Expresiones
// ----------------------
expr
    : expr POW expr                   # powExpr
    | expr MUL expr                   # mulExpr
    | expr DIV expr                   # divExpr
    | expr INTDIV expr                # intDivExpr
    | expr MOD expr                   # modExpr
    | expr ADD expr                   # addExpr
    | expr SUB expr                   # subExpr
    | SUB expr                        # unaryMinusExpr
    | LPAR expr RPAR                  # parenExpr
    | functionCall                     # functionCallExpr
    | NUMBER                           # numberExpr
    | ID                               # idExpr
    ;

functionCall
    : ID LPAR (expr (COMMA expr)*)? RPAR
    ;

// Argumentos y listas
arg
    : ID
    | expr
    ;

argList
    : arg (COMMA arg)*
    ;

idList
    : ID (COMMA ID)*
    ;

// ----------------------
// Puertas (nombres aceptados a nivel de parser)
// ----------------------
gate
    : 'h'
    | 'x'
    | 'y'
    | 'z'
    | 'cx'
    | 'ccx'
    | 'cz'
    | 'u3'
    | 'rz'
    | 'rx'
    | 'ry'
    ;

// ----------------------
// Reglas del lexer (tokens)
// ----------------------

TINT  : 'int' ;
TFLOAT: 'float' ;

// Símbolos / puntuación
POW    : '^' ;
ADD    : '+' ;
SUB    : '-' ;
MUL    : '*' ;
DIV    : '/' ;
INTDIV : '//' ;
MOD    : '%' ;
ASSIGN : '=' ;
LPAR   : '(' ;
RPAR   : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
COLON  : ':' ;
COMMA  : ',' ;
ARROW  : '->' ;
SEMI   : ';' ;

// Identificadores y números
ID
    : [A-Za-z_] [A-Za-z_0-9]*
    ;

// NUMBER coincide con entero o decimal (forma simple)
NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

// Comentarios y espacios en blanco
LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
