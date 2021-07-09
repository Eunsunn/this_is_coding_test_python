# https://app.codility.com/demo/results/trainingSY78SX-GVM/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if not A:
        return 0
    else:
        return len(list(set(A)))