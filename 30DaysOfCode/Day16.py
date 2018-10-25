#!/bin/python3

import sys

s = input().strip()


try:
    number = int(s)
    print(number)
except ValueError:
    print("Bad String")


