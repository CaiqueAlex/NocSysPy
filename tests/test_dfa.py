# tests/test_dfa.py
import unittest
import sys
import os

# Adiciona diretório src ao path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lexer.dfa import build_identifier_dfa, build_number_dfa, build_operator_dfa, build_string_dfa

class TestDFA(unittest.TestCase):
    
    def test_identifier(self):
        dfa = build_identifier_dfa()
        
        # Casos Válidos
        self.assertEqual(dfa.run("variavel")[0], 'IDENTIFIER')
        self.assertEqual(dfa.run("_privado")[0], 'IDENTIFIER')
        self.assertEqual(dfa.run("var123")[0], 'IDENTIFIER')
        
        # Casos Inválidos (retorna None ou consome parcialmente)
        self.assertIsNone(dfa.run("123var")[0]) # Começa com número
        
    def test_number(self):
        dfa = build_number_dfa()
        
        # Inteiros
        self.assertEqual(dfa.run("123")[0], 'INTEGER')
        self.assertEqual(dfa.run("0")[0], 'INTEGER')
        
        # Hex
        self.assertEqual(dfa.run("0xFF")[0], 'HEXADECIMAL')
        
        # Float
        self.assertEqual(dfa.run("3.14")[0], 'FLOAT')
        
        # Parcial (ex: 123a deve ler só 123)
        token, val = dfa.run("123abc")
        self.assertEqual(val, "123")
        
    def test_relational(self):
        dfa = build_operator_dfa()
        
        # Máxima correspondência
        self.assertEqual(dfa.run("<=")[0], 'LESS_EQUAL')
        self.assertEqual(dfa.run("<->")[0], 'SWAP')
        self.assertEqual(dfa.run("<")[0], 'LESS')
        
    def test_string(self):
        dfa = build_string_dfa()
        
        self.assertEqual(dfa.run('"Ola Mundo"')[0], 'STRING')
        self.assertEqual(dfa.run('"Ola \\" Mundo"')[0], 'STRING') # Escape

if __name__ == '__main__':
    unittest.main()