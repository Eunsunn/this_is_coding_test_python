# https://app.codility.com/demo/results/training6J5GHX-44W/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # 각 위치에 나뭇잎이 떨어졌는지
    leaves = [False] * (X + 1)
    cnt = 0 # 나뭇잎이 떨어진 개수 (각 위치마다 한번만 카운트) 
    for i in range(len(A)):
        loc = A[i] # 떨어지는 위치 (1 <= loc <= X)
        if leaves[loc] == False:
            leaves[loc] = True
            cnt += 1
        if cnt == X:
            return i
    return -1