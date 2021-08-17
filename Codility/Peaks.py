# https://app.codility.com/demo/results/trainingT999S2-JDV/

def solution(A):
    n = len(A)
    max_block = 0
    # 0. base case: no peak
    if n < 3:
        return max_block
    
    # 1. peak 찾기
    peak = []
    i = 1
    while i < n - 1:
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peak.append(i)
        if A[i] > A[i + 1]:
            i += 1
        i += 1
    k = len(peak)
    if k <= 1:
        return len(peak)
    # A[:i+1]까지 peak 개수
    cum_peak = [0] * n
    for i in peak:
        cum_peak[i] = 1
    for i in range(1, n):
        cum_peak[i] += cum_peak[i - 1]


    # 2. maximum block 찾기
    for num_block in range(k, 0, -1):
        if max_block >= num_block:
            break
        if n % num_block != 0:
            continue
        len_block = n // num_block
        # block에 peak가 있는지 판별하기
        if cum_peak[ : len_block] == 0:
            continue
        contain_peak = True
        for i in range(1, num_block):
            start, end = i * len_block - 1, (i+1) * len_block - 1
            if cum_peak[end] - cum_peak[start] == 0:
                contain_peak = False
                break
        if contain_peak:
            max_block = num_block
            break
    return max_block