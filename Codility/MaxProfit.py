# https://app.codility.com/demo/results/trainingA7DUVQ-29F/
def solution(A):
    max_profit = 0
    if not A:
        return max_profit
    n = len(A)
    # max(A[i:])를 구한다 : O(N)
    right_max = [A[-1]]
    for i in range(n - 2, -1, -1):
        max_val = max(right_max[-1], A[i])
        right_max.append(max_val)
    right_max.reverse()
    # right_max[i] - A[i]의 값을 구한다 : O(N)
    ret = 0
    for i in range(n - 1):
        ret = max(ret, right_max[i] - A[i])
    return ret