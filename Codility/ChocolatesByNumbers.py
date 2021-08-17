# https://app.codility.com/demo/results/training7D6SU2-4DQ/

def solution(N, M):
    cnt = 0
    start = 0
    started = set()
    # O(1)
    if N == M:
        cnt = 1
    # O(min(M, N))
    elif N < M:
        for _ in range(N):
            if start in started:
                break
            cnt += 1
            started.add(start)
            start = (start + M) % N
    else:
        for i in range(M):
            if start in started:
                break
            started.add(start)
            # 현재 시작점에서 먹는 개수
            k = (N - 1 - start) // M
            cnt += (k + 1)
            # 다음 시작점 계산
            start = (start + (k + 1) * M) % N
    return cnt