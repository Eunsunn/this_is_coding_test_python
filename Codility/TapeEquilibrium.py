# https://app.codility.com/demo/results/training4ZXUMU-4SH/

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    left_sum, right_sum = [], []
    left_sum.append(A[0])
    right_sum.append(A[-1])
    for i in range(1, n):
        left_sum.append(left_sum[-1] + A[i])
        right_sum.append(right_sum[-1] + A[n - i - 1])
    right_sum.reverse()

    # find diff
    min_diff = abs(left_sum[0] - right_sum[1])
    for i in range(1, n - 1):
        tmp_diff = abs(left_sum[i] - right_sum[i + 1])
        if tmp_diff < min_diff:
            min_diff = tmp_diff
    return min_diff