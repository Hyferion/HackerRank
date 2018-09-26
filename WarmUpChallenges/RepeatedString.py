#!/bin/python
#https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    k = s.count("a")*(n/len(s))
    k += s[:n%len(s)].count("a")

    return k
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = long(raw_input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()