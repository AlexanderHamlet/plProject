from eval import evaluate
from parser import parse

def main():
    # Standard REPL
    while True:
        try:
            expr = input("> ")
            if expr == "exit": break
            print(evaluate(parse(expr)))
        except EOFError:
            break
        except Exception as e:
            print("Error: " + str(e))

if __name__ == "__main__":
    main()