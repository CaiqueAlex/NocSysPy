# src/lexer/afn_to_afd.py

from collections import defaultdict, deque

EPSILON = None  # usamos None para representar transições-ε

class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        """
        states: conjunto ou lista de estados (strings ou ints)
        alphabet: conjunto de símbolos (chars) EXCETO epsilon
        transitions: dict {(state, symbol) -> set(next_states)}
                     use symbol = EPSILON para transições-ε
        start_state: estado inicial
        accept_states: conjunto de estados de aceitação
        """
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = set(accept_states)

    def epsilon_closure(self, state_set):
        """Retorna o fecho-ε de um conjunto de estados."""
        stack = list(state_set)
        closure = set(state_set)

        while stack:
            s = stack.pop()
            for nxt in self.transitions.get((s, EPSILON), []):
                if nxt not in closure:
                    closure.add(nxt)
                    stack.append(nxt)
        return closure


class DFAFromNFA:
    """
    Representação simples do AFD gerado a partir de um AFN.
    Transições são: dict {state_name: {symbol: next_state_name}}
    """
    def __init__(self, start_state, accept_states, transitions):
        self.start_state = start_state
        self.accept_states = set(accept_states)
        self.transitions = transitions  # {dfa_state: {symbol: dfa_state}}


def nfa_to_dfa(nfa: NFA) -> DFAFromNFA:
    """
    Implementa o algoritmo de construção de subconjuntos (AFN -> AFD).
    Retorna um objeto DFAFromNFA.
    """
    # 1. Estado inicial do DFA = fecho-ε do estado inicial do NFA
    start_closure = frozenset(nfa.epsilon_closure({nfa.start_state}))

    # Mapeia conjunto de estados do NFA -> nome do estado do DFA
    set_to_name = {}
    name_to_set = {}
    dfa_transitions = defaultdict(dict)
    dfa_accept_states = set()

    def get_state_name(state_set):
        if state_set not in set_to_name:
            name = f"S{len(set_to_name)}"
            set_to_name[state_set] = name
            name_to_set[name] = state_set
        return set_to_name[state_set]

    start_name = get_state_name(start_closure)

    # Se o conjunto inicial contém algum estado de aceitação do NFA, é aceitação no DFA também
    if nfa.accept_states & set(start_closure):
        dfa_accept_states.add(start_name)

    # 2. Processar estados com BFS
    queue = deque([start_name])
    visited = set([start_name])

    while queue:
        current_dfa_state = queue.popleft()
        current_nfa_states = name_to_set[current_dfa_state]

        # Para cada símbolo do alfabeto do NFA
        for symbol in nfa.alphabet:
            # 3. Computar o conjunto de estados alcançáveis
            next_nfa_states = set()
            for s in current_nfa_states:
                for nxt in nfa.transitions.get((s, symbol), []):
                    next_nfa_states |= nfa.epsilon_closure({nxt})

            if not next_nfa_states:
                continue  # sem transição para esse símbolo

            next_nfa_states_frozen = frozenset(next_nfa_states)
            next_dfa_state = get_state_name(next_nfa_states_frozen)

            dfa_transitions[current_dfa_state][symbol] = next_dfa_state

            if next_dfa_state not in visited:
                visited.add(next_dfa_state)
                queue.append(next_dfa_state)
                # Verifica se algum estado NFA do conjunto é de aceitação
                if nfa.accept_states & next_nfa_states:
                    dfa_accept_states.add(next_dfa_state)

    return DFAFromNFA(start_state=start_name,
                      accept_states=dfa_accept_states,
                      transitions=dict(dfa_transitions))