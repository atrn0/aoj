import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
inf = 10**9

n = 0

# p1: (x1, y1)
# p2: (x2, y2)
# s: ((2*x1+x2)/3, (2*y1+y2)/3)
# t: ((x1+2*x2)/3, (y1+2*y2)/3)
# u: ()


def divide_three(p1, p2):
    return (
        ((2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3),
        ((p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3)
    )


def get_coordinates(p1, p2, cur_n):
    d = divide_three(p1, p2)
    top = ()
    if cur_n <= n:
        return [p1] + get_coordinates(p1,) + [p2]


def main():
    global n
    n = int(input())
    for c in get_coordinates((0, 0), (100, 0), 0):
        print(c[0], c[1])


if __name__ == '__main__':
    main()
