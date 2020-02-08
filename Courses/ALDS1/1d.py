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


def main():
    n = int(input())
    minv = int(input())
    maxv = -inf

    for i in range(n-1):
        x = int(input())
        maxv = max(maxv, x-minv)
        minv = min(minv, x)

    print(maxv)


if __name__ == '__main__':
    main()
