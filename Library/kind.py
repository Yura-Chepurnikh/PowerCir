from enum import Enum

class Kind(Enum):
    WHITESPACE_TOKEN = "whitespace"
    IDENTIFIER_TOKEN = "identifier"
    EOF_TOKEN = "eof"


