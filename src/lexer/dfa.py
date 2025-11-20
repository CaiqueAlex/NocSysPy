# src/lexer/dfa.py

class DFA:
    """
    Classe base para Autômatos Finitos Determinísticos baseados em Tabela.
    """
    def __init__(self, name):
        self.name = name
        self.transitions = {}  # { state: { char_condition: next_state } }
        self.accepting_states = {} # { state: token_type }
        self.start_state = 'start'

    def add_transition(self, state, char_condition, next_state):
        """Adiciona uma transição. char_condition pode ser um char ou uma função."""
        if state not in self.transitions:
            self.transitions[state] = []
        self.transitions[state].append((char_condition, next_state))

    def set_accepting(self, state, token_type):
        self.accepting_states[state] = token_type

    def run(self, text):
        """
        Executa o AFD sobre o texto.
        Retorna (token_type, valor_consumido) ou (None, None) se falhar.
        """
        current_state = self.start_state
        chars_consumed = 0
        last_accepting_pos = None
        last_accepting_type = None

        for char in text:
            next_state = None
            
            # Busca transição válida
            if current_state in self.transitions:
                for condition, target in self.transitions[current_state]:
                    # Se a condição for função (ex: is_digit) ou literal (ex: 'a')
                    if callable(condition):
                        if condition(char):
                            next_state = target
                            break
                    elif condition == char:
                        next_state = target
                        break
            
            if next_state:
                current_state = next_state
                chars_consumed += 1
                # Verifica se é estado de aceitação
                if current_state in self.accepting_states:
                    last_accepting_pos = chars_consumed
                    last_accepting_type = self.accepting_states[current_state]
            else:
                break # Transição inválida, para o autômato

        if last_accepting_pos:
            return last_accepting_type, text[:last_accepting_pos]
        return None, None


# --- Definições de Auxiliares ---
def is_digit(c): return c.isdigit()
def is_alpha(c): return c.isalpha() or c == '_'
def is_alnum(c): return c.isalnum() or c == '_'
def is_hex(c): return c in '0123456789abcdefABCDEF'
def is_not_quote(c): return c != '"' and c != '\\'
def is_any(c): return True

# --- Construção dos Autômatos Específicos ---

def build_identifier_dfa():
    dfa = DFA("Identifier")
    # q0 -> q1 (alpha)
    dfa.add_transition('start', is_alpha, 'id_body')
    # q1 -> q1 (alnum)
    dfa.add_transition('id_body', is_alnum, 'id_body')
    dfa.set_accepting('id_body', 'IDENTIFIER')
    return dfa

def build_number_dfa():
    dfa = DFA("Number")
    
    # Inteiro simples e Zero
    dfa.add_transition('start', lambda c: c in '123456789', 'int')
    dfa.add_transition('start', '0', 'zero')
    dfa.add_transition('int', is_digit, 'int')
    
    # Hexadecimal
    dfa.add_transition('zero', 'x', 'hex_pre')
    dfa.add_transition('hex_pre', is_hex, 'hex')
    dfa.add_transition('hex', is_hex, 'hex')
    
    # Float
    dfa.add_transition('int', '.', 'dot')
    dfa.add_transition('zero', '.', 'dot')
    dfa.add_transition('dot', is_digit, 'float')
    dfa.add_transition('float', is_digit, 'float')
    
    # Aceitação
    dfa.set_accepting('int', 'INTEGER')
    dfa.set_accepting('zero', 'INTEGER')
    dfa.set_accepting('hex', 'HEXADECIMAL')
    dfa.set_accepting('float', 'FLOAT')
    
    return dfa

def build_operator_dfa():
    """AFD para Operadores Relacionais e SWAP"""
    dfa = DFA("Relational")
    
    # <, <=, <->
    dfa.add_transition('start', '<', 'less')
    dfa.add_transition('less', '=', 'le')
    dfa.add_transition('less', '-', 'swap_pre')
    dfa.add_transition('swap_pre', '>', 'swap')
    
    # >, >=
    dfa.add_transition('start', '>', 'greater')
    dfa.add_transition('greater', '=', 'ge')
    
    dfa.set_accepting('less', 'LESS')
    dfa.set_accepting('le', 'LESS_EQUAL')
    dfa.set_accepting('swap', 'SWAP')
    dfa.set_accepting('greater', 'GREATER')
    dfa.set_accepting('ge', 'GREATER_EQUAL')
    
    return dfa

def build_string_dfa():
    dfa = DFA("String")
    dfa.add_transition('start', '"', 'body')
    dfa.add_transition('body', is_not_quote, 'body')
    dfa.add_transition('body', '\\', 'escape')
    dfa.add_transition('escape', is_any, 'body') # Aceita qlqr coisa depois da barra
    dfa.add_transition('body', '"', 'final')
    
    dfa.set_accepting('final', 'STRING')
    return dfa