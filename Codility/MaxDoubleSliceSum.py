# https://app.codility.com/demo/results/trainingNZV52A-BDA/

def solution(A):
    n = len(A)
    # maximal sum of any double slice
    M = 0 # 세 인덱스가 인접한 경우
    # a) base case: 세 인덱스가 인접한 경우
    if n == 3:
        return M

    # b) 두 인덱스가 인접한 경우
    # left_cum[i] = A[i]를 반드시 포함하는 A[:i+1] 구간합 최대값
    # Y + 1 = Z 인 경우도 됨 (= left sum만 있는 경우)
    left_cum = [0, A[1]]
    M = max(M, A[1])
    for i in range(2, n - 1):
        if left_cum[-1] > 0:
            left_cum.append(A[i] + left_cum[-1])
        else:
            left_cum.append(A[i])
        # Y == n - 2 인 경우 Y + 1 = Z에서 제외
        if i != n - 2:
            M = max(M, left_cum[-1])
    left_cum.append(0)
    # 오른쪽 구간합의 최대값
    # X + 1 = Y인 경우 포함 (=right sum만 있는 경우)
    right_cum = [0, A[n - 2]]
    M = max(M, A[n - 2])
    for i in range(n - 3, 0, -1):
        if right_cum[-1] > 0:
            right_cum.append(A[i] + right_cum[-1])
        else:
            right_cum.append(A[i])
        # Y == 1 인 경우 X + 1 = Y 에서 제외
        if i != 1:
            M = max(M, right_cum[-1])
    right_cum.append(0)
    right_cum.reverse()

    # c) 모든 인덱스가 인접하지 않은 경우
    # double slice sum = A[X + 1 : Y] + A[Y + 1 : Z]
    #                  = left_cum[Y - 1] + right_cum[Y + 1]
    for y in range(1, len(left_cum) - 1):
        M = max(M, left_cum[y - 1] + right_cum[y + 1])
    return M