#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in list(reversed(arr)):
        print(str(i) + ' ', sep=' ', end='', flush=True)