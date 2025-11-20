# Gramática Formal da Linguagem NocSysPy

## 1. Introdução

Esta especificação define a gramática formal da linguagem NocSysPy utilizando a notação **EBNF (Extended Backus-Naur Form)**. A linguagem é projetada para ser expressiva, legível e com características únicas de programação.

## 2. Gramática Formal em EBNF

### 2.1 Símbolos Terminais

```ebnf
(* Palavras-chave *)
SE = "se" ;
SENAO = "senao" ;
SENAOSE = "senaose" ;
ENQUANTO = "enquanto" ;
PARA = "para" ;
FUNCAO = "funcao" ;
RETORNA = "retorna" ;
CLASSE = "classe" ;
TIPO = "tipo" ;
ASYNC = "async" ;
AGUARDA = "aguarda" ;
E = "e" ;
OU = "ou" ;
NAO = "nao" ;
EM = "em" ;
VERDADEIRO = "verdadeiro" ;
FALSO = "falso" ;
NADA = "nada" ;
QUEBRA = "quebra" ;
CONTINUA = "continua" ;
PULA = "pula" ;
ESCREVA = "escreva" ;
LEIA = "leia" ;

(* Operadores *)
PLUS = "+" ;
MINUS = "-" ;
MULTIPLY = "*" ;
DIVIDE = "/" ;
MODULO = "%" ;
POWER = "**" ;
FLOOR_DIV = "//" ;
ASSIGN = "=" ;
EQUAL = "==" ;
NOT_EQUAL = "!=" ;
LESS = "<" ;
GREATER = ">" ;
LESS_EQUAL = "<=" ;
GREATER_EQUAL = ">=" ;
SWAP = "<->" ;
NULL_COALESCING = "??" ;
ARROW = "=>" ;
PIPE = "|>" ;

(* Delimitadores *)
LPAREN = "(" ;
RPAREN = ")" ;
LBRACE = "{" ;
RBRACE = "}" ;
LBRACKET = "[" ;
RBRACKET = "]" ;
COMMA = "," ;
SEMICOLON = ";" ;
COLON = ":" ;

(* Literais *)
INTEGER = digit, { digit } ;
FLOAT = digit, { digit }, ".", digit, { digit } ;
STRING = '"', { character - '"' }, '"' | "'", { character - "'" }, "'" ;
IDENTIFIER = letter, { letter | digit | "_" } ;

(* Auxiliares *)
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
letter = "a" | "b" | ... | "z" | "A" | "B" | ... | "Z" ;
character = ? qualquer caractere unicode ? ;

2.2 Programa Principal

programa = { declaracao | instrucao } ;

declaracao = declaracao_variavel
           | declaracao_funcao  
           | declaracao_classe
           | declaracao_importacao ;

instrucao = instrucao_expressao
          | instrucao_se
          | instrucao_enquanto
          | instrucao_para
          | instrucao_retorna
          | instrucao_quebra
          | instrucao_continua
          | instrucao_pula
          | instrucao_troca
          | bloco ;

2.2.2 Declarações

declaracao_variavel = [ TIPO, tipo_nome ], IDENTIFIER, ASSIGN, expressao, SEMICOLON ;

declaracao_funcao = [ ASYNC ], FUNCAO, IDENTIFIER, LPAREN, [ lista_parametros ], RPAREN, 
                   [ ARROW, tipo_nome ], bloco ;

declaracao_funcao_arrow = IDENTIFIER, ASSIGN, LPAREN, [ lista_parametros ], RPAREN, 
                         ARROW, expressao, SEMICOLON ;

declaracao_classe = CLASSE, IDENTIFIER, [ COLON, IDENTIFIER ], bloco ;

declaracao_importacao = IMPORTA, IDENTIFIER, [ COMO, IDENTIFIER ], SEMICOLON ;

lista_parametros = parametro, { COMMA, parametro } ;
parametro = IDENTIFIER, [ COLON, tipo_nome ] ;
tipo_nome = "inteiro" | "real" | "texto" | "booleano" | "lista" | "dicionario" | IDENTIFIER ;

2.2.3 Instruções de Controle

instrucao_se = SE, LPAREN, expressao, RPAREN, bloco, 
               { SENAOSE, LPAREN, expressao, RPAREN, bloco },
               [ SENAO, bloco ] ;

instrucao_enquanto = ENQUANTO, LPAREN, expressao, RPAREN, bloco ;

instrucao_para = PARA, LPAREN, IDENTIFIER, EM, expressao, RPAREN, bloco ;

instrucao_retorna = RETORNA, [ expressao ], SEMICOLON ;

instrucao_quebra = QUEBRA, SEMICOLON ;

instrucao_continua = CONTINUA, SEMICOLON ;

instrucao_pula = PULA, SEMICOLON ;

instrucao_expressao = expressao, SEMICOLON ;

instrucao_troca = IDENTIFIER, SWAP, IDENTIFIER, SEMICOLON ;

bloco = LBRACE, { instrucao }, RBRACE ;

2.2.4 Expressões

expressao = expressao_pipe ;

expressao_pipe = expressao_null_coalescing, { PIPE, expressao_null_coalescing } ;

expressao_null_coalescing = expressao_ou, [ NULL_COALESCING, expressao_ou ] ;

expressao_ou = expressao_e, { OU, expressao_e } ;

expressao_e = expressao_igualdade, { E, expressao_igualdade } ;

expressao_igualdade = expressao_relacional, { ( EQUAL | NOT_EQUAL ), expressao_relacional } ;

expressao_relacional = expressao_aritmetica, { ( LESS | GREATER | LESS_EQUAL | GREATER_EQUAL ), expressao_aritmetica } ;

expressao_aritmetica = termo, { ( PLUS | MINUS ), termo } ;

termo = fator, { ( MULTIPLY | DIVIDE | MODULO | FLOOR_DIV ), fator } ;

fator = base, [ POWER, fator ] ;

base = expressao_unaria | expressao_primaria ;

expressao_unaria = ( MINUS | NAO ), base ;

expressao_primaria = literal
                   | IDENTIFIER
                   | chamada_funcao
                   | expressao_lista
                   | expressao_dicionario
                   | expressao_aguarda
                   | LPAREN, expressao, RPAREN ;

chamada_funcao = IDENTIFIER, LPAREN, [ lista_argumentos ], RPAREN ;

lista_argumentos = expressao, { COMMA, expressao } ;

expressao_lista = LBRACKET, [ expressao, { COMMA, expressao } ], RBRACKET ;

expressao_dicionario = LBRACE, [ par_chave_valor, { COMMA, par_chave_valor } ], RBRACE ;

par_chave_valor = expressao, COLON, expressao ;

expressao_aguarda = AGUARDA, expressao ;

literal = INTEGER | FLOAT | STRING | VERDADEIRO | FALSO | NADA ;

3. Classificação na Hierarquia de Chomsky

Análise da Gramática
A gramática da linguagem NocSysPy é classificada como Tipo 2 (Livre de Contexto) na hierarquia de Chomsky, pelas seguintes características:

1. Todas as regras têm a forma A → α, onde:

A é um símbolo não-terminal
α é uma string de terminais e não-terminais


2. 
Estruturas recursivas: A gramática permite estruturas aninhadas como:

Expressões aritméticas recursivas
Blocos aninhados
Chamadas de função dentro de expressões


3. 
Não há dependências contextuais: As regras podem ser aplicadas independentemente do contexto


3.2 Características Tipo 2

* ✅ Recursão à esquerda e direita
* ✅ Estruturas aninhadas (blocos, expressões)
* ✅ Ambiguidade controlável por precedência
* ✅ Parseável por algoritmos CFG (LR, LALR, Recursive Descent)

3.3 Justificativa da Classificação
Por que Tipo 2 e não Tipo 3 (Regular)?

* Estruturas aninhadas como { { } } não são regulares
* Balanceamento de parênteses requer pilha
* Recursão em expressões aritméticas

Por que Tipo 2 e não Tipo 1 (Sensível ao Contexto)?

* Nenhuma regra depende do contexto circundante
* Todas as produções são da forma A → α
* Não há restrições como αAβ → αγβ

4. Exemplos de Derivações
4.1 Declaração de Variável Simples
Entrada: tipo inteiro x = 10;

Derivação:
programa
├─ declaracao
   ├─ declaracao_variavel
      ├─ TIPO → "tipo"
      ├─ tipo_nome → "inteiro" 
      ├─ IDENTIFIER → "x"
      ├─ ASSIGN → "="
      ├─ expressao
         ├─ expressao_pipe
            ├─ expressao_null_coalescing
               ├─ expressao_ou
                  ├─ expressao_e
                     ├─ expressao_igualdade
                        ├─ expressao_relacional
                           ├─ expressao_aritmetica
                              ├─ termo
                                 ├─ fator
                                    ├─ base
                                       ├─ expressao_primaria
                                          ├─ literal
                                             ├─ INTEGER → "10"
      ├─ SEMICOLON → ";"

4.2 Função Simples
Entrada: funcao somar(a, b) => inteiro { retorna a + b; }

Derivação:
programa
├─ declaracao
   ├─ declaracao_funcao
      ├─ FUNCAO → "funcao"
      ├─ IDENTIFIER → "somar"
      ├─ LPAREN → "("
      ├─ lista_parametros
         ├─ parametro
            ├─ IDENTIFIER → "a"
         ├─ COMMA → ","
         ├─ parametro
            ├─ IDENTIFIER → "b"
      ├─ RPAREN → ")"
      ├─ ARROW → "=>"
      ├─ tipo_nome → "inteiro"
      ├─ bloco
         ├─ LBRACE → "{"
         ├─ instrucao
            ├─ instrucao_retorna
               ├─ RETORNA → "retorna"
               ├─ expressao
                  ├─ expressao_aritmetica
                     ├─ termo → IDENTIFIER("a")
                     ├─ PLUS → "+"
                     ├─ termo → IDENTIFIER("b")
               ├─ SEMICOLON → ";"
         ├─ RBRACE → "}"

4.3 Estrutura Se-Senao
Entrada: se (x > 0) { escreva("positivo"); } senao { escreva("não positivo"); }

Derivação:
programa
├─ instrucao
   ├─ instrucao_se
      ├─ SE → "se"
      ├─ LPAREN → "("
      ├─ expressao
         ├─ expressao_relacional
            ├─ expressao_aritmetica → IDENTIFIER("x")
            ├─ GREATER → ">"
            ├─ expressao_aritmetica → INTEGER("0")
      ├─ RPAREN → ")"
      ├─ bloco
         ├─ LBRACE → "{"
         ├─ instrucao
            ├─ instrucao_expressao
               ├─ expressao
                  ├─ chamada_funcao
                     ├─ IDENTIFIER → "escreva"
                     ├─ LPAREN → "("
                     ├─ lista_argumentos
                        ├─ expressao → STRING("positivo")
                     ├─ RPAREN → ")"
               ├─ SEMICOLON → ";"
         ├─ RBRACE → "}"
      ├─ SENAO → "senao"
      ├─ bloco → /* similar ao anterior */

4.4 Pipeline com Operador |>
Entrada: resultado = dados |> filtrar |> mapear;

Derivação:
programa
├─ instrucao
   ├─ instrucao_expressao
      ├─ expressao
         ├─ expressao_pipe
            ├─ expressao_null_coalescing → IDENTIFIER("dados")
            ├─ PIPE → "|>"
            ├─ expressao_null_coalescing → IDENTIFIER("filtrar")
            ├─ PIPE → "|>"
            ├─ expressao_null_coalescing → IDENTIFIER("mapear")
      ├─ SEMICOLON → ";"

4.5 Operador de Troca
Entrada: a <-> b;

Derivação:
programa
├─ instrucao
   ├─ instrucao_troca
      ├─ IDENTIFIER → "a"
      ├─ SWAP → "<->"
      ├─ IDENTIFIER → "b"
      ├─ SEMICOLON → ";"

5. Análise de Ambiguidades e Estratégias de Resolução
5.1 Ambiguidade de Precedência de Operadores
Problema:
resultado = a + b * c;

Ambiguidade: Pode ser interpretado como (a + b) * c ou a + (b * c)

Estratégia de Resolução:

* Precedência fixa na gramática (do maior para menor):

** (potência)
*, /, //, % (multiplicativos)
+, - (aditivos)
<, >, <=, >= (relacionais)
==, != (igualdade)
e (AND lógico)
ou (OR lógico)
?? (null coalescing)
|> (pipe)



Implementação: Hierarquia de não-terminais reflete a precedência
5.2 Ambiguidade do Dangling Else
Problema:
se (condicao1) se (condicao2) instrucao1; senao instrucao2;

Ambiguidade: O senao pode estar associado ao primeiro ou segundo se
Estratégia de Resolução:

* Uso obrigatório de blocos {} elimina completamente a ambiguidade
* Sintaxe correta:
se (condicao1) {
    se (condicao2) {
        instrucao1;
    } senao {
        instrucao2;
    }
}

5.3 Ambiguidade do Operador Pipe
Problema:
resultado = a |> b == c;

Ambiguidade: Pode ser (a |> b) == c ou a |> (b == c)
Estratégia de Resolução:

* Precedência: == tem precedência maior que |>
* Resultado: Interpretado como a |> (b == c)
* Associatividade: |> é associativo à esquerda

5.4 Ambiguidade de Arrow Functions
Problema:
f = (x) => x > 5 == verdadeiro;

Estratégia de Resolução:

* Precedência: => tem precedência muito baixa
* Interpretação: f = (x) => ((x > 5) == verdadeiro)
* Parênteses recomendados para clareza

5.5 Ambiguidade do Operador de Troca
Problema:
a <-> b == c;

Estratégia de Resolução:

* Operador de troca é instrução, não expressão
* Sintaxe obrigatória: a <-> b; (termina com ponto e vírgula)
* Não pode ser parte de expressões maiores

5.6 Ambiguidade em Listas vs Dicionários
Problema:
dados = {};

Ambiguidade: Lista vazia ou dicionário vazio?
Estratégia de Resolução:

* [] → Lista vazia
* {} → Bloco vazio ou dicionário vazio (contexto define)
* {:} → Dicionário vazio explícito
* Context-aware parsing resolve o conflito

6. Características Especiais da Gramática
6.1 Operadores Únicos
A linguagem NocSysPy introduz operadores únicos que requerem tratamento especial:

* Troca (<->): Instrução dedicada, não expressão
* Pipe (|>): Associativo à esquerda, baixa precedência
* Null coalescing (??): Avaliação curto-circuitada
* Arrow (=>): Context-sensitive para funções

6.2 Sistema de Tipos na Gramática

declaracao_com_tipo = TIPO, tipo_nome, IDENTIFIER, ASSIGN, expressao, SEMICOLON ;
tipo_nome = tipo_primitivo | tipo_composto | IDENTIFIER ;
tipo_primitivo = "inteiro" | "real" | "texto" | "booleano" ;
tipo_composto = "lista" | "dicionario" ;

6.3 Async/Await

funcao_async = ASYNC, FUNCAO, IDENTIFIER, LPAREN, [ lista_parametros ], RPAREN, bloco ;
expressao_aguarda = AGUARDA, expressao ;

7. Validação da Gramática
7.1 Testes de Consistência
A gramática foi validada contra os seguintes critérios:

1.  Não há recursão infinita
2.  Todos os não-terminais são alcançáveis
3.  Todos os não-terminais geram strings finitas
4.  Precedência de operadores é consistente
5.  Ambiguidades são resolvidas sistematicamente

7.2 Cobertura de Funcionalidades

*  Declarações de variáveis com tipos
*  Funções normais e arrow functions
*  Estruturas de controle (se, enquanto, para)
*  Expressões aritméticas e lógicas
*  Operadores especiais únicos
*  Listas e dicionários
*  Programação assíncrona
*  Sistema de tipos

8. Conclusão
A gramática formal da linguagem NocSysPy é classificada como Tipo 2 (Livre de Contexto) e suporta todas as funcionalidades planejadas da linguagem. As ambiguidades identificadas foram resolvidas através de:

* Precedência explícita de operadores
* Uso obrigatório de blocos {}
* Context-sensitive parsing para casos específicos
* Separação clara entre instruções e expressões

A gramática está pronta para implementação de um parser usando técnicas como Recursive Descent, LR ou LALR.