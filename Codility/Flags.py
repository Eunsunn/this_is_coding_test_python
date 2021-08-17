# https://app.codility.com/demo/results/trainingGRZGSX-ETW/
from math import sqrt

def solution(A):
    n = len(A)
    flags = 0
    # 1. base case : no flag 처리
    if n < 3:
        return flags
    
    # 2. peak 찾기
    peak = []
    i = 1
    while i < n - 1:
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peak.append(i)
        if A[i] > A[i + 1]:
            i += 1
        i += 1
    
    # 3. maximum flag 찾기
    k = len(peak)
    if k == 0:
        return flags
    flags = 1
    # 거리 x에 x개를 꽂을 때 peak는 x**2 이상
    max_dist = int(sqrt(peak[-1] - peak[0]) + 1)
    for distance in range(max_dist, 0, -1):
        # 조기종료
        if distance <= flags:
            break
        # peak[:i+1]까지 최대 flags 수 (DP)
        max_flags = [0] * k
        prev, cur = 0, 1
        max_flags[prev] = 1
        while cur < k:
            # 조기종료
            if max_flags[cur] == distance:
                break
            diff = peak[cur] - peak[prev]
            if diff < distance:
                max_flags[cur] = max(1, max_flags[prev], max_flags[cur])
                cur += 1
            elif diff == distance:
                max_flags[cur] = max(max_flags[cur], max_flags[prev] + 1)
                cur += 1
            else:
                max_flags[cur] = max(max_flags[cur], max_flags[prev] + 1)
                if prev + 1 == cur:
                    cur += 1
                prev += 1
        flags = max(flags, max(max_flags))
    return flags