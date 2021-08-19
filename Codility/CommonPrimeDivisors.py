# https://app.codility.com/demo/results/trainingQQD8YB-ZB8/
# 참고: https://mkki.github.io/codility/2018/05/31/codility-common-prime-divisors.html

# prime divisors가 같다 
# <=> 두 수의 소인수가 최대공약수의 소인수와 같다
# <=> 각 수와 최대공약수의 소인수가 같다
# <=> 어떤 수를 그 수와 최대공약수의 최대공약수로 계속 나눴을 때 1이면 prime divisors 같음

def solution(A, B):
    # 두 수의 최대공약수를 찾는 함수
    def greatest_common_divisor(a, b):
        if a % b == 0:
            return b
        return greatest_common_divisor(b, a % b)

    # 두 수의 prime divisors가 같은지 확인하는 함수
    def have_same_prime_divisors(a, b):
        # 두 수의 최대공약수
        gcd = greatest_common_divisor(a, b)
        # 최대공약수와의 최대공약수로 계속 나눴을 때 1이면 pd가 같다
        tmp_gcd = 0
        while tmp_gcd != 1:
            tmp_gcd = greatest_common_divisor(a, gcd)
            a /= tmp_gcd
        if a != 1:
            return False
        tmp_gcd = 0
        while tmp_gcd != 1:
            tmp_gcd = greatest_common_divisor(b, gcd)
            b /= tmp_gcd
        if b != 1:
            return False
        return True
    
    # query
    cnt = 0
    for i in range(len(A)):
        if have_same_prime_divisors(A[i], B[i]):
            cnt += 1
    return cnt




# https://app.codility.com/demo/results/trainingTQ6ZT7-7TD/
# my solution : timeout error
# idea1) 소수구하기 -> 에라토스테네스의 체
# idea2) prime divisor 구하기 -> 소수로 나눌 수 있을때까지 나누기, 재귀호출 with cache
# idea3) 두 수가 배수관계인 경우 rule 추가

from math import sqrt

# O((N + K) * sqrt(N))
def solution(A, B):
    # N = max(max(A), max(B)), len(A) = len(B) = K
    max_n = max(max(A), max(B))
    # prime number : O(N * sqrt(N))
    primes = set()
    for i in range(2, max_n + 1):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.add(i)
    # prime divisor cache
    cache = {}
    cache[1] = set()

    # prime divisor 구하기 : O(sqrt(N))
    def get_prime_divisor(n):
        if n in cache:
            return cache[n]
        pd = set()
        for i in range(1, int(sqrt(n)) + 1):
            if n % i != 0:
                continue
            j = n // i
            for k in [i, j]:
                if k in primes:
                    pd.add(k)
                    # 나눌 수 있을 때까지 나눈다
                    divided = n
                    while (divided % k == 0):
                        divided = divided // k
                    pd = pd.union(get_prime_divisor(divided))
                    break
        cache[n] = pd
        return pd

    # query 처리 : O(K * sqrt(N))
    cnt = 0
    for i in range(len(A)):
        n, m = A[i], B[i]
        # case1) 두 수가 같은 경우
        if n == m:
            cnt += 1
            continue
        # case2) 두 수가 배수관계 & 배수가 작은수의 prime divisor인 경우
        if n < m:
            n, m = m, n
        if (n % m == 0) and (n // m in get_prime_divisor(m)): 
            cnt += 1
            continue
        # case3) 모두 해당되지 않는 경우
        if get_prime_divisor(n) == get_prime_divisor(m):
            cnt += 1
    return cnt