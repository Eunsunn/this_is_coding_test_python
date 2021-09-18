# https://app.codility.com/demo/results/trainingT35WAC-WR5/
def solution(A):
    return len(set([abs(a) for a in A]))


# https://app.codility.com/demo/results/trainingGSCUX6-CDZ/
def solution(A):
    abs_value = set()
    # non-decreasing -> 최초로 음수가 아닌 지점 찾기
    prev_idx = -1
    for i in range(len(A)):
        if A[i] >= 0:
            break
        abs_value.add(-A[i])
        prev_idx = i
    for i in range(prev_idx + 1, len(A)):
        abs_value.add(A[i])
    return len(abs_value)