# main.py

from src.lexer.lexer import Lexer
from src.parser.parser import Parser

def main():
    try:
        # Lê o arquivo de exemplo
        with open('exemplo.noc', 'r', encoding='utf-8') as f:
            source_code = f.read()

        # 1) Mostrar tokens
        print(f"{'TOKEN TYPE':<20} | {'VALUE':<20} | {'LINE':<5} | {'COL':<5}")
        print("-" * 60)

        lexer = Lexer(source_code)

        while True:
            tok = lexer.next_token()

            if tok.type == 'EOF':
                break

            print(f"{tok.type:<20} | {tok.value:<20} | {tok.line:<5} | {tok.column:<5}")

        # 2) Integração com o parser (exemplo simples)
        parser = Parser(source_code)
        ast = parser.parse_program()
        print(f"\nParser consumiu {len(ast)} tokens (sem contar EOF).")

    except SyntaxError as e:
        print(f"\nErro de sintaxe: {e}")
    except FileNotFoundError:
        print("Erro: Arquivo 'exemplo.noc' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()