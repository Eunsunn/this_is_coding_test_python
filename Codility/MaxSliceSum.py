# https://app.codility.com/demo/results/trainingVXWYBR-QNW/

def solution(A):
    n = len(A)
    # A[i]를 반드시 사용할 때 A[i:]에서 구간합 최대값
    max_sum = [0] * n
    max_sum[-1] = A[-1]
    ret = max_sum[-1]
    for i in range(n - 2, -1, -1):
        max_sum[i] = A[i] + max(0, max_sum[i + 1]) # 이전 합 선택x / 선택o
        ret = max(ret, max_sum[i])
    return ret