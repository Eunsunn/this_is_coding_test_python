# 1차: https://app.codility.com/demo/results/trainingQA9N79-FUG/
# 2차: https://app.codility.com/demo/results/trainingDAKSHW-2GJ/ (코드정리)

def solution(K, A):
    n = len(A)

    # A[:i + 1]까지 누적 개수
    dp = [0] * n # 단조증가
    dp[0] = (A[0] >= K) * 1
    # 최근 묶은 후 값 누적
    last_cum = 0
    if dp[0] == 0:
        last_cum = A[0]
        
    # 개수가 최대가 되도록 묶기
    for i in range(1, n):
        # 1) (원소가 K이상) or (tie해서 K이상으로 만들 수 있는 경우) cnt 증가
        if (A[i] >= K) or (A[i] + last_cum >= K):
            dp[i] = dp[i - 1] + 1
            last_cum = 0
        # 2) K이상을 만들 수 없는 경우
        else:
            dp[i] = dp[i - 1]
            last_cum += A[i]
    return dp[-1]