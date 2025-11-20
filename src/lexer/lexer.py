# src/lexer/lexer.py

from dataclasses import dataclass
from .dfa import build_identifier_dfa, build_number_dfa, build_operator_dfa, build_string_dfa

# Lista de palavras reservadas da linguagem NocSysPy
KEYWORDS = {
    'if', 'else', 'while', 'for', 'return', 'func', 'var',
    'print', 'int', 'float', 'string', 'bool', 'true', 'false'
}

@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int


class Lexer:
    def __init__(self, source_code: str):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1

        # Inicializa os autômatos (AFDs específicos)
        self.dfas = [
            build_number_dfa(),
            build_string_dfa(),
            build_operator_dfa(),
            # IDENTIFIER por último (pode virar KEYWORD se estiver na tabela)
            build_identifier_dfa(),
        ]

    def _skip_whitespace(self):
        """Ignora espaços em branco e atualiza linha/coluna."""
        while self.position < len(self.source):
            char = self.source[self.position]
            if char in ' \t\r':
                self.position += 1
                self.column += 1
            elif char == '\n':
                self.position += 1
                self.line += 1
                self.column = 1
            else:
                break

    def next_token(self) -> Token:
        """Retorna o próximo token (princípio do match mais longo)."""
        self._skip_whitespace()

        if self.position >= len(self.source):
            return Token('EOF', 'EOF', self.line, self.column)

        best_match = None
        best_length = 0
        best_token_type = None

        # Buffer: texto restante a partir da posição atual
        remaining_text = self.source[self.position:]

        # Tenta todos os DFAs e pega o que consumiu mais caracteres (Longest Match)
        for dfa in self.dfas:
            token_type, matched_text = dfa.run(remaining_text)
            if matched_text and len(matched_text) > best_length:
                best_match = matched_text
                best_length = len(matched_text)
                best_token_type = token_type

        # Se nenhum DFA aceitou
        if not best_match:
            char = self.source[self.position]
            # Verifica se é pontuação simples que não cobrimos nos DFAs (ex: ; ( ) { } )
            if char in ';,(){}[]':
                token = Token('SYMBOL', char, self.line, self.column)
                self.position += 1
                self.column += 1
                return token

            raise SyntaxError(
                f"Erro Léxico: Caractere inválido '{char}' "
                f"na linha {self.line}, coluna {self.column}"
            )

        # Tratamento especial para Identificadores vs Palavras-Chave
        if best_token_type == 'IDENTIFIER' and best_match in KEYWORDS:
            best_token_type = 'KEYWORD'

        # Cria o token com posição atual
        token = Token(best_token_type, best_match, self.line, self.column)

        # Atualiza posição
        self.position += best_length
        self.column += best_length

        return token

    def get_all_tokens(self):
        tokens = []
        while True:
            tok = self.next_token()
            tokens.append(tok)
            if tok.type == 'EOF':
                break
        return tokens