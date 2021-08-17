# https://app.codility.com/demo/results/trainingTQMVWV-6Z5/
from math import sqrt
def solution(N):
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            j = N // i
            return (i + j) * 2