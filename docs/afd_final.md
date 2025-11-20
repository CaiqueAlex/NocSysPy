# AFD Final do Analisador Léxico

```mermaid
stateDiagram-v2
    [*] --> START

    START --> ID       : letra / _
    ID --> ID          : letra / dígito / _
    ID --> [*]         : aceita IDENTIFIER/KEYWORD

    START --> INT      : 1-9
    START --> ZERO     : 0
    INT --> INT        : dígito
    ZERO --> HEX_PRE   : x
    HEX_PRE --> HEX    : [0-9a-fA-F]
    HEX --> HEX        : [0-9a-fA-F]
    INT --> DOT        : .
    ZERO --> DOT       : .
    DOT --> FLOAT      : dígito
    FLOAT --> FLOAT    : dígito

    INT --> [*]        : aceita INTEGER
    ZERO --> [*]       : aceita INTEGER
    HEX --> [*]        : aceita HEXADECIMAL
    FLOAT --> [*]      : aceita FLOAT

    START --> STRING_START : "
    STRING_START --> STRING_BODY : caractere != " e != \
    STRING_BODY --> STRING_BODY  : caractere != " e != \
    STRING_BODY --> ESCAPE       : \
    ESCAPE --> STRING_BODY       : qualquer
    STRING_BODY --> STRING_END   : "
    STRING_END --> [*]           : aceita STRING

    START --> LESS        : <
    LESS --> LE           : =
    LESS --> SWAP_PRE     : -
    SWAP_PRE --> SWAP     : >
    START --> GREATER     : >
    GREATER --> GE        : =
    START --> ASSIGN      : =
    ASSIGN --> EQUAL      : =
    START --> PLUS        : +
    START --> MINUS       : -
    START --> STAR        : *
    START --> SLASH       : /

    LESS --> [*]      : LESS
    LE --> [*]        : LESS_EQUAL
    SWAP --> [*]      : SWAP
    GREATER --> [*]   : GREATER
    GE --> [*]        : GREATER_EQUAL
    ASSIGN --> [*]    : ASSIGN
    EQUAL --> [*]     : EQUAL
    PLUS --> [*]      : PLUS
    MINUS --> [*]     : MINUS
    STAR --> [*]      : STAR
    SLASH --> [*]     : SLASH