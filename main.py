# main.py
import sys
from src.lexer.lexer import Lexer

def main():
    try:
        # Lê o arquivo de exemplo
        with open('exemplo.noc', 'r') as f:
            source_code = f.read()

        print(f"{'TOKEN TYPE':<20} | {'VALUE':<20}")
        print("-" * 45)

        lexer = Lexer(source_code)
        
        # Processa tokens
        while True:
            token_type, token_value = lexer.next_token()
            
            if token_type == 'EOF':
                break
                
            print(f"{token_type:<20} | {token_value:<20}")
            
    except SyntaxError as e:
        print(f"\n❌ {e}")
    except FileNotFoundError:
        print("Erro: Arquivo 'exemplo.noc' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()