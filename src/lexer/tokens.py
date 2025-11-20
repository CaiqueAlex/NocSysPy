"""
Definição dos tokens para o analisador léxico da linguagem PySimple.
Cada token representa um elemento básico da linguagem.
"""

from enum import Enum, auto

class TokenType(Enum):
    # Palavras-chave
    IF = auto()
    ELSE = auto()
    ELIF = auto()
    WHILE = auto()
    FOR = auto()
    DEF = auto()
    RETURN = auto()
    CLASS = auto()
    IMPORT = auto()
    FROM = auto()
    AS = auto()
    IN = auto()
    IS = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    TRUE = auto()
    FALSE = auto()
    NONE = auto()
    BREAK = auto()
    CONTINUE = auto()
    PASS = auto()
    PRINT = auto()
    INPUT = auto()
    
    # Identificadores e literais
    IDENTIFIER = auto()
    INTEGER = auto()
    FLOAT = auto()
    STRING = auto()
    
    # Operadores aritméticos
    PLUS = auto()           # +
    MINUS = auto()          # -
    MULTIPLY = auto()       # *
    DIVIDE = auto()         # /
    FLOOR_DIV = auto()      # //
    MODULO = auto()         # %
    POWER = auto()          # **
    
    # Operadores de comparação
    EQUAL = auto()          # ==
    NOT_EQUAL = auto()      # !=
    LESS = auto()           # <
    GREATER = auto()        # >
    LESS_EQUAL = auto()     # <=
    GREATER_EQUAL = auto()  # >=
    
    # Operador de atribuição
    ASSIGN = auto()         # =
    
    # Delimitadores
    LPAREN = auto()         # (
    RPAREN = auto()         # )
    LBRACKET = auto()       # [
    RBRACKET = auto()       # ]
    LBRACE = auto()         # {
    RBRACE = auto()         # }
    COLON = auto()          # :
    COMMA = auto()          # ,
    
    # Controle de fluxo
    NEWLINE = auto()        # \n
    INDENT = auto()         # Indentação
    DEDENT = auto()         # Redução de indentação
    
    # Especiais
    COMMENT = auto()        # #comentário
    WHITESPACE = auto()     # espaços
    EOF = auto()            # Fim do arquivo

class Token:
    """
    Representa um token encontrado no código fonte.
    
    Atributos:
        type: O tipo do token (TokenType)
        lexeme: O texto original que gerou o token
        line: A linha onde o token foi encontrado
        column: A coluna onde o token foi encontrado
    """
    
    def __init__(self, token_type: TokenType, lexeme: str, line: int, column: int):
        self.type = token_type
        self.lexeme = lexeme
        self.line = line
        self.column = column
    
    def __str__(self):
        return f"Token({self.type.name}, '{self.lexeme}', {self.line}:{self.column})"
    
    def __repr__(self):
        return self.__str__()

# Dicionário das palavras-chave
KEYWORDS = {
    'if': TokenType.IF,
    'else': TokenType.ELSE,
    'elif': TokenType.ELIF,
    'while': TokenType.WHILE,
    'for': TokenType.FOR,
    'def': TokenType.DEF,
    'return': TokenType.RETURN,
    'class': TokenType.CLASS,
    'import': TokenType.IMPORT,
    'from': TokenType.FROM,
    'as': TokenType.AS,
    'in': TokenType.IN,
    'is': TokenType.IS,
    'and': TokenType.AND,
    'or': TokenType.OR,
    'not': TokenType.NOT,
    'True': TokenType.TRUE,
    'False': TokenType.FALSE,
    'None': TokenType.NONE,
    'break': TokenType.BREAK,
    'continue': TokenType.CONTINUE,
    'pass': TokenType.PASS,
    'print': TokenType.PRINT,
    'input': TokenType.INPUT,
}

def is_keyword(lexeme: str) -> bool:
    """
    Verifica se um lexema é uma palavra-chave.
    
    Args:
        lexeme: O texto a ser verificado
        
    Returns:
        True se for uma palavra-chave, False caso contrário
    """
    return lexeme in KEYWORDS

def get_keyword_token_type(lexeme: str) -> TokenType:
    """
    Retorna o tipo de token para uma palavra-chave.
    
    Args:
        lexeme: A palavra-chave
        
    Returns:
        O TokenType correspondente à palavra-chave
        
    Raises:
        KeyError: Se o lexema não for uma palavra-chave
    """
    if not is_keyword(lexeme):
        raise KeyError(f"'{lexeme}' não é uma palavra-chave válida")
    
    return KEYWORDS[lexeme]