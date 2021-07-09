# https://app.codility.com/demo/results/training5DAUMB-XY8/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 투 포인터 아이디어로 end 인덱스를 증가시키며 더한다
# 이때 평균보다 작은 수만 더한다

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    min_avg, start_idx = int(1e5) * n, None
    for start in range(n - 1):
        interval_sum = A[start] + A[start + 1]
        if min_avg > (interval_sum / 2):
            min_avg = interval_sum / 2
            start_idx = start
        for end in range(start + 2, n):
            interval_sum += A[end]
            if min_avg > interval_sum / (end - start + 1):
                min_avg = interval_sum / (end - start + 1)
                start_idx = start
            else:
                break
    return start_idx

            