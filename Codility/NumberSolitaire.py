# https://app.codility.com/demo/results/trainingKN6ZAM-BNE/

def solution(A):
    n = len(A)
    min_val = -int(1e5) * n

    # i번째까지 marked sum의 최대값
    max_sum = [min_val] * n
    max_sum[0] = A[0]
    
    # i번째에서 갈 수 있는 범위를 갱신한다
    for i in range(n - 1):
        for dice in range(1, 7):
            if i + dice >= n:
                break
            max_sum[i + dice] = max(max_sum[i + dice], max_sum[i] + A[i + dice])
    
    return max_sum[-1]
