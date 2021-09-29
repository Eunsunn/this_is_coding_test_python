# https://app.codility.com/demo/results/trainingY743SJ-5DH/

def solution(A, B):
    n = len(A)
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    prev_end = B[0]
    cnt = 1

    for i in range(1, n):
        # overlap되는 경우 맨 앞에서 한 번만 센다
        # 그렇지 않은 경우, end를 갱신하며 count 증가
        if prev_end < A[i]:
            prev_end = B[i]
            cnt += 1
    return cnt