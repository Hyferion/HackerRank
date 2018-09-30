#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    calc = (meal_cost * (tip_percent / 100))
    calc2 = (meal_cost * (tax_percent / 100))
    total = round(meal_cost + calc + calc2)
    return total


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total = solve(meal_cost, tip_percent, tax_percent)

    print(total)
