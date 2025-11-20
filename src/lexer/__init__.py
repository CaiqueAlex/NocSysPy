"""
Pacote do analisador léxico (lexer) para a linguagem PySimple.

Este pacote contém:
- Definições de tokens (tokens.py)
- Analisador léxico principal (lexer.py) - a ser implementado
- Utilitários para análise lexical

O analisador léxico é responsável por:
1. Dividir o código fonte em tokens
2. Identificar palavras-chave, identificadores, operadores e literais
3. Tratar espaçamento e indentação
4. Detectar e reportar erros léxicos
"""

from .tokens import Token, TokenType, KEYWORDS, is_keyword, get_keyword_token_type

__all__ = [
    'Token',
    'TokenType', 
    'KEYWORDS',
    'is_keyword',
    'get_keyword_token_type'
]

__version__ = '1.0.0'
__author__ = 'PySimple Language Team'
__description__ = 'Analisador léxico para a linguagem PySimple'