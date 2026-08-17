class Node:

    def __init__(self):
        self.children = {} # letter -> Node
        self.is_word = False # is the path a valid word?


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        if not word:
            return

        tmp = self.root
        for c in word:
            if c not in tmp.children:
                tmp.children[c] = Node()
            
            tmp = tmp.children[c]

        tmp.is_word = True

    def search(self, word: str) -> bool:
        tmp = self.root
        for c in word:
            if c not in tmp.children:
                return False
            
            tmp = tmp.children[c]
        
        return tmp.is_word

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for c in prefix:
            if c not in tmp.children:
                return False
            
            tmp = tmp.children[c]
        
        return True
        
        