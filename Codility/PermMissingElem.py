# https://app.codility.com/demo/results/trainingYPKSCM-96C/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # base case: empty list
    if not A:
        return 1
    n = len(A)
    check = [False] * (n + 2)
    for e in A:
        check[e] = True
        
    for i in range(1, n + 2):
        if not check[i]:
            return i
    return