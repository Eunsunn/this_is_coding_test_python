# https://app.codility.com/demo/results/training9GH8ZP-W7H/

def solution(A):
    idx = {}
    max_len = []
    for i in range(len(A)):
        key = A[i]
        if key in idx:
            idx[key].append(i)
        else:
            idx[key] = [i]
        if len(idx[key]) > len(max_len):
            max_len = idx[key]

    if len(max_len) > len(A) / 2:
        return max_len[0]
    else:
        return -1