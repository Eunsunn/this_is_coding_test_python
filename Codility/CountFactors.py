# https://app.codility.com/demo/results/trainingWBZN4P-993/
from math import sqrt

def solution(N):
    cnt = 0
    iterate = int(sqrt(N))
    for i in range(1, iterate):
        if N % i == 0:
            cnt += 2
    if N % iterate == 0:
        if iterate ** 2 == N:
            cnt += 1
        else:
            cnt += 2
    return cnt