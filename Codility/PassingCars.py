# https://app.codility.com/demo/results/trainingB63AG2-7AQ/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # base case: no pair
    if len(A) == 1:
        return 0
    
    n = len(A)
    west_cnt = 0
    pairs = 0
    for i in range(n):
        # 조기종료
        if pairs > int(1e9):
            pairs = -1
            break
        if A[i] == 0:
            west_cnt += 1
        else:
            pairs += west_cnt
    return pairs
    