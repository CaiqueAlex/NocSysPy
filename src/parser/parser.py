# src/parser/parser.py

from src.lexer.lexer import Lexer, Token

class Parser:
    def __init__(self, source_code: str):
        self.lexer = Lexer(source_code)
        self.current_token: Token = self.lexer.next_token()

    def _advance(self):
        self.current_token = self.lexer.next_token()

    def _match(self, expected_type: str):
        if self.current_token.type == expected_type:
            self._advance()
        else:
            raise SyntaxError(
                f"Erro Sintático: esperado {expected_type}, "
                f"mas encontrado {self.current_token.type} "
                f"('{self.current_token.value}') "
                f"na linha {self.current_token.line}, "
                f"coluna {self.current_token.column}"
            )

    def parse_program(self):
        """
        Exemplo de método de parsing: por enquanto só consome todos tokens
        até EOF. Depois você pode substituir isso pelas regras da sua gramática.
        """
        ast = []
        while self.current_token.type != 'EOF':
            ast.append(self.current_token)
            self._advance()
        return ast