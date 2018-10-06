#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    dicto = {}
    for i in range(n):
        new_input = input()
        name, number = new_input.split()
        dicto[name] = number
    while True:
        inp = input()
        if inp in dicto:
            print(inp + "=" + dicto[inp])
        else:
            print("Not found")
        if inp == "":
            break
