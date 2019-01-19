#!/bin/python3

import sys


def swap(base, comp):
    a[comp], a[base] = a[base], a[comp]


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
numSwaps = 0

for passnum in range(n - 1, 0, -1):
    for i in range(passnum):
        if a[i] > a[i + 1]:
            swap(i, i + 1)
            numSwaps = numSwaps + 1

print("Array is sorted in " + str(numSwaps) + " swaps.")
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[n - 1]))
