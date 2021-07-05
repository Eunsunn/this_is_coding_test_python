# https://app.codility.com/demo/results/trainingPGJ2NK-J9Z/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    max_n = int(1e6)
    occur = [False] * (max_n + 1)
    for i in A:
        if i > 0:
            occur[i] = True
    
    for i in range(1, max_n + 1):
        if occur[i] == False:
            return i