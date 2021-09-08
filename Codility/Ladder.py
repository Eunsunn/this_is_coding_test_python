# https://app.codility.com/demo/results/trainingQ7JU5Y-DJM/

def solution(A, B):
    n = max(A)
    
    # 피보나치 수열 만들기 : O(n) <= O(L)
    fibo = [0, 1, 2]
    while len(fibo) < n + 1:
        fibo.append(fibo[-1] + fibo[-2])

    # Query 처리 : O(L)
    answer = []
    for i in range(len(A)):
        num, p = A[i], B[i]
        # # 시간초과
        # answer.append(fibo[num] % (2 ** p))
        answer.append(fibo[num] & ((1 << p) - 1))
    return answer


# 2의 지수로 나눈 몫, 나머지 비트연산으로 구하기
# n을 2 ** k로 나눈다
from math import log2

def divide(n, k):
    quotient = n >> (int(log2(2 ** k))) # n >> k 와 같다.
    remainder = n & ((1 << k) - 1)
    print("{}을 {}로 나눈 나머지={}, 몫={}".format(n, 2 ** k, remainder, quotient))


divide(152, 3)
divide(27, 2)
divide(197, 4)
