# Especificação da Linguagem NocSysPy

## 1. Alfabeto

### Letras
- Minúsculas: `a` até `z`
- Maiúsculas: `A` até `Z`

### Dígitos
- `0` até `9`

### Símbolos Especiais
- Operadores aritméticos: `+`, `-`, `*`, `/`, `%`, `**`, `//`
- Operadores de comparação: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Operadores lógicos: `e`, `ou`, `nao`
- Operadores especiais: `<->` (troca), `??` (null coalescing), `=>` (arrow), `|>` (pipe)
- Atribuição: `=`
- Delimitadores: `(`, `)`, `[`, `]`, `{`, `}`, `:`, `,`, `;`
- Strings: `"`, `'`
- Comentário: `#`
- Underscore: `_`

### Caracteres de Espaçamento
- Espaço: ` `
- Tabulação: `\t`
- Nova linha: `\n`

## 2. Estrutura Léxica

### Palavras-chave
se, senao, senaose, enquanto, para, funcao, retorna, classe,
importa, de, como, em, eh, verdadeiro, falso, nada,
e, ou, nao, quebra, continua, pula, escreva, leia, tipo, async, aguarda

### Identificadores
- Iniciam com letra ou underscore
- Podem conter letras, dígitos e underscore
- Case-sensitive
- Regex: `[a-zA-Z_][a-zA-Z0-9_]*`

### Literais

#### Números Inteiros
- Decimais: `42`, `1000`, `0`
- Hexadecimais: `0x1F`, `0xFF`
- Regex: `[0-9]+|0x[0-9A-Fa-f]+`

#### Números de Ponto Flutuante
- Com ponto decimal: `3.14`, `0.001`, `42.0`
- Notação científica: `1e5`, `2.5e-3`
- Regex: `[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?`

#### Strings
- Delimitadas por aspas simples: `'texto'`
- Delimitadas por aspas duplas: `"texto"`
- Strings multi-linha: `"""texto"""`
- Suportam caracteres de escape: `\n`, `\t`, `\\`, `\"`, `\'`

#### Booleanos
- `verdadeiro`
- `falso`

#### Valor Nulo
- `nada`

### Comentários
- Linha única: `# comentário até o fim da linha`
- Multi-linha: `/* comentário em bloco */`

## 3. Estrutura da Linguagem

### Programa
Um programa NocSysPy é uma sequência de declarações e instruções delimitadas por chaves.

### Declarações

#### Variáveis
```nocsyspy
nome = valor;
x = 10;
mensagem = "Olá";
tipo numero = 42;  # Declaração com tipo

##### Funções

funcao nome_funcao(parametros) => tipo {
    # corpo da função
    retorna valor;
}

# Arrow function
quadrado = (x) => x * x;

# Função async
async funcao buscar_dados() => lista {
    aguarda requisicao();
    retorna dados;
}