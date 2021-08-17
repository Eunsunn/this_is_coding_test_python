# https://app.codility.com/demo/results/trainingVY6565-U62/

from collections import Counter
from math import sqrt

def solution(A):
    n = len(A)
    max_range = max(A) + 1
    non_divisors = [n] * max_range
    cnt = Counter(A)

    # num의 약수의 개수를 뺀다
    for num in range(1, max_range):
        if num not in cnt:
            continue
        # 에라토스테네스의 체
        # : sqrt(num)까지만 점검한다
        max_iter = int(sqrt(num)) + 1
        for i in range(1, max_iter):
            if num % i != 0:
                continue
            j = num // i
            if i in cnt:
                non_divisors[num] -= cnt[i]
            if (j in cnt) and (i != j):
                non_divisors[num] -= cnt[j]
        
    ret = [non_divisors[val] for val in A]
    return ret