# src/parser/parser.py

from __future__ import annotations
from typing import List, Optional
from src.lexer.lexer import Lexer, Token
from .ast import (
    Program, VarDecl, FuncDecl, Param,
    Block, AssignStmt, IfStmt, WhileStmt,
    ReturnStmt, PrintStmt, ExprStmt,
    Expr, BinaryExpr, UnaryExpr, LiteralExpr,
    VarExpr, CallExpr
)


class ParserError(SyntaxError):
    pass


class Parser:
    def __init__(self, source_code: str):
        self.lexer = Lexer(source_code)
        self.current_token: Token = self.lexer.next_token()

    # ==========================
    # Utilitários básicos
    # ==========================
    def _advance(self):
        self.current_token = self.lexer.next_token()

    def _check(self, type_: str, value: Optional[str] = None) -> bool:
        if self.current_token.type != type_:
            return False
        if value is not None and self.current_token.value != value:
            return False
        return True

    def _match(self, type_: str, value: Optional[str] = None) -> bool:
        if self._check(type_, value):
            self._advance()
            return True
        return False

    def _consume(self, type_: str, value: Optional[str] = None, message: str = "") -> Token:
        if self._check(type_, value):
            tok = self.current_token
            self._advance()
            return tok
        exp = f"{type_}" + (f"('{value}')" if value else "")
        got = f"{self.current_token.type}('{self.current_token.value}')"
        loc = f"linha {self.current_token.line}, coluna {self.current_token.column}"
        if message:
            raise ParserError(f"{message} (esperado {exp}, mas encontrado {got} em {loc})")
        raise ParserError(f"Esperado {exp}, mas encontrado {got} em {loc}")

    # ==========================
    # Entrada principal
    # ==========================
    def parse(self) -> Program:
        """
        Program ::= { TopLevel } EOF
        TopLevel ::= FuncDecl
                   | VarDecl
                   | Stmt        -- permite statements no nível global
        """
        declarations: List = []
        while self.current_token.type != 'EOF':
            if self._check('KEYWORD', 'func'):
                declarations.append(self._func_decl())
            elif self._check('KEYWORD', 'var'):
                declarations.append(self._var_decl())
            else:
                # permite print, if, etc. no nível global
                declarations.append(self._statement())
        return Program(declarations)

    # ==========================
    # Declarações
    # ==========================
    def _var_decl(self) -> VarDecl:
        """
        VarDecl ::= "var" IDENT ["=" Expr] ";"
        (na prática seu código SEMPRE usa "var x = expr;")
        """
        var_tok = self._consume('KEYWORD', 'var', "Esperado 'var' em declaração de variável")

        name_tok = self._consume('IDENTIFIER', message="Esperado identificador de variável após 'var'")

        init_expr: Optional[Expr] = None
        if self._check('ASSIGN') or (self._check('SYMBOL') and self.current_token.value == '='):
            self._advance()
            init_expr = self._expression()

        self._consume('SYMBOL', ';', "Esperado ';' ao final da declaração de variável")

        return VarDecl(var_tok, name_tok, init_expr)

    def _func_decl(self) -> FuncDecl:
        """
        FuncDecl ::= "func" IDENT "(" [ ParamList ] ")" Block
        ParamList ::= IDENT { "," IDENT }     -- parâmetros sem tipo
        """
        func_tok = self._consume('KEYWORD', 'func', "Esperado 'func' em declaração de função")
        name_tok = self._consume('IDENTIFIER', message="Esperado nome da função após 'func'")

        self._consume('SYMBOL', '(', "Esperado '(' após nome da função")

        params: List[Param] = []
        if not self._check('SYMBOL', ')'):
            params.append(self._param())
            while self._match('SYMBOL', ','):
                params.append(self._param())

        self._consume('SYMBOL', ')', "Esperado ')' após parâmetros da função")

        body = self._block()

        return FuncDecl(func_tok, name_tok, params, body)

    def _param(self) -> Param:
        """
        Param ::= IDENT      -- sem tipo
        """
        name_tok = self._consume('IDENTIFIER', message="Esperado nome de parâmetro")
        return Param(name_tok)

    # ==========================
    # Blocos e statements
    # ==========================
    def _block(self) -> Block:
        """
        Block ::= "{" { Stmt } "}"
        """
        self._consume('SYMBOL', '{', "Esperado '{' para iniciar bloco")
        statements: List = []
        while not self._check('SYMBOL', '}') and self.current_token.type != 'EOF':
            statements.append(self._statement())
        self._consume('SYMBOL', '}', "Esperado '}' para finalizar bloco")
        return Block(statements)

    def _statement(self):
        """
        Stmt ::= VarDecl
               | AssignStmt
               | IfStmt
               | WhileStmt
               | ReturnStmt
               | PrintStmt
               | Block
               | ";"
        """
        if self._check('KEYWORD', 'var'):
            return self._var_decl()

        if self._check('KEYWORD', 'if'):
            return self._if_stmt()
        if self._check('KEYWORD', 'while'):
            return self._while_stmt()
        if self._check('KEYWORD', 'return'):
            return self._return_stmt()
        if self._check('KEYWORD', 'print'):
            return self._print_stmt()
        if self._check('SYMBOL', '{'):
            return self._block()
        if self._check('SYMBOL', ';'):
            self._advance()
            return ExprStmt(LiteralExpr(None))

        return self._assign_or_expr_stmt()

    def _assign_or_expr_stmt(self):
        """
        - AssignStmt: IDENT "=" Expr ";"
        - ExprStmt: Expr ";"
        """
        if self._check('IDENTIFIER'):
            ident_tok = self.current_token
            self._advance()
            if self._check('ASSIGN') or (self._check('SYMBOL') and self.current_token.value == '='):
                self._advance()
                value = self._expression()
                self._consume('SYMBOL', ';', "Esperado ';' após atribuição")
                target = VarExpr(ident_tok)
                return AssignStmt(target, value)
            else:
                expr: Expr = self._finish_primary_from_ident(ident_tok)
                expr = self._expression_tail(expr)
                self._consume('SYMBOL', ';', "Esperado ';' após expressão")
                return ExprStmt(expr)

        expr = self._expression()
        self._consume('SYMBOL', ';', "Esperado ';' após expressão")
        return ExprStmt(expr)

    # ==========================
    # Comandos específicos
    # ==========================
    def _if_stmt(self) -> IfStmt:
        self._consume('KEYWORD', 'if')
        self._consume('SYMBOL', '(', "Esperado '(' após 'if'")
        cond = self._expression()
        self._consume('SYMBOL', ')', "Esperado ')' após condição do if")
        then_branch = self._as_block(self._statement())
        else_branch: Optional[Block] = None
        if self._check('KEYWORD', 'else'):
            self._advance()
            else_branch = self._as_block(self._statement())
        return IfStmt(cond, then_branch, else_branch)

    def _while_stmt(self) -> WhileStmt:
        self._consume('KEYWORD', 'while')
        self._consume('SYMBOL', '(', "Esperado '(' após 'while'")
        cond = self._expression()
        self._consume('SYMBOL', ')', "Esperado ')' após condição do while")
        body = self._as_block(self._statement())
        return WhileStmt(cond, body)

    def _return_stmt(self) -> ReturnStmt:
        self._consume('KEYWORD', 'return')
        if self._check('SYMBOL', ';'):
            self._advance()
            return ReturnStmt(None)
        value = self._expression()
        self._consume('SYMBOL', ';', "Esperado ';' após return")
        return ReturnStmt(value)

    def _print_stmt(self) -> PrintStmt:
        self._consume('KEYWORD', 'print')
        self._consume('SYMBOL', '(', "Esperado '(' após 'print'")
        value = self._expression()
        self._consume('SYMBOL', ')', "Esperado ')' após expressão em print")
        self._consume('SYMBOL', ';', "Esperado ';' após print")
        return PrintStmt(value)

    def _as_block(self, stmt) -> Block:
        if isinstance(stmt, Block):
            return stmt
        return Block([stmt])

    # ==========================
    # Expressões
    # ==========================
    def _expression(self) -> Expr:
        left = self._add_expr()
        return self._rel_expr_tail(left)

    def _rel_expr_tail(self, left: Expr) -> Expr:
        while self._check('GREATER') or \
              (self._check('SYMBOL') and self.current_token.value in ('>',)):
            op_tok = self.current_token
            self._advance()
            right = self._add_expr()
            left = BinaryExpr(left, op_tok, right)
        return left

    def _add_expr(self) -> Expr:
        expr = self._term()
        while (self._check('PLUS') or self._check('MINUS') or
               (self._check('SYMBOL') and self.current_token.value in ('+', '-'))):
            op_tok = self.current_token
            self._advance()
            right = self._term()
            expr = BinaryExpr(expr, op_tok, right)
        return expr

    def _term(self) -> Expr:
        expr = self._factor()
        while (self._check('STAR') or self._check('SLASH') or
               (self._check('SYMBOL') and self.current_token.value in ('*', '/'))):
            op_tok = self.current_token
            self._advance()
            right = self._factor()
            expr = BinaryExpr(expr, op_tok, right)
        return expr

    def _factor(self) -> Expr:
        if (self._check('PLUS') or self._check('MINUS') or
                (self._check('SYMBOL') and self.current_token.value in ('+', '-'))):
            op_tok = self.current_token
            self._advance()
            right = self._factor()
            return UnaryExpr(op_tok, right)

        if self._check('SYMBOL', '('):
            self._advance()
            expr = self._expression()
            self._consume('SYMBOL', ')', "Esperado ')' após expressão")
            return expr

        if self._check('INTEGER'):
            tok = self.current_token
            self._advance()
            return LiteralExpr(int(tok.value))
        if self._check('FLOAT'):
            tok = self.current_token
            self._advance()
            return LiteralExpr(float(tok.value))
        if self._check('STRING'):
            tok = self.current_token
            self._advance()
            return LiteralExpr(tok.value)

        if self._check('IDENTIFIER'):
            ident_tok = self.current_token
            self._advance()
            if self._check('SYMBOL', '('):
                self._advance()
                args: List[Expr] = []
                if not self._check('SYMBOL', ')'):
                    args.append(self._expression())
                    while self._match('SYMBOL', ','):
                        args.append(self._expression())
                self._consume('SYMBOL', ')', "Esperado ')' após argumentos de função")
                return CallExpr(ident_tok, args)
            return VarExpr(ident_tok)

        tok = self.current_token
        raise ParserError(
            f"Esperado expressão, mas encontrado {tok.type}('{tok.value}') "
            f"na linha {tok.line}, coluna {tok.column}"
        )

    def _finish_primary_from_ident(self, ident_tok: Token) -> Expr:
        if self._check('SYMBOL', '('):
            self._advance()
            args: List[Expr] = []
            if not self._check('SYMBOL', ')'):
                args.append(self._expression())
                while self._match('SYMBOL', ','):
                    args.append(self._expression())
            self._consume('SYMBOL', ')', "Esperado ')' após argumentos de função")
            return CallExpr(ident_tok, args)
        return VarExpr(ident_tok)

    def _expression_tail(self, left: Expr) -> Expr:
        return left