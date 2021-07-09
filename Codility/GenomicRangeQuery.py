# https://app.codility.com/demo/results/trainingKX9U6F-J9Y/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    def type_to_factor(t):
        if t == 'A':
            return 1
        elif t == 'C':
            return 2
        elif t == 'G':
            return 3
        elif t == 'T':
            return 4
    
    # S[ : i + 1]까지 타입 개수 count
    # O(N)
    n_types = 4
    cnt = [[0] * n_types]
    cnt[0][type_to_factor(S[0]) - 1] += 1
    for s in S[1:]:
        cur_cnt = []
        for i in range(n_types):
            cur_cnt.append(cnt[-1][i])
        cur_cnt[type_to_factor(s) - 1] += 1
        cnt.append(cur_cnt)

    # cnt[right] ~ cnt[left - 1] 비교
    # O(M) 
    answer = []
    for i in range(len(P)):
        left, right = P[i], Q[i]
        if left == 0:
            for i in range(n_types):
                if cnt[right][i] > 0:
                    answer.append(i + 1)
                    break
        else:
            left -= 1
            for i in range(n_types):
                if cnt[right][i] - cnt[left][i] > 0:
                    answer.append(i + 1)
                    break
    return answer