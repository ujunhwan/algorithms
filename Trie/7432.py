# https://www.acmicpc.net/problem/7432
# 7432번 디스크 트리 

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def solution():

    class Node(object):
        def __init__(self, key, data=None):
            self.key = key
            self.data = data
            self.children = {}

        def traverse(self, cnt):
            children = self.children
            blank = ""

            for i in range(cnt):
                blank += " "

            for child in sorted(children):
                print(blank + child)
                children[child].traverse(cnt+1)
        
    class Trie(object):
        def __init__(self, key=None, data=None):
            self.head = Node(None)
            self.key = key
            self.data = data
            self.children = {}

        def insert(self, words):
            node = self.head 
            for word in words:
                if word not in node.children:
                    node.children[word] = Node(word)
                node = node.children[word]
            node.data = words

        def traverse(self):
            node = self.head
            children = sorted(node.children)
            for word in children:
                print(word)
                node.children[word].traverse(1)
                
    N = int(input())
    path = []
    root = Trie('')
    for i in range(N):
        path.append(input().rstrip())

    for p in path:
        words = p.split('\\')
        root.insert(words)

    root.traverse()

solution()
