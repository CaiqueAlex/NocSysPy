# 📘 Gramática Formal da Linguagem NocSysPy

## 1. Definição Formal

Seja a gramática:

\[
G = (V, \Sigma, P, S)
\]

onde:

### 1.1. Conjunto de variáveis (não-terminais) \(V\)

\[
V = \{
Program, 
DeclList, Decl,
VarDecl, FuncDecl, 
Type, 
ParamListOpt, ParamList, ParamTail,
Block, StmtList, Stmt,
AssignStmt, IfStmt, WhileStmt, ReturnStmt, PrintStmt,
Expr, ExprTail, Term, TermTail, Factor,
RelExpr, RelOp,
AddOp, MulOp
\}
\]

### 1.2. Conjunto de terminais \(\Sigma\)

Palavras reservadas, símbolos e tokens léxicos:

\[
\Sigma = \{
\text{"func"}, \text{"var"},
\text{"if"}, \text{"else"},
\text{"while"},
\text{"return"},
\text{"print"},
\text{"int"}, \text{"float"}, \text{"string"}, \text{"bool"},
"(", ")", "{", "}", ",", ";",
"=", "==", "<", "<=", ">", ">=",
"+", "-", "*", "/",
\text{IDENTIFIER}, \text{INTEGER}, \text{FLOAT}, \text{STRING}
\}
\]

> Observação: `IDENTIFIER`, `INTEGER`, `FLOAT` e `STRING` são os tokens produzidos pelo analisador léxico.

### 1.3. Símbolo inicial \(S\)

\[
S = Program
\]

---

## 2. Gramática em EBNF

Abaixo, a gramática da NocSysPy em **EBNF**, adequada para um parser recursivo descendente.

```ebnf
Program       = { Decl } EOF ;

Decl          = VarDecl
              | FuncDecl ;

VarDecl       = "var" Type IDENTIFIER ";"
              | "var" Type IDENTIFIER { "," IDENTIFIER } ";" ;

FuncDecl      = "func" IDENTIFIER "(" [ ParamList ] ")" Block ;

ParamList     = Type IDENTIFIER { "," Type IDENTIFIER } ;

Type          = "int" | "float" | "string" | "bool" ;

Block         = "{" { Stmt } "}" ;

Stmt          = AssignStmt
              | IfStmt
              | WhileStmt
              | ReturnStmt
              | PrintStmt
              | Block
              | ";" ;           (* statement vazio *)

AssignStmt    = IDENTIFIER "=" Expr ";" ;

IfStmt        = "if" "(" Expr ")" Stmt [ "else" Stmt ] ;

WhileStmt     = "while" "(" Expr ")" Stmt ;

ReturnStmt    = "return" [ Expr ] ";" ;

PrintStmt     = "print" "(" Expr ")" ";" ;


(* Expressões: suportam operações aritméticas e relacionais *)

Expr          = RelExpr ;

RelExpr       = AddExpr [ RelOp AddExpr ] ;

RelOp         = "==" | "<" | "<=" | ">" | ">=" ;

AddExpr       = Term { AddOp Term } ;

AddOp         = "+" | "-" ;

Term          = Factor { MulOp Factor } ;

MulOp         = "*" | "/" ;

Factor        = IDENTIFIER
              | INTEGER
              | FLOAT
              | STRING
              | "(" Expr ")" ;

3. Gramática em BNF
A mesma gramática, reescrita em BNF puro, com introdução explícita de símbolos auxiliares.

<Program>        ::= <DeclList> "EOF"

<DeclList>       ::= <Decl> <DeclList>
                   | ε

<Decl>           ::= <VarDecl>
                   | <FuncDecl>


<VarDecl>        ::= "var" <Type> IDENTIFIER <VarDeclTail> ";"

<VarDeclTail>    ::= "," IDENTIFIER <VarDeclTail>
                   | ε


<FuncDecl>       ::= "func" IDENTIFIER "(" <ParamListOpt> ")" <Block>

<ParamListOpt>   ::= <ParamList>
                   | ε

<ParamList>      ::= <Type> IDENTIFIER <ParamTail>

<ParamTail>      ::= "," <Type> IDENTIFIER <ParamTail>
                   | ε


<Type>           ::= "int"
                   | "float"
                   | "string"
                   | "bool"


<Block>          ::= "{" <StmtList> "}"

<StmtList>       ::= <Stmt> <StmtList>
                   | ε


<Stmt>           ::= <AssignStmt>
                   | <IfStmt>
                   | <WhileStmt>
                   | <ReturnStmt>
                   | <PrintStmt>
                   | <Block>
                   | ";"


<AssignStmt>     ::= IDENTIFIER "=" <Expr> ";"


<IfStmt>         ::= "if" "(" <Expr> ")" <Stmt> <ElseOpt>

<ElseOpt>        ::= "else" <Stmt>
                   | ε


<WhileStmt>      ::= "while" "(" <Expr> ")" <Stmt>


<ReturnStmt>     ::= "return" <ExprOpt> ";"

<ExprOpt>        ::= <Expr>
                   | ε


<PrintStmt>      ::= "print" "(" <Expr> ")" ";"


(* Expressões *)

<Expr>           ::= <RelExpr>

<RelExpr>        ::= <AddExpr> <RelExprTail>

<RelExprTail>    ::= <RelOp> <AddExpr> <RelExprTail>
                   | ε

<RelOp>          ::= "=="
                   | "<"
                   | "<="
                   | ">"
                   | ">="


<AddExpr>        ::= <Term> <AddExprTail>

<AddExprTail>    ::= <AddOp> <Term> <AddExprTail>
                   | ε

<AddOp>          ::= "+"
                   | "-"


<Term>           ::= <Factor> <TermTail>

<TermTail>       ::= <MulOp> <Factor> <TermTail>
                   | ε

<MulOp>          ::= "*"
                   | "/"


<Factor>         ::= IDENTIFIER
                   | INTEGER
                   | FLOAT
                   | STRING
                   | "(" <Expr> ")"

4. Observações

1. 
Não há classes, arrays ou new, ao contrário de MicroJava.
A linguagem é propositalmente mais simples, focada em:

declarações de variáveis,
funções,
controle de fluxo (if, else, while),
expressões aritméticas e relacionais,
operações de impressão (print).


2. 
A gramática foi escrita:

sem recursão à esquerda, facilitando um parser recursivo descendente;
de forma compatível com o conjunto de tokens já definidos pelo analisador léxico (NocSysPy).


3. 
O símbolo EOF pode ser tratado como:

terminal especial gerado pelo lexer, ou
implícito (fim do arquivo) na implementação do parser.