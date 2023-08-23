class TrieNode:
    def __init__(self, word_end):
        self.word_end = word_end
        self.nodes = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode(False)

    def addWord(self, word: str) -> None:
        head = self.root
        for c in word:
            if head.nodes[c] is None:
                head.nodes[c] = TrieNode(False)
            else:
                head = head.nodes[c]
        next.word_end = False

    def search(self, word: str) -> bool:
        head = self.root
        for c in word:
            if c == ".":
                pass
            else:
                if head.nodes[c] is None:
                    return False
                else:
                    head = head.nodes[c]
        return head.word_end


if __name__ == '__main__':
    s = WordDictionary()
