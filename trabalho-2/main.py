from Work import main
from init import menu
import os, sys

if __name__ == "__main__":
    while True:
        menu()
        op: int = int(input("\x1b[1m\x1b[34mEscolha uma opção:\x1b[0m "))
        if op == 0:
            print("\x1b[1m\x1b[31m Saindo....\x1b[0m")
            sys.exit(0)
        elif op == 1:
            main()
            op: str = input("\x1b[1m\x1b[33mDeseja continuar[s/n]:\x1b[0m ").lower()
            if op == 's':
                os.system("clear")
                continue
            else:
                print("\x1b[1m\x1b[31m Saindo....\x1b[0m")
                sys.exit(0)
        else:
            raise AttributeError("\x1b[1m\x1b[31m Opção inválida\x1b[0m")