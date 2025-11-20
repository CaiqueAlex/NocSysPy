# Especificação da Linguagem PySimple

## 1. Alfabeto

### Letras
- Minúsculas: `a` até `z`
- Maiúsculas: `A` até `Z`

### Dígitos
- `0` até `9`

### Símbolos Especiais
- Operadores aritméticos: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- Operadores de comparação: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Operadores lógicos: `and`, `or`, `not`
- Atribuição: `=`
- Delimitadores: `(`, `)`, `[`, `]`, `{`, `}`, `:`, `,`
- Strings: `"`, `'`
- Comentário: `#`
- Underscore: `_`

### Caracteres de Espaçamento
- Espaço: ` `
- Tabulação: `\t`
- Nova linha: `\n`

## 2. Estrutura Léxica

### Palavras-chave
if, else, elif, while, for, def, return, class,
import, from, as, in, is, True, False, None,
and, or, not, break, continue, pass, print, input

### Identificadores
- Iniciam com letra ou underscore
- Podem conter letras, dígitos e underscore
- Case-sensitive
- Regex: `[a-zA-Z_][a-zA-Z0-9_]*`

### Literais

#### Números Inteiros
- Decimais: `42`, `1000`, `0`
- Regex: `[0-9]+`

#### Números de Ponto Flutuante
- Com ponto decimal: `3.14`, `0.001`, `42.0`
- Regex: `[0-9]+\.[0-9]+`

#### Strings
- Delimitadas por aspas simples: `'texto'`
- Delimitadas por aspas duplas: `"texto"`
- Suportam caracteres de escape: `\n`, `\t`, `\\`, `\"`, `\'`

#### Booleanos
- `True`
- `False`

#### Valor Nulo
- `None`

### Comentários
- Linha única: `# comentário até o fim da linha`

### Programa
Um programa PySimple é uma sequência de declarações e instruções.

### Declarações

#### Variáveis
```python
nome = valor
x = 10
mensagem = "Olá"

def nome_funcao(parametros):
    # corpo da função
    return valor

if condicao:
    # bloco
elif outra_condicao:
    # bloco
else:
    # bloco

while condicao:
    # bloco

for variavel in iteravel:
    # bloco

Adição: a + b
Subtração: a - b
Multiplicação: a * b
Divisão: a / b
Divisão inteira: a // b
Módulo: a % b
Potenciação: a ** b

Igual: a == b
Diferente: a != b
Menor: a < b
Maior: a > b
Menor ou igual: a <= b
Maior ou igual: a >= b

E lógico: a and b
Ou lógico: a or b
Negação: not a

Tipagem dinâmica
Tipos: int, float, str, bool, None, list

Escopo léxico
Variáveis locais em funções
Variáveis globais

Implícita em operações mistas (int + float = float)
Explícita com funções: int(), float(), str(), bool()

print(): Saída de dados
input(): Entrada de dados
len(): Comprimento de sequências
int(), float(), str(), bool(): Conversão de tipos