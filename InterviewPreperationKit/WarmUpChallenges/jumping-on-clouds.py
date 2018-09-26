#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    index = 0
    while index < len(c) - 1:
        if index + 2 < len(c):
            if c[index + 2] == 0:
                jumps = jumps + 1
                index = index + 2
            elif c[index + 1] == 0:
                jumps = jumps + 1
                index = index + 1
        elif index + 1 < len(c):
            if c[index + 1] == 0:
                jumps = jumps + 1
                index = index + 1

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()