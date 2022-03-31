# https://www.acmicpc.net/problem/5052
# 5052번 전화번호 목록 

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tc = int(input())

def solution():
    class Node(object):
        def __init__(self, key, data=None):
            self.key = key
            self.data = data
            self.children = {}
            self.terminal = False
    
    class Trie(object):
        def __init__(self):
            self.head = Node(None)
        
        def insert(self, str):
            node = self.head

            for char in str:
                if char not in node.children:
                    node.children[char] = Node(char)
                node = node.children[char]
            
            node.data = str
            node.terminal = True
                    
        def consistent(self, str):
            node = self.head

            for char in str:
                if node.terminal:
                    return False
                node = node.children[char]
            
            if node.data != None:
                return True


    root = Trie()
    n = int(input())
    cand = True 

    phone = []

    for i in range(n):
        str = input().strip()
        root.insert(str)
        phone.append(str)

    for p in phone:
        if not cand:
            break
        cand &= root.consistent(p)

    ans = "YES" if cand else "NO"
    print(ans)

for i in range(tc):
    solution()

"""
1
3
911
9111
911111
"""