# https://app.codility.com/demo/results/trainingYMY3AQ-NJC/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    neg, pos, zero = [], [], False
    for element in A:
        if element < 0:
            neg.append(element)
        elif element > 0:
            pos.append(element)
        else:
            zero = True
    
    if neg:
        neg.sort()
    if pos:
        pos.sort()
        
    answer = -int(1e9)
    if zero:
        answer = 0
    if len(pos) >= 3:
        tmp_answer = pos[-1] * pos[-2] * pos[-3] # 큰 양수 3개
        answer = max(answer, tmp_answer)
    if len(neg) >= 3:
        tmp_answer = neg[-1] * neg[-2] * neg[-3] # 절댓값 작은 음수 3개
        answer = max(answer, tmp_answer)

    if len(neg) >= 2:
        if len(pos) >= 1:
            tmp_answer = neg[0] * neg[1] * pos[-1] # 절대값 큰 음수 2개 * 큰 양수 1개
            answer = max(answer, tmp_answer)
    elif len(neg) == 1:
        if len(pos) >= 2:
            tmp_answer = pos[0] * pos[1] * neg[-1] # 절대값 작은 양수 2개 * 절대값 작은 음수 1개
            answer = max(answer, tmp_answer)

    return answer