# https://app.codility.com/demo/results/training4FU7MN-VED/

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    # write your code in Python 3.6
    # convert to binay representation
    binary = []
    for _ in range(int(math.log(N, 2))):
        binary.append(N % 2)
        N = N // 2
    binary.append(N)
    binary.reverse()
    
    one_idx = []
    for i in range(len(binary)):
        if binary[i] == 1:
            one_idx.append(i)

    longest_gap = 0
    for i in range(len(one_idx) - 1):
        tmp_gap = one_idx[i + 1] - one_idx[i] - 1
        if tmp_gap > longest_gap:
            longest_gap = tmp_gap
    return longest_gap