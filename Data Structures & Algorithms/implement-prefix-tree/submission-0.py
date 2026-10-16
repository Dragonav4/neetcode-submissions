class PrefixTree:

    def __init__(self):
        self.val = {}
        self.is_End = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.val:
                node.val[char] = PrefixTree()
            node = node.val[char]
        node.is_End = True

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.val:
                return False
            node = node.val[char]
        return node.is_End

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.val:
                return False
            node = node.val[char]
        return True