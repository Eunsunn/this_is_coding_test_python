# https://app.codility.com/demo/results/training94VEBR-829/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import Counter

def solution(A):
    # write your code in Python 3.6
    # non-empty list
    cnt = Counter(A)
    for key in cnt:
        if cnt[key] % 2 == 1:
            return key