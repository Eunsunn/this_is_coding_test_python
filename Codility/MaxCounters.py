# https://app.codility.com/demo/results/trainingMF6MD7-EJ2/
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 핵심 아이디어
# max 이후 매번 counter를 갱신(O(NM)) 하지 말고
# 최대값을 이용한 효율적인 갱신!

def solution(N, A):
    # write your code in Python 3.6
    counter = [0] * N
    # 현재 최대값, 이전 max 연산에서 최대값
    tmp_max, max_value = 0, 0

    for oper in A:
        idx = oper - 1
        # 1) increase 연산
        if 1 <= oper <= N:
            # a) max 연산 이후
            if max_value > 0:
                # max 이후 갱신이 된 경우
                if counter[idx] >= max_value:
                    counter[idx] += 1
                else:
                    counter[idx] = max_value + 1
            # b) max 연산 이전
            else:
                counter[idx] += 1
            # 최대값 갱신
            if counter[idx] > tmp_max:
                tmp_max = counter[idx]
        # 2) max 연산
        elif oper == N + 1:
            max_value = tmp_max
    
    
    # 가장 최근 max 연산 결과 반영하기
    for i in range(N):
        if counter[i] < max_value:
            counter[i] = max_value
    return counter