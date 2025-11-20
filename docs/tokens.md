# Tokens da Linguagem PySimple

## 1. Tokens de Palavras-chave

| Token | Lexema | Descrição |
|-------|--------|-----------|
| IF | if | Estrutura condicional |
| ELSE | else | Alternativa condicional |
| ELIF | elif | Else if |
| WHILE | while | Loop while |
| FOR | for | Loop for |
| DEF | def | Definição de função |
| RETURN | return | Retorno de função |
| CLASS | class | Definição de classe |
| IMPORT | import | Importação |
| FROM | from | Importação específica |
| AS | as | Alias |
| IN | in | Operador de pertencimento |
| IS | is | Comparação de identidade |
| AND | and | Operador lógico E |
| OR | or | Operador lógico OU |
| NOT | not | Operador lógico NÃO |
| TRUE | True | Valor booleano verdadeiro |
| FALSE | False | Valor booleano falso |
| NONE | None | Valor nulo |
| BREAK | break | Interrompe loop |
| CONTINUE | continue | Continua loop |
| PASS | pass | Instrução vazia |
| PRINT | print | Função de saída |
| INPUT | input | Função de entrada |

## 2. Tokens de Identificadores

| Token | Padrão | Descrição |
|-------|--------|-----------|
| IDENTIFIER | [a-zA-Z_][a-zA-Z0-9_]* | Nome de variáveis, funções, etc. |

## 3. Tokens de Literais

| Token | Padrão | Descrição |
|-------|--------|-----------|
| INTEGER | [0-9]+ | Número inteiro |
| FLOAT | [0-9]+\.[0-9]+ | Número decimal |
| STRING | '[^']*' \| "[^"]*" | Cadeia de caracteres |

## 4. Tokens de Operadores

### Operadores Aritméticos
| Token | Lexema | Descrição |
|-------|--------|-----------|
| PLUS | + | Adição |
| MINUS | - | Subtração |
| MULTIPLY | * | Multiplicação |
| DIVIDE | / | Divisão |
| FLOOR_DIV | // | Divisão inteira |
| MODULO | % | Módulo |
| POWER | ** | Potenciação |

### Operadores de Comparação
| Token | Lexema | Descrição |
|-------|--------|-----------|
| EQUAL | == | Igualdade |
| NOT_EQUAL | != | Desigualdade |
| LESS | < | Menor que |
| GREATER | > | Maior que |
| LESS_EQUAL | <= | Menor ou igual |
| GREATER_EQUAL | >= | Maior ou igual |

### Operador de Atribuição
| Token | Lexema | Descrição |
|-------|--------|-----------|
| ASSIGN | = | Atribuição |

## 5. Tokens de Delimitadores

| Token | Lexema | Descrição |
|-------|--------|-----------|
| LPAREN | ( | Parênteses esquerdo |
| RPAREN | ) | Parênteses direito |
| LBRACKET | [ | Colchete esquerdo |
| RBRACKET | ] | Colchete direito |
| LBRACE | { | Chave esquerda |
| RBRACE | } | Chave direita |
| COLON | : | Dois pontos |
| COMMA | , | Vírgula |

## 6. Tokens de Controle

| Token | Lexema | Descrição |
|-------|--------|-----------|
| NEWLINE | \n | Nova linha |
| INDENT | (espaços) | Indentação |
| DEDENT | (redução) | Redução de indentação |
| EOF | (fim) | Fim do arquivo |

## 7. Tokens Especiais

| Token | Lexema | Descrição |
|-------|--------|-----------|
| COMMENT | #.* | Comentário |
| WHITESPACE | [ \t]+ | Espaços em branco |