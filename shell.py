from eval import evaluate
from custom_parser import parse
import sys

def main():
    ast_mode = False
    # -ast flag will print the AST instead of the evaluation
    if len(sys.argv) > 1 and sys.argv[1] == "-ast":
        ast_mode = True
    # Standard REPL
    while True:
        try:
            expr = input("> ")
            if expr == "exit": break
            if ast_mode:
                print(parse(expr))
            else:
                print(evaluate(parse(expr)))
        except EOFError:
            break
        except Exception as e:
            print("Error: " + str(e))

if __name__ == "__main__":
    main()