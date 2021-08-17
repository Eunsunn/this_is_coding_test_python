# 1차) https://app.codility.com/demo/results/trainingDRXHYJ-6H3/
# 2차) https://app.codility.com/demo/results/trainingUDX5S8-M6F/
# -> 제어문 하나로 2배 시간절약

from math import sqrt

def solution(N, P, Q):
    # 1. 소수 구하기 : 에라토스테네스의 체
    # O(N * sqrt(N))
    is_prime = [True] * (N + 1)
    is_prime[1] = False
    max_iter = int(sqrt(N)) + 1
    for i in range(2, max_iter):
        if not is_prime[i]:
            continue
        # 배수를 지운다
        for j in range(i * 2, N + 1, i):
            if is_prime[j]:
                is_prime[j] = False

    # 2. semi_prime 구하기
    # O(N * sqrt(N))
    semi_prime = [False] * (N + 1)
    for i in range(2, max_iter):
        if not is_prime[i]:
            continue
        for j in range(N + 1):
            ######## 추가된 제어문 ########
            if i * j > N:
                break
            ###############################
            if not is_prime[j]:
                continue
            semi_prime[i * j] = True

    # 3. 누적 semi_prime 개수 (DP)
    # O(N)
    cum_sp = [0]
    for i in range(1, N + 1):
        cum_sp.append(cum_sp[-1] + semi_prime[i])

    # 4. query 처리
    # O(K)
    ret = []
    k = len(P)
    for i in range(k):
        l, r = P[i], Q[i]
        ret.append(cum_sp[r] - cum_sp[l - 1])
    return ret