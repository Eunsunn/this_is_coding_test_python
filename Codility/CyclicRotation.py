# https://app.codility.com/demo/results/training6QYQWD-6GF/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    # base case: empty list
    if not A:
        return A

    n = len(A)
    K = K % n
    rotation = [0] * n
    for idx in range(n):
        new_idx = (idx + K) % n
        rotation[new_idx] = A[idx]
    return rotation