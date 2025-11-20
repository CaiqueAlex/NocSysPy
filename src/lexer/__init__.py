"""
Pacote do analisador léxico (lexer) para a linguagem NocSysPy.

Este pacote contém:
- dfa.py: Definição dos AFDs específicos (identificadores, números, operadores, strings).
- afn_to_afd.py: Implementação genérica do algoritmo de construção de subconjuntos (AFN -> AFD).
- lexer.py: Implementação do analisador léxico baseado em AFDs.
"""

from .lexer import Lexer, Token, KEYWORDS

__all__ = [
    'Lexer',
    'Token',
    'KEYWORDS',
]

__version__ = '1.0.0'
__author__ = 'NocSysPy Language Team'
__description__ = 'Analisador léxico para a linguagem NocSysPy'