from tokens import Token
from kind import Kind

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0

    def next(self):
        self.position += 1

    def next_token(self):
        if self.position >= len(self.text):
            return Token("eof", Kind.EOF_TOKEN, self.position-1)
        
        if self.text[self.position].isspace():
            while self.position < len(self.text) and self.text[self.position].isspace():
                self.next()
            return Token("", Kind.WHITESPACE_TOKEN, self.position-1)
        
        start = self.position
        if self.text[self.position].isalnum():
            while self.position < len(self.text) and self.text[self.position].isalnum():
                self.next()
            str = self.text[start:self.position]
            return Token(str, Kind.IDENTIFIER_TOKEN, start)

        
