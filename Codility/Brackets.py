# Codejam 에서도 푼 문제
# 유명(?)하다
# https://app.codility.com/demo/results/trainingHEKMVM-C56/

def solution(S):
    nested = 1
    if not S:
        return nested
    
    pairs = {'}':'{', ')':'(', ']':'['}
    stack = []
    for s in S:
        if (len(stack) >= 1) and (s in pairs) and pairs[s] == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(s)

    if len(stack) >= 1:
        nested = 0
    return nested