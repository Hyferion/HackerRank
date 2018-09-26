#!/bin/python3
#https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    sealevel = 0
    valleys = 0
    for step in s:
        if step == "D":
            sealevel = sealevel - 1
        if step == 'U':
            sealevel = sealevel + 1
            if sealevel == 0:
                valleys = valleys + 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
