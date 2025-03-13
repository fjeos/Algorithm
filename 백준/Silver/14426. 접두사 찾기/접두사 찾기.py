import sys

input = sys.stdin.readline


class Node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end = True

    def is_prefix(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


N, M = map(int, input().split())

trie = Trie()
for _ in range(N):
    word = input().strip()
    trie.insert(word)

count = 0
for _ in range(M):
    query = input().strip()
    if trie.is_prefix(query):
        count += 1

print(count)