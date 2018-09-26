#!/bin/python3
#https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    ar.append('-1')
    pairs = 0
    i = 0

    while i < n:
        if ar[i] == ar[i + 1]:
            pairs = pairs + 1
            i += 2
        else:
            i += 1
    return pairs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
