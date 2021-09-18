# https://app.codility.com/demo/results/trainingM6UF8C-NRK/

from bisect import bisect_left, bisect_right

def solution(A):
    n = len(A)

    # O(N)
    # 양수, 음수로 분리
    positive, negative = [], []
    for i in range(n):
        # base case: 0인 경우 -> 절대값이 0 -> 절대값의 최소
        if A[i] == 0:
            return 0
        elif A[i] > 0:
            positive.append(A[i])
        else:
            negative.append(A[i])
    
    # O(N * log(N))
    min_abs = int(1e9) * 2
    if positive:
        positive.sort()
        # min_abs case 1) 절대값이 가장 작은 수 * 2
        min_abs = min(min_abs, positive[0] * 2)
        # min_abs case 2) 절대값이 가장 작은 두 수의 합
        if len(positive) >= 2:
            min_abs = min(min_abs, positive[0] + positive[1])
    if negative:
        negative.sort()
        # min_abs case 1)
        min_abs = min(min_abs, (-negative[-1]) * 2)
        # min_abs case 2)
        if len(negative) >= 2:
            min_abs = min(min_abs, -(negative[-1] + negative[-2]))
        
    # base case: 양수 혹은 음수만 있는 경우 위에서 정답 발생
    if len(positive) == 0 or len(negative) == 0:
        return min_abs

    # O(N * logN)
    # min_abs case 3) 부호 반대에서 절대값이 가장 비슷한 수
    positive_n = len(positive)
    for neg in negative:
        target = -neg
        # 1) bisect_left -> 동일한 값은 bl_idx + 1 이상에서 발생
        bl_idx = bisect_left(positive, target)
        # base case: 절대값이 반대인 수가 있으면 최소값 0 리턴
        if (bl_idx < positive_n - 1) and positive[bl_idx + 1] == target:
            min_abs = 0
            break
        if bl_idx > 0:
            min_abs = min(min_abs, target - positive[bl_idx - 1])
        if bl_idx < positive_n:
            min_abs = min(min_abs, abs(positive[bl_idx] - target)) # bl_idx 번째는 뭐가 큰지 모름
        # 2) bisect_right -> 동일한 값은 이미 위에서 체크
        br_idx = bisect_right(positive, target)
        if br_idx > 0:
            min_abs = min(min_abs, target - positive[br_idx - 1])
        if br_idx < positive_n:
            min_abs = min(min_abs, abs(positive[br_idx] - target)) # br_idx 번째는 뭐가 큰기 모름

    return min_abs