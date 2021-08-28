# https://app.codility.com/demo/results/trainingTZ3ZWU-X5E/

from collections import deque

def solution(A):
    n = len(A)
    answer = -1

    # 피보나치 수열 만들기 (-1 -> n 총 n + 1까지)
    # O(n)
    fibo = set()
    prev, cur = 1, 2
    fibo.add(prev)
    while cur <= (n + 1):
        fibo.add(cur)
        prev, cur = cur, prev + cur
    
    # base case: 한번에 가는 경우
    # O(n)
    if (n + 1) in fibo:
        answer = 1
        return answer
    
    # base case: 도달하지 못하는 경우 (시작점이 없음)
    # O(n)
    start_ls = []
    for i in range(n):
        if A[i] == 1 and (i + 1) in fibo:
            start_ls.append(i)
    if len(start_ls) == 0:
        return answer

    # -1에서 n까지 최소점프횟수를 계산한다
    # O(n)
    fibo_ls = sorted(list(fibo))
    visited = [False] * (n + 1)
    queue = deque()
    for i in start_ls:
        visited[i] = True
        queue.append((i, 1)) # leaf index, jump

    while queue:
        cur, cnt = queue.popleft()
        for jump in fibo_ls:
            next_leaf = cur + jump
            if next_leaf > n:
                break
            # 최초로 만난 시점이 최소횟수
            elif next_leaf == n:
                answer = cnt + 1
                return answer
            # (next_leaf < n)일때
            elif A[next_leaf] == 1 and not visited[next_leaf]:
                visited[next_leaf] = True
                queue.append((next_leaf, cnt + 1))
    return answer

