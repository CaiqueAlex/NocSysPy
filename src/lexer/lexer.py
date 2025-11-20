# src/lexer/lexer.py
from .dfa import build_identifier_dfa, build_number_dfa, build_operator_dfa, build_string_dfa

# Lista de palavras reservadas da linguagem NocSysPy
KEYWORDS = {
    'if', 'else', 'while', 'for', 'return', 'func', 'var', 
    'print', 'int', 'float', 'string', 'bool', 'true', 'false'
}

class Lexer:
    def __init__(self, source_code):
        self.source = source_code
        self.position = 0
        self.line = 1
        self.column = 1
        
        # Inicializa os autômatos
        self.dfas = [
            build_number_dfa(),
            build_string_dfa(),
            build_operator_dfa(),
            build_identifier_dfa(), # Deixar por ultimo (prioridade menor que keywords se houvesse conflito direto)
        ]

    def _skip_whitespace(self):
        """Ignora espaços e conta linhas"""
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

    def next_token(self):
        self._skip_whitespace()
        
        if self.position >= len(self.source):
            return ('EOF', 'EOF')

        best_match = None
        best_length = 0
        best_dfa = None

        # Tenta todos os DFAs e pega o que consumiu mais caracteres (Longest Match)
        remaining_text = self.source[self.position:]
        
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
                self.position += 1
                self.column += 1
                return ('SYMBOL', char)
                
            raise SyntaxError(f"Erro Léxico: Caractere inválido '{char}' na linha {self.line}, coluna {self.column}")

        # Tratamento especial para Identificadores vs Palavras-Chave
        if best_token_type == 'IDENTIFIER':
            if best_match in KEYWORDS:
                best_token_type = 'KEYWORD'

        # Atualiza posição
        self.position += best_length
        self.column += best_length
        
        return (best_token_type, best_match)

    def get_all_tokens(self):
        tokens = []
        while True:
            type_, value = self.next_token()
            if type_ == 'EOF':
                break
            tokens.append((type_, value))
        return tokens