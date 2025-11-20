# src/parser/ast.py
from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional, Union
from src.lexer.lexer import Token


# ================================
# 1. Nó base da AST
# ================================
class ASTNode:
    """Nó base da AST. Guarda opcionalmente o token de origem."""
    def __init__(self, token: Optional[Token] = None):
        self.token = token


# ================================
# 2. Nós de alto nível (programa, declarações)
# ================================
@dataclass
class Program(ASTNode):
    declarations: List[ASTNode]


@dataclass
class VarDecl(ASTNode):
    var_token: Token        # token 'var'
    name: Token             # IDENTIFIER
    init_expr: Optional['Expr']  # expressão de inicialização (pode ser None no futuro)


@dataclass
class Param(ASTNode):
    """Parâmetro de função: só nome, sem tipo explícito."""
    name: Token  # IDENTIFIER


@dataclass
class FuncDecl(ASTNode):
    func_token: Token           # token 'func'
    name: Token                 # IDENTIFIER
    params: List[Param]         # lista de parâmetros (somente nomes)
    body: 'Block'


# ================================
# 3. Comandos (statements)
# ================================
@dataclass
class Block(ASTNode):
    statements: List[ASTNode]


@dataclass
class AssignStmt(ASTNode):
    target: 'Expr'
    value: 'Expr'


@dataclass
class IfStmt(ASTNode):
    condition: 'Expr'
    then_branch: Block
    else_branch: Optional[Block]


@dataclass
class WhileStmt(ASTNode):
    condition: 'Expr'
    body: Block


@dataclass
class ReturnStmt(ASTNode):
    value: Optional['Expr']


@dataclass
class PrintStmt(ASTNode):
    value: 'Expr'


@dataclass
class ExprStmt(ASTNode):
    """Expressão sozinha terminada por ';' (por exemplo: chamada de função)."""
    expr: 'Expr'


# ================================
# 4. Expressões
# ================================
class Expr(ASTNode):
    """Base para expressões."""
    pass


@dataclass
class BinaryExpr(Expr):
    left: Expr
    op: Token       # operador: + - * / > < >= <= == etc.
    right: Expr


@dataclass
class UnaryExpr(Expr):
    op: Token       # operador unário: + -
    right: Expr


@dataclass
class LiteralExpr(Expr):
    value: Union[int, float, str, bool, None]


@dataclass
class VarExpr(Expr):
    name: Token     # IDENTIFIER


@dataclass
class CallExpr(Expr):
    callee: Token           # nome da função (IDENTIFIER)
    args: List[Expr]