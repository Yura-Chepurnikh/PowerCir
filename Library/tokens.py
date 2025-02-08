class Token:
    def __init__(self, content, kind, position):
        self.content = content
        self.kind = kind
        self.position = position
    def __str__(self):
        return f"{self.content}\t{self.kind}\t{self.position}"
    def __len__(self):
        return len(self.content)