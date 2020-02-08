import time
import random
import sys
import bisect
import array
import re
import collections
import heapq
import fractions
import itertools
import string
import math

inf = 10**9


def isPrime(x):
    if x == 2:
        return True

    if x < 2 or x % 2 == 0:
        return False

    for i in range(3, math.floor(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True


def main():
    count = 0
    n = int(input())

    for i in range(n):
        x = int(input())
        if isPrime(x):
            count = count + 1
            # print(x, "is prime number")

    print(count)


if __name__ == '__main__':
    main()
