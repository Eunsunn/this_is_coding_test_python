# https://app.codility.com/demo/results/trainingPSSZUF-E7G/

# "겹치는" 조건)
# 두 원의 X좌표 구간 [a, b], [a', b']에 대해 (a <= a')
# a <= a' <= b 를 만족한다.
# => 어떤 원의 구간 [a, b]에 대해 a <= a' <= b를 만족하는 a'의 개수를 센다. (bisect)

import bisect

def solution(A):
    # base case: no intersect
    cnt = 0
    if (not A) or (len(A) == 1):
        return cnt

    # 원의 X좌표 구간, 시작점 리스트
    n = len(A)
    max_n = int(1e7)
    interval, start = [], []
    for i in range(n):
        s, e = i - A[i], i + A[i]
        interval.append([s, e])
        start.append(s)
    interval.sort()
    start.sort()
    # 겹치는 시작점 개수
    same_start = dict()
    for i in range(n - 1):
        if start[i] == start[i + 1]:
            val = start[i]
            if val in same_start:
                same_start[val] += 1
            else:
                same_start[val] = 2
    
    # 개수 세기
    for (s, e) in interval:
        # border를 포함하므로 "모두" 센다
        # => 시작 좌표는 bisect_left, 끝 좌표는 bisect_right
        i = bisect.bisect_left(start, s) # 해당 인덱스는 자기 자신 -> 불포함
        j = bisect.bisect_right(start, e) # 끝 점은 경계를 벗어남 -> 불포함
        cnt += (j - i - 1) # 양쪽 불포함

    # 겹치는 start 구간의 중복 빼기
    for s in same_start:
        k = same_start[s]
        cnt -= int((k * (k - 1)) / 2)
    
    if cnt > max_n:
        cnt = -1
    return cnt