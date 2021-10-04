
#!/usr/bin/py

class BinaryIndexedTree():
    def __init__(self, sz):
        self.sz = sz
        self.tree = [0] * sz

    def update(self, idx, val):
        while (idx <= self.sz):
               self.tree[idx] += val
               idx += (idx & -idx)
    def read(self, idx):
        sum = 0
        while (idx > 0):
            sum += self.tree[idx]
            idx -= (idx & -idx)
        return sum

if __name__ == '__main__':
    t = input()
    for _ in range(t):
        n = input()
     arr = map(int, raw_input().split())

        cnt = 0
        bit = BinaryIndexedTree(10**7+1)
        for val in reversed(arr):
            bit.update(val, 1)
            cnt += bit.read(val-1)
        print cnt
        #!/bin/python
 
import math
import os
import random
import re
import sys
 
 
def mergeSort(alist):
    inversion_count = 0
 
    n = len(alist)
    if n == 1:
        return 0
 
    mid = len(alist) // 2
    lefthalf = alist[:mid]
    righthalf = alist[mid:]
 
    n1 = len(lefthalf)
    n2 = len(righthalf)
 
    inversion_count += mergeSort(lefthalf)
    inversion_count += mergeSort(righthalf)
 
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        if lefthalf[i] <= righthalf[j]:
            alist[k] = lefthalf[i]
            i = i + 1
        else:
            alist[k] = righthalf[j]
            j = j + 1
            inversion_count += n1 - i
        k = k + 1
 
    while i < n1:
        alist[k] = lefthalf[i]
        i = i + 1
        k = k + 1
 
    while j < n2:
        alist[k] = righthalf[j]
        j = j + 1
        k = k + 1
 
    return inversion_count
 
 
if __name__ == '__main__':
 
    t = int(raw_input())
 
    for t_itr in xrange(t):
        n = int(raw_input())
 
        arr = map(int, raw_input().rstrip().split())
 
        result = mergeSort(arr)
 
        print result
