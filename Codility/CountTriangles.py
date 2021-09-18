# https://app.codility.com/demo/results/training43J32Z-E9F/
from bisect import bisect_left

def solution(A):
    n = len(A)
    cnt = 0
    if n <= 2:
        return cnt
    sorted_A = sorted(A)

    # O((N ** 2) * logN)
    # triangle triplets 개수 세기
    # 작은 두 변의 인덱스 i, j
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            # 두 변이 고정되었을 때, 부등식을 만족하는 최대 인덱스 k 찾기
            sums = sorted_A[i] + sorted_A[j]
            k = bisect_left(sorted_A, sums) # 등호 불포함 -> bisect_left
            # 한개 이상이 존재할 경우 count
            if k > j + 1:
                cnt += (k - j - 1)
    return cnt