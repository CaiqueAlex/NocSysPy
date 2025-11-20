# 📘 Gramática da NocSysPy + Conjuntos FIRST e FOLLOW

## 1. Gramática (BNF)

Símbolo inicial: `<Program>`

```bnf
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

2. Conjuntos FIRST
Lembrando

* FIRST(X): conjunto de terminais que podem iniciar alguma cadeia derivada de X.
* Se X ⇒* ε, então ε ∈ FIRST(X).

A seguir, FIRST para cada não-terminal da gramática.

2.1. FIRST dos não-terminais de topo
FIRST(Program)
<Program> ::= <DeclList> "EOF"

* FIRST(Program) = FIRST(DeclList)
* como ε ∈ FIRST(DeclList), então FIRST(Program) = FIRST(DeclList) ∪ {"EOF"}

Vamos achar FIRST(DeclList) primeiro.

FIRST(DeclList)
<DeclList> ::= <Decl> <DeclList>
             | ε

* Pode derivar ε.
* Ou começa por <Decl>.

Então:

* FIRST(DeclList) = FIRST(Decl) ∪ { ε }

Vamos ver FIRST(Decl).

FIRST(Decl)
<Decl> ::= <VarDecl>
         | <FuncDecl>

* <VarDecl> ::= "var" ...
* <FuncDecl> ::= "func" ...

Então:

* FIRST(VarDecl) = { "var" }
* FIRST(FuncDecl) = { "func" }

Logo:

* FIRST(Decl) = { "var", "func" }

Voltando:

* FIRST(DeclList) = { "var", "func", ε }

Agora:

* FIRST(Program) = FIRST(DeclList) ∪ { "EOF" } = { "var", "func", ε, "EOF" }

Em termos práticos (para parsing), consideramos que a entrada sempre termina em EOF, então os inícios reais de Program são "var", "func" ou diretamente EOF (programa vazio).

2.2. FIRST de declarações e tipos
FIRST(VarDecl)

<VarDecl> ::= "var" <Type> IDENTIFIER <VarDeclTail> ";"

* Começa sempre por "var".

FIRST(VarDecl) = { "var" }

FIRST(VarDeclTail)

<VarDeclTail> ::= "," IDENTIFIER <VarDeclTail>
                | ε
* Produz "," ou ε.


FIRST(VarDeclTail) = { ",", ε }


FIRST(FuncDecl)

<FuncDecl> ::= "func" IDENTIFIER "(" <ParamListOpt> ")" <Block>

* Começa por "func".


FIRST(FuncDecl) = { "func" }


FIRST(ParamListOpt)

<ParamListOpt> ::= <ParamList>
                 | ε

* Pode ser ε
* Ou começar como ParamList.

Vamos ver FIRST(ParamList):

<ParamList> ::= <Type> IDENTIFIER <ParamTail>

Type é um dos 4 tipos básicos:

<Type> ::= "int"
         | "float"
         | "string"
         | "bool"

Logo:

FIRST(ParamList) = FIRST(Type) = { "int", "float", "string", "bool" }

Portanto:

FIRST(ParamListOpt) = { "int", "float", "string", "bool", ε }


FIRST(ParamTail)

<ParamTail> ::= "," <Type> IDENTIFIER <ParamTail>
              | ε

FIRST(ParamTail) = { ",", ε }


2.3. FIRST de blocos e statements
FIRST(Block)

<Block> ::= "{" <StmtList> "}"

RST(Block) = { "{" }


FIRST(StmtList)

<StmtList> ::= <Stmt> <StmtList>
             | ε

* Pode ser ε.
* Ou começa com FIRST(Stmt).

Vamos achar FIRST(Stmt):
<Stmt> ::= <AssignStmt>
         | <IfStmt>
         | <WhileStmt>
         | <ReturnStmt>
         | <PrintStmt>
         | <Block>
         | ";"

* FIRST(AssignStmt) começa com IDENTIFIER.
* FIRST(IfStmt) = { "if" }
* FIRST(WhileStmt) = { "while" }
* FIRST(ReturnStmt) = { "return" }
* FIRST(PrintStmt) = { "print" }
* FIRST(Block) = { "{" }
* O ";" é terminal.

Logo:

FIRST(Stmt) = { IDENTIFIER, "if", "while", "return", "print", "{", ";" }

Portanto:

FIRST(StmtList) = FIRST(Stmt) ∪ { ε }
= { IDENTIFIER, "if", "while", "return", "print", "{", ";", ε }


FIRST(AssignStmt)

<AssignStmt> ::= IDENTIFIER "=" <Expr> ";"

FIRST(AssignStmt) = { IDENTIFIER }


FIRST(IfStmt)
<IfStmt> ::= "if" "(" <Expr> ")" <Stmt> <ElseOpt>

FIRST(IfStmt) = { "if" }


FIRST(ElseOpt)
<ElseOpt> ::= "else" <Stmt>
            | ε

FIRST(ElseOpt) = { "else", ε }


FIRST(WhileStmt)
<WhileStmt> ::= "while" "(" <Expr> ")" <Stmt>

FIRST(WhileStmt) = { "while" }


FIRST(ReturnStmt)
<ReturnStmt> ::= "return" <ExprOpt> ";"

FIRST(ReturnStmt) = { "return" }


FIRST(ExprOpt)
<ExprOpt> ::= <Expr>
            | ε

Vamos ver FIRST(Expr):
<Expr> ::= <RelExpr>
<RelExpr> ::= <AddExpr> <RelExprTail>
<AddExpr> ::= <Term> <AddExprTail>
<Term> ::= <Factor> <TermTail>
<Factor> ::= IDENTIFIER
           | INTEGER
           | FLOAT
           | STRING
           | "(" <Expr> ")"

Logo:

FIRST(Factor) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }

E isso se propaga:

* FIRST(Term) = FIRST(Factor)
* FIRST(AddExpr) = FIRST(Term)
* FIRST(RelExpr) = FIRST(AddExpr)
* FIRST(Expr) = FIRST(RelExpr)

Portanto:

FIRST(Expr) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }

Logo:

FIRST(ExprOpt) = FIRST(Expr) ∪ { ε }
= { IDENTIFIER, INTEGER, FLOAT, STRING, "(", ε }


FIRST(PrintStmt)
<PrintStmt> ::= "print" "(" <Expr> ")" ";"

FIRST(PrintStmt) = { "print" }


2.4. FIRST de expressões
Reforçando:
<Expr>         ::= <RelExpr>

<RelExpr>      ::= <AddExpr> <RelExprTail>

<RelExprTail>  ::= <RelOp> <AddExpr> <RelExprTail>
                 | ε

<RelOp>        ::= "=="
                 | "<"
                 | "<="
                 | ">"
                 | ">="

<AddExpr>      ::= <Term> <AddExprTail>

<AddExprTail>  ::= <AddOp> <Term> <AddExprTail>
                 | ε

<AddOp>        ::= "+"
                 | "-"

<Term>         ::= <Factor> <TermTail>

<TermTail>     ::= <MulOp> <Factor> <TermTail>
                 | ε

<MulOp>        ::= "*"
                 | "/"

<Factor>       ::= IDENTIFIER
                 | INTEGER
                 | FLOAT
                 | STRING
                 | "(" <Expr> ")"

Já vimos:

FIRST(Factor) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }

Propagando:

* FIRST(Term) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }
* FIRST(AddExpr) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }
* FIRST(RelExpr) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }
* FIRST(Expr) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }

Demais:

FIRST(RelExprTail) = FIRST(RelOp) ∪ { ε }
FIRST(RelOp) = { "==", "<", "<=", ">", ">=" }


FIRST(AddExprTail) = FIRST(AddOp) ∪ { ε }
FIRST(AddOp) = { "+", "-" }


FIRST(TermTail) = FIRST(MulOp) ∪ { ε }
FIRST(MulOp) = { "*", "/" }


3. Conjuntos FOLLOW
Lembrando:

* FOLLOW(A): conjunto de terminais que podem aparecer logo após A em alguma derivação.
* Para o símbolo inicial S, EOF ∈ FOLLOW(S).

Vou listar FOLLOW por não-terminal.
Quando eu colocar “(vem de regra tal)”, é a justificativa informal.

3.1. FOLLOW(Program)
<Program> ::= <DeclList> "EOF"

* Após <Program> não vem nada, mas por definição:
* FOLLOW(Program) = { EOF }


3.2. FOLLOW(DeclList)
Em:

<Program>  ::= <DeclList> "EOF"

* Depois de <DeclList> vem "EOF" ⇒ "EOF" ∈ FOLLOW(DeclList)

Em:
<DeclList> ::= <Decl> <DeclList>
             | ε

* Após o segundo <DeclList> não há nada ⇒ FOLLOW(DeclList) ⊆ FOLLOW(DeclList) (nada novo)
* Após o primeiro <DeclList> também nada (regra recursiva à direita já considerada).

Logo:

FOLLOW(DeclList) = { "EOF" }


3.3. FOLLOW(Decl)
De:
<DeclList> ::= <Decl> <DeclList>

* Depois de <Decl> vem <DeclList>.
* Tudo de FIRST(DeclList) exceto ε entra em FOLLOW(Decl):

FIRST(DeclList) = { "var", "func", ε }
então { "var", "func" } ⊆ FOLLOW(Decl)


* Como <DeclList> pode ir para ε, também adicionamos FOLLOW(DeclList) a FOLLOW(Decl):

FOLLOW(DeclList) = { "EOF" }



Logo:

FOLLOW(Decl) = { "var", "func", "EOF" }


3.4. FOLLOW(VarDecl), FOLLOW(VarDeclTail)
De:
<Decl> ::= <VarDecl> | <FuncDecl>

* FOLLOW(VarDecl) inclui FOLLOW(Decl) = { "var", "func", "EOF" }

Logo:

FOLLOW(VarDecl) = { "var", "func", "EOF" }

De:
<VarDecl> ::= "var" <Type> IDENTIFIER <VarDeclTail> ";"
* Após <VarDeclTail> vem ";" ⇒ ";" ∈ FOLLOW(VarDeclTail)

Em:
<VarDeclTail> ::= "," IDENTIFIER <VarDeclTail>
                | ε

* A recursão à direita não acrescenta novos símbolos (depois do segundo <VarDeclTail> não há nada, então FOLLOW dele é o mesmo).

Logo:

FOLLOW(VarDeclTail) = { ";" }

3.5. FOLLOW(FuncDecl)
De:
<Decl> ::= <VarDecl> | <FuncDecl>

* FOLLOW(FuncDecl) inclui FOLLOW(Decl) = { "var", "func", "EOF" }

Logo:

FOLLOW(FuncDecl) = { "var", "func", "EOF" }


3.6. FOLLOW(ParamListOpt), ParamList, ParamTail, Type
De:
<FuncDecl> ::= "func" IDENTIFIER "(" <ParamListOpt> ")" <Block>

* Depois de <ParamListOpt> vem ")" ⇒ ")" ∈ FOLLOW(ParamListOpt)

Como:
<ParamListOpt> ::= <ParamList> | ε

* FOLLOW(ParamList) inclui FOLLOW(ParamListOpt) = { ")" }

Logo:

FOLLOW(ParamListOpt) = { ")" }
FOLLOW(ParamList)    = { ")" }

De:
<ParamList> ::= <Type> IDENTIFIER <ParamTail>

* Depois de <ParamTail> não há nada ⇒ FOLLOW(ParamTail) inclui FOLLOW(ParamList).
* Então FOLLOW(ParamTail) = { ")" }.

Na recursão:
<ParamTail> ::= "," <Type> IDENTIFIER <ParamTail>
              | ε

* O segundo <ParamTail> já tem FOLLOW herdado.

Logo:

FOLLOW(ParamTail) = { ")" }

Sobre <Type>:

* Aparece em <VarDecl>: "var" <Type> IDENTIFIER ...

Depois de <Type> vem IDENTIFIER ⇒ FOLLOW(Type) ⊇ { IDENTIFIER }


* Em <ParamList>: <Type> IDENTIFIER ...

também seguida de IDENTIFIER.



Não há ocorrências de <Type> em final de produção, então:

FOLLOW(Type) = { IDENTIFIER }


3.7. FOLLOW(Block), StmtList, Stmt
De:
<FuncDecl> ::= "func" IDENTIFIER "(" <ParamListOpt> ")" <Block>

* Após <Block> não há nada ⇒ FOLLOW(Block) ⊇ FOLLOW(FuncDecl) = { "var", "func", "EOF" }

De:
<Block> ::= "{" <StmtList> "}"

* Depois de <StmtList> vem "}" ⇒ "}" ∈ FOLLOW(StmtList)

De:
<StmtList> ::= <Stmt> <StmtList>
             | ε

* Após <Stmt> vem <StmtList>:

Primeiro, FIRST(StmtList) \ {ε} vai para FOLLOW(Stmt)

FIRST(StmtList) = { IDENTIFIER, "if", "while", "return", "print", "{", ";", ε }
então { IDENTIFIER, "if", "while", "return", "print", "{", ";" } ⊆ FOLLOW(Stmt)


Como StmtList pode ir para ε, FOLLOW(StmtList) também vai para FOLLOW(Stmt):

FOLLOW(StmtList) = { "}" }





Portanto:

FOLLOW(StmtList) = { "}" }
FOLLOW(Stmt) ⊇ { IDENTIFIER, "if", "while", "return", "print", "{", ";", "}" }

Mas Stmt também aparece em outros lugares (IfStmt, WhileStmt, etc.), vamos somar tudo:
FOLLOW(Block) mais detalhado
Blocks aparecem em:
<FuncDecl> ::= ... <Block>
<Stmt>     ::= <Block> | ...
<IfStmt>   ::= "if" "(" <Expr> ")" <Stmt> <ElseOpt>
<ElseOpt>  ::= "else" <Stmt> | ε
<WhileStmt>::= "while" "(" <Expr> ")" <Stmt>

* Em <Stmt> ::= <Block> | ..., FOLLOW(Block) inclui FOLLOW(Stmt).
* Em FuncDecl, FOLLOW(Block) inclui FOLLOW(FuncDecl) = { "var", "func", "EOF" }.

Ainda não fechamos FOLLOW(Stmt), então mantenha em mente que:

FOLLOW(Block) = FOLLOW(Stmt) ∪ { "var", "func", "EOF" }

Voltamos a FOLLOW(Stmt) depois de computar os outros contextos.

3.8. FOLLOW de cada tipo de Stmt
FOLLOW(AssignStmt)
De:
<Stmt> ::= <AssignStmt> | ...
* FOLLOW(AssignStmt) inclui FOLLOW(Stmt).

FOLLOW(IfStmt)
De:
<Stmt> ::= <IfStmt> | ...

* FOLLOW(IfStmt) inclui FOLLOW(Stmt).

Em:
<IfStmt> ::= "if" "(" <Expr> ")" <Stmt> <ElseOpt>

* Após o <Stmt> interno vem <ElseOpt>.

FIRST(ElseOpt) \ {ε} = { "else" } ⊆ FOLLOW(Stmt) (interno ao If).
Como ElseOpt pode ir para ε, FOLLOW(IfStmt) também vai para FOLLOW(desse Stmt interno).
E FOLLOW(IfStmt) ⊆ FOLLOW(Stmt) (porque aparece no nível de <Stmt>).



No fim, isso fecha um sistema onde:

FOLLOW(Stmt interno em If) = FOLLOW(IfStmt) ∪ { "else" }

mas, como ambos acabam sendo subconjuntos de FOLLOW(Stmt) global, no conjunto final global de FOLLOW(Stmt) teremos "else" também.
FOLLOW(ElseOpt)
De:
<IfStmt> ::= "if" "(" <Expr> ")" <Stmt> <ElseOpt>

* Após <ElseOpt> não há nada ⇒ FOLLOW(ElseOpt) ⊇ FOLLOW(IfStmt)
* E FOLLOW(IfStmt) ⊆ FOLLOW(Stmt) (pois IfStmt aparece em <Stmt>)

Então:

FOLLOW(ElseOpt) = FOLLOW(Stmt)  (em termos de conjunto final)

FOLLOW(WhileStmt)
De:
<Stmt> ::= <WhileStmt> | ...

* FOLLOW(WhileStmt) inclui FOLLOW(Stmt).

FOLLOW(ReturnStmt)
Idem:

FOLLOW(ReturnStmt) inclui FOLLOW(Stmt)

FOLLOW(PrintStmt)
Idem:

FOLLOW(PrintStmt) inclui FOLLOW(Stmt)

Em resumo: todos os tipos concretos de Stmt herdam FOLLOW(Stmt).
FOLLOW(Stmt) já vimos que tem:

* { IDENTIFIER, "if", "while", "return", "print", "{", ";", "}" }
* e, via contextos maiores (DeclList/Block), isso se encaixa bem com os tokens que podem aparecer a seguir em blocos e no topo do programa.


3.9. FOLLOW(Expr), RelExpr, AddExpr, Term, Factor, etc.
Começando por onde Expr aparece:

* Em IfStmt: "if" "(" <Expr> ")" ...

Depois de <Expr> vem ")" ⇒ ")" ∈ FOLLOW(Expr)


* Em WhileStmt: "while" "(" <Expr> ")" ...

Também ")" ∈ FOLLOW(Expr)


* Em AssignStmt: IDENTIFIER "=" <Expr> ";"

Depois vem ";" ⇒ ";" ∈ FOLLOW(Expr)


* Em ReturnStmt: "return" <ExprOpt> ";" e dentro de ExprOpt, Expr vem antes de ";".

";" ∈ FOLLOW(Expr)


* Em PrintStmt: "print" "(" <Expr> ")" ";"

Depois ")" ⇒ ")" ∈ FOLLOW(Expr)


* Em Factor: "(" <Expr> ")" ⇒ ")" ∈ FOLLOW(Expr) (já temos).

Logo:

FOLLOW(Expr) = { ")", ";" }

Agora, <Expr> ::= <RelExpr>:

* FOLLOW(RelExpr) inclui FOLLOW(Expr) = { ")", ";" }

E:
<RelExpr> ::= <AddExpr> <RelExprTail>

De <RelExprTail>:
<RelExprTail> ::= <RelOp> <AddExpr> <RelExprTail>
                | ε

* Quando RelExprTail ⇒ ε, FOLLOW(RelExprTail) = FOLLOW(RelExpr) = { ")", ";" }
* FIRST(RelExprTail) = { "==", "<", "<=", ">", ">=", ε }
* Então FOLLOW(AddExpr) inclui (FIRST(RelExprTail){ε}) ∪ FOLLOW(RelExpr)
= { "==", "<", "<=", ">", ">=", ")", ";" }


FOLLOW(AddExpr) = { "==", "<", "<=", ">", ">=", ")", ";" }

E:
<AddExpr> ::= <Term> <AddExprTail>
<AddExprTail> ::= <AddOp> <Term> <AddExprTail> | ε

* FIRST(AddExprTail) = { "+", "-", ε }
* Logo FOLLOW(Term) inclui:

{ "+", "-" } (de FIRST(AddExprTail){ε})
∪ FOLLOW(AddExpr) quando AddExprTail ⇒ ε



Portanto:

FOLLOW(Term) = { "+", "-", "==", "<", "<=", ">", ">=", ")", ";" }

Agora:
<Term>     ::= <Factor> <TermTail>
<TermTail> ::= <MulOp> <Factor> <TermTail> | ε

* FIRST(TermTail) = { "*", "/", ε }
* FOLLOW(Factor) inclui:

{ "*", "/" } (de FIRST(TermTail){ε})
∪ FOLLOW(Term) quando TermTail ⇒ ε



Logo:

FOLLOW(Factor) = { "*", "/", "+", "-", "==", "<", "<=", ">", ">=", ")", ";" }

Demais FOLLOW:

* FOLLOW(RelExprTail) = FOLLOW(RelExpr) = { ")", ";" }
* FOLLOW(AddExprTail) = FOLLOW(AddExpr) = { "==", "<", "<=", ">", ">=", ")", ";" }
* FOLLOW(MulOp), AddOp, RelOp são irrelevantes para análise LL(1), pois são terminais.


4. A gramática é LL(1)?
Critérios principais
Uma gramática é LL(1) se, para cada não-terminal A:

1. As produções alternativas de A têm primeiros símbolos terminais distintos, ou:
2. Se alguma produção produz ε, então:

FIRST(outra produção) ∩ FOLLOW(A) = ∅



Vamos checar os pontos “suspeitos”:
4.1. Não-terminais com mais de uma alternativa

* 
<DeclList> ::= <Decl> <DeclList> | ε

FIRST(DeclList) = { "var", "func", ε }
FOLLOW(DeclList) = { "EOF" }
FIRST(Decl) = { "var", "func" }
FIRST(Decl) ∩ FOLLOW(DeclList) = ∅ → ok.


* 
<Decl> ::= <VarDecl> | <FuncDecl>

FIRST(VarDecl) = { "var" }
FIRST(FuncDecl) = { "func" }
Disjuntos → ok.


* 
<VarDeclTail> ::= "," IDENTIFIER <VarDeclTail> | ε

FIRST = { ",", ε }
FOLLOW(VarDeclTail) = { ";" }
{ "," } ∩ { ";" } = ∅ → ok.


* 
<ParamListOpt> ::= <ParamList> | ε

FIRST(ParamList) = { "int", "float", "string", "bool" }
FOLLOW(ParamListOpt) = { ")" }
FIRST(ParamList) ∩ FOLLOW(ParamListOpt) = ∅ → ok.


* 
<ParamTail> ::= "," <Type> IDENTIFIER <ParamTail> | ε

FIRST = { ",", ε }, FOLLOW(ParamTail) = { ")" }
{ "," } ∩ { ")" } = ∅ → ok.


* 
<StmtList> ::= <Stmt> <StmtList> | ε

FIRST(Stmt) = { IDENTIFIER, "if", "while", "return", "print", "{", ";" }
FOLLOW(StmtList) = { "}" }
FIRST(Stmt) ∩ FOLLOW(StmtList) = ∅ → ok.


* 
<Stmt> ::= <AssignStmt> | <IfStmt> | <WhileStmt> | <ReturnStmt> | <PrintStmt> | <Block> | ";"
FIRST de cada alternativa:

AssignStmt: { IDENTIFIER }
IfStmt: { "if" }
WhileStmt: { "while" }
ReturnStmt: { "return" }
PrintStmt: { "print" }
Block: { "{" }
";" literal: { ";" }

Todos os conjuntos são disjuntos → não há ambiguidade → ok.

* 
<ElseOpt> ::= "else" <Stmt> | ε

FIRST(ElseOpt) = { "else", ε }
FOLLOW(ElseOpt) = FOLLOW(Stmt) (em blocos/if/while/etc).
FIRST(“else”-produção) = { "else" }
{ "else" } ∩ FOLLOW(ElseOpt) = pode conter “else”?

FOLLOW(ElseOpt) é conjunto de símbolos que podem aparecer depois do if/stmt, como IDENTIFIER, if, while, return, print, {, ;, }.
“else” não aparece em FOLLOW(Stmt); só aparece como início de uma produção de ElseOpt.


Então FIRST(“else”-prod) ∩ FOLLOW(ElseOpt) = ∅ → ok.


* 
<ExprOpt> ::= <Expr> | ε

FIRST(Expr) = { IDENTIFIER, INTEGER, FLOAT, STRING, "(" }
FOLLOW(ExprOpt) (vem de return <ExprOpt> ";") = { ";" }
FIRST(Expr) ∩ FOLLOW(ExprOpt) = ∅ → ok.


* 
<RelExprTail> ::= <RelOp> <AddExpr> <RelExprTail> | ε

FIRST = { "==", "<", "<=", ">", ">=", ε }
FOLLOW(RelExprTail) = FOLLOW(RelExpr) = { ")", ";" }
{ "==", "<", "<=", ">", ">=" } ∩ { ")", ";" } = ∅ → ok.


* 
<AddExprTail> ::= <AddOp> <Term> <AddExprTail> | ε

FIRST = { "+", "-", ε }, FOLLOW(AddExprTail) = FOLLOW(AddExpr) = { "==", "<", "<=", ">", ">=", ")", ";" }
{ "+", "-" } ∩ { "==", "<", "<=", ">", ">=", ")", ";" } = ∅ → ok.


* 
<TermTail> ::= <MulOp> <Factor> <TermTail> | ε

FIRST = { "*", "/", ε }, FOLLOW(TermTail) = FOLLOW(Term) = { "+", "-", "==", "<", "<=", ">", ">=", ")", ";" }
{ "*", "/" } ∩ { "+", "-", "==", "<", "<=", ">", ">=", ")", ";" } = ∅ → ok.



4.2. Conclusão

* Não há recursão à esquerda.
* As alternativas de cada não-terminal têm FIRST disjuntos, ou quando existe produção ε, FIRST(outros) ∩ FOLLOW(não-terminal) = ∅.
* Não há conflitos FIRST/FIRST nem FIRST/FOLLOW.

Logo, a gramática é LL(1).
Isso significa que:

* É possível construir um analisador sintático preditivo (top-down) com 1 símbolo de lookahead.
* A tabela LL(1) não terá conflitos (nenhuma célula com mais de uma produção).