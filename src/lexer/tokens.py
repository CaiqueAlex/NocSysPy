```python
"""
Definição dos tokens para o analisador léxico da linguagem NocSysPy.
Cada token representa um elemento básico da linguagem.
"""

from enum import Enum, auto

class TokenType(Enum):
    # Palavras-chave (português)
    SE = auto()             # se (if)
    SENAO = auto()          # senao (else)
    SENAOSE = auto()        # senaose (elif)
    ENQUANTO = auto()       # enquanto (while)
    PARA = auto()           # para (for)
    FUNCAO = auto()         # funcao (def)
    RETORNA = auto()        # retorna (return)
    CLASSE = auto()         # classe (class)
    IMPORTA = auto()        # importa (import)
    DE = auto()             # de (from)
    COMO = auto()           # como (as)
    EM = auto()             # em (in)
    EH = auto()             # eh (is)
    E = auto()              # e (and)
    OU = auto()             # ou (or)
    NAO = auto()            # nao (not)
    VERDADEIRO = auto()     # verdadeiro (True)
    FALSO = auto()          # falso (False)
    NADA = auto()           # nada (None)
    QUEBRA = auto()         # quebra (break)
    CONTINUA = auto()       # continua (continue)
    PULA = auto()           # pula (pass)
    ESCREVA = auto()        # escreva (print)
    LEIA = auto()           # leia (input)
    TIPO = auto()           # tipo (type declaration)
    ASYNC = auto()          # async
    AGUARDA = auto()        # aguarda (await)
    
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
    
    # Operadores especiais do NocSysPy
    SWAP = auto()           # <-> (troca)
    NULL_COALESCING = auto() # ?? (null coalescing)
    ARROW = auto()          # => (arrow function)
    PIPE = auto()           # |> (pipe operator)
    
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
    SEMICOLON = auto()      # ;
    
    # Controle de fluxo
    NEWLINE = auto()        # \n
    
    # Especiais
    COMMENT = auto()        # # comentário
    BLOCK_COMMENT = auto()  # /* comentário */
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

# Dicionário das palavras-chave em português
KEYWORDS = {
    'se': TokenType.SE,
    'senao': TokenType.SENAO,
    'senaose': TokenType.SENAOSE,
    'enquanto': TokenType.ENQUANTO,
    'para': TokenType.PARA,
    'funcao': TokenType.FUNCAO,
    'retorna': TokenType.RETORNA,
    'classe': TokenType.CLASSE,
    'importa': TokenType.IMPORTA,
    'de': TokenType.DE,
    'como': TokenType.COMO,
    'em': TokenType.EM,
    'eh': TokenType.EH,
    'e': TokenType.E,
    'ou': TokenType.OU,
    'nao': TokenType.NAO,
    'verdadeiro': TokenType.VERDADEIRO,
    'falso': TokenType.FALSO,
    'nada': TokenType.NADA,
    'quebra': TokenType.QUEBRA,
    'continua': TokenType.CONTINUA,
    'pula': TokenType.PULA,
    'escreva': TokenType.ESCREVA,
    'leia': TokenType.LEIA,
    'tipo': TokenType.TIPO,
    'async': TokenType.ASYNC,
    'aguarda': TokenType.AGUARDA,
}

# Operadores multi-caractere
OPERATORS = {
    '==': TokenType.EQUAL,
    '!=': TokenType.NOT_EQUAL,
    '<=': TokenType.LESS_EQUAL,
    '>=': TokenType.GREATER_EQUAL,
    '//': TokenType.FLOOR_DIV,
    '**': TokenType.POWER,
    '<->': TokenType.SWAP,
    '??': TokenType.NULL_COALESCING,
    '=>': TokenType.ARROW,
    '|>': TokenType.PIPE,
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

def is_operator(lexeme: str) -> bool:
    """
    Verifica se um lexema é um operador multi-caractere.
    
    Args:
        lexeme: O texto a ser verificado
        
    Returns:
        True se for um operador, False caso contrário
    """
    return lexeme in OPERATORS

def get_operator_token_type(lexeme: str) -> TokenType:
    """
    Retorna o tipo de token para um operador.
    
    Args:
        lexeme: O operador
        
    Returns:
        O TokenType correspondente ao operador
        
    Raises:
        KeyError: Se o lexema não for um operador válido
    """
    if not is_operator(lexeme):
        raise KeyError(f"'{lexeme}' não é um operador válido")
    
    return OPERATORS[lexeme]