# https://app.codility.com/demo/results/trainingG7GZ2V-538/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # a <= b <= c
    def is_triangle(a, b, c):
        if (a + b) <= c or (b + c) <= a or (a + c) <= b:
            return False
        return True

    answer = 0
    if (not A) or (len(A) <= 2):
        return answer
    
    n = len(A)
    A.sort()
    # 시작지점 = 양수
    start = n
    for i in range(n):
        if A[i] >= 0:
            start = i
            break
    
    for i in range(start, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (A[i] + A[j]) <= A[k]:
                    break
                if is_triangle(A[i], A[j], A[k]):
                    answer = 1
                    return answer

    return answer