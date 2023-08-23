class TrieNode:
    def __init__(self):
        self.word_end = False
        self.nodes = {}


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        head = self.root
        for c in word:
            if c not in head.nodes:
                head.nodes[c] = TrieNode()
            head = head.nodes[c]
        head.word_end = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            head = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for node in head.nodes.values():
                        if dfs(i + 1, node):
                            return True
                    return False
                else:
                    if c not in head.nodes:
                        return False
                    head = head.nodes[c]
            return head.word_end

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)