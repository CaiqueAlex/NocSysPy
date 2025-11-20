# main.py

from src.lexer.lexer import Lexer
from src.parser.parser import Parser, ParserError


def mostrar_tokens(source_code: str):
    print(f"{'TOKEN TYPE':<15} | {'VALUE':<15} | {'LINE':<5} | {'COL':<5}")
    print("-" * 50)

    lexer = Lexer(source_code)

    while True:
        tok = lexer.next_token()
        print(f"{tok.type:<15} | {str(tok.value):<15} | {tok.line:<5} | {tok.column:<5}")
        if tok.type == 'EOF':
            break


def main():
    try:
        with open('exemplo.noc', 'r', encoding='utf-8') as f:
            source_code = f.read()

        print("\n=== TOKENS ===")
        mostrar_tokens(source_code)

        print("\n=== PARSER / AST ===")
        parser = Parser(source_code)
        ast = parser.parse()

        from src.parser.ast import Program, FuncDecl, VarDecl

        if isinstance(ast, Program):
            num_funcs = sum(1 for d in ast.declarations if isinstance(d, FuncDecl))
            num_vars = sum(1 for d in ast.declarations if isinstance(d, VarDecl))
            print("AST construída com sucesso!")
            print(f"- Declarações totais: {len(ast.declarations)}")
            print(f"- Funções: {num_funcs}")
            print(f"- Variáveis globais: {num_vars}")
        else:
            print("AST raiz não é Program (algo estranho aconteceu).")
            print(ast)

    except ParserError as e:
        print(f"\nErro de parser: {e}")
    except SyntaxError as e:
        print(f"\nErro de sintaxe (lexer): {e}")
    except FileNotFoundError:
        print("Erro: Arquivo 'exemplo.noc' não encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()