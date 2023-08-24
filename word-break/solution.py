from typing import List


class TrieNode:
    def __init__(self):
        self.word_end = False
        self.nodes = {}



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        # implement a trie
        for word in wordDict:
            head = root
            for c in word:
                if c not in head.nodes:
                    head.nodes[c] = TrieNode()
                head = head.nodes[c]
            head.word_end = True

        return self.search(root, [x for x in s])


    def search(self, root, chars):
        temp = root
        while chars:
            char = chars.pop(0)
            if char not in temp.nodes:
                return False
            elif temp.nodes[char].word_end and len(chars) != 0:
                # we found a word end, and some chars in string left to explore
                temp = root
            else:

                temp = temp.nodes[char]

        return temp.word_end


if __name__ == '__main__':
    s = Solution()
    s.wordBreak("aaaaaaa", ["aaaa","aaa"])
