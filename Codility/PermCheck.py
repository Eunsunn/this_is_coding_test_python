# https://app.codility.com/demo/results/trainingXF729C-SB5/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # n >= 1
    n = len(A)
    check = [False] * (n + 1)
    for e in A:
        if 1 <= e <= n:
            check[e] = True
    
    is_perm = 1
    for e in check[1:]:
        if e == False:
            is_perm = 0
            break
    return is_perm