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

###### Estruturas de Controle

se (condicao) {
    # bloco
} senaose (outra_condicao) {
    # bloco
} senao {
    # bloco
}

enquanto (condicao) {
    # bloco
}

para (variavel em iteravel) {
    # bloco
}

Aritiméticos

Adição: a + b
Subtração: a - b
Multiplicação: a * b
Divisão: a / b
Divisão inteira: a // b
Módulo: a % b
Potenciação: a ** b

Comparação

Igual: a == b
Diferente: a != b
Menor: a < b
Maior: a > b
Menor ou igual: a <= b
Maior ou igual: a >= b

Lógicos

E lógico: a e b
Ou lógico: a ou b
Negação: nao a

Especiais

Troca: a <-> b (troca os valores de a e b)
Null coalescing: a ?? b (retorna b se a for nada)
Pipe: valor |> funcao (equivale a funcao(valor))

Tipos Básicos

inteiro: Números inteiros
real: Números de ponto flutuante
texto: Strings
booleano: verdadeiro/falso
lista: Arrays dinâmicos
dicionario: Hash maps

Declaração com Tipos

tipo inteiro idade = 25;
tipo texto nome = "João";
tipo lista numeros = [1, 2, 3];

####### Unicas

Threading Simples

async funcao tarefa() {
    escreva("Executando em paralelo");
}

# Executa múltiplas tarefas
aguarda tarefa1(), tarefa2(), tarefa3();

Pipeline de Dados

resultado = dados
    |> filtrar(condicao)
    |> mapear(transformacao)
    |> reduzir(operacao);

Troca de Variáveis

a = 10;
b = 20;
a <-> b;  # Agora a = 20 e b = 10

escreva(): Saída de dados
leia(): Entrada de dados
tamanho(): Comprimento de sequências
inteiro(), real(), texto(), booleano(): Conversão de tipos
tipo_de(): Retorna o tipo de uma variável
async(): Executa função de forma assíncrona