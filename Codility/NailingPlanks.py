# https://app.codility.com/demo/results/trainingRWM88W-298/
# 참고: https://github.com/mbobesic/algorithms-playground/blob/master/codility/NailingPlanks.py

def solution(A, B, C):
    n, m = len(A), len(C)

    # C[:num]까지로 all nailed인지 check
    def all_nailed(num):
        nailed = [0] * (2 * m + 1) # max number
        # num까지 nail 표시
        for i in range(num):
            nailed[C[i]] = 1
        # DP
        for i in range(1, len(nailed)):
            nailed[i] += nailed[i - 1]        
        for i in range(n):
            l, r = A[i], B[i]
            if nailed[r] - nailed[l - 1] == 0:
               return False
        return True 

    # C의 first end nails로 가능한지 판단
    start, end = 0, m
    ret = -1
    while start <= end:
        mid = (start + end) // 2
        # mid까지로 모두 박으면 범위를 줄이고
        if all_nailed(mid):
            end = mid - 1
            ret = mid
        # 그렇지 않으면 범위를 늘린다 (mid까지는 모두 사용)
        else:
            start = mid + 1
    return ret




# my solution : 75% (효율성 2개 timeout)
# 쉬운건 쉽게 풀자
# https://app.codility.com/demo/results/trainingF6BNKM-ZVK/

from bisect import bisect_left, bisect_right

def solution(A, B, C):
    n, m = len(A), len(C)
    # key=start, value=[end] 딕셔너리
    start_end = {}
    for i in range(n):
        start, end = A[i], B[i]
        if start in start_end:
            start_end[start].append(end)
        else:
            start_end[start] = [end]
    # 정렬한 key값의 리스트
    sorted_keys = list(start_end.keys())
    sorted_keys.sort()
    # end 리스트도 정렬
    for key in sorted_keys:
        start_end[key].sort()

    # 각 시작점마다 못이 박힌 최초 위치
    # (한번 박히면 그 뒤로는 다 nailed)
    first_nailed = {}
    for key in sorted_keys:
        first_nailed[key] = len(start_end[key])

    cnt = 0
    ret = -1
    for i in range(m):
        nail = C[i]
        # 1) A[k] <= C[i] 인 최대 시작점을 찾는다
        # (x <= constant) 를 만족하는 최대 x -> upper bound
        max_start_idx = bisect_right(sorted_keys, nail) # 해당 인덱스 불포함

        # 2) 각 시작점마다 C[k] <= B[i]인 최소 끝점을 찾는다
        # (constant <= x)를 만족하는 최소 x -> lower bound 
        for start_idx in range(max_start_idx):
            start = sorted_keys[start_idx]
            # 해당 시작점은 모두 nailed된 경우
            if first_nailed[start] == 0:
                continue
            min_end_idx = bisect_left(start_end[start], nail) # 해당 인덱스 포함
            # 새로 박을 판자가 있는 경우
            if min_end_idx < first_nailed[start]:
                cnt += (first_nailed[start] - min_end_idx)
                first_nailed[start] = min_end_idx
            if cnt == n:
                break
        # 모두 찾은 경우
        if cnt == n:
            ret = i + 1
            break
    return ret