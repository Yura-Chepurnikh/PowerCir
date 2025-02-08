from lexer import Lexer
from kind import Kind

# R1   Vdd  Drain  10k
def main():
    lexer = Lexer("R1   Vdd  Drain  10k")
    print("---START---")

    while True:
        token = lexer.next_token()
        if (token.kind == Kind.EOF_TOKEN):
            break
        print(token)

if __name__ == "__main__":
    main()