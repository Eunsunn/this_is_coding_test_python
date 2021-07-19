# https://app.codility.com/demo/results/trainingHBTWVD-NH3/

def solution(A):
    n = len(A)
    l_cnt, l_max, l_val, l_leader = {}, 0, None, [None] * n
    r_cnt, r_max, r_val, r_leader = {}, 0, None, [None] * n
    for i in range(n):
        # 왼쪽 leader 찾기
        key1 = A[i]
        if key1 in l_cnt:
            l_cnt[key1] += 1
        else:
            l_cnt[key1] = 1
        if l_cnt[key1] > l_max:
            l_max = l_cnt[key1]
            l_val = key1
        if l_max > (i + 1) / 2:
            l_leader[i] = l_val
        # 오른쪽 leader
        key2 = A[n - 1 - i]
        if key2 in r_cnt:
            r_cnt[key2] += 1
        else:
            r_cnt[key2] = 1
        if r_cnt[key2] > r_max:
            r_max = r_cnt[key2]
            r_val = key2
        if r_max > (i + 1) / 2:
            r_leader[n - 1 - i] = r_val

    # equi leader 찾기
    ret = 0
    for i in range(n - 1):
        # 주의) "!= None" 을 써야함. if leader[i]하면 값이 0인경우 카운트되지 않음
        if l_leader[i] != None and r_leader[i + 1] != None and l_leader[i] == r_leader[i + 1]:
            ret += 1
    return ret