# 풀이 1: while 문
# https://app.codility.com/demo/results/training9FC7DP-JF9/

def solution(S):
    nested = 1
    if not S:
        return nested

    op, cl = '(', ')'
    stack = []
    for s in S:
        stack.append(s)
        while len(stack) > 1 and stack[-2] == op and stack[-1] == cl:
            stack.pop(-1)
            stack.pop(-1)
    
    if len(stack) > 0:
        nested = 0
    return nested


# 풀이 2: for문 - 최대 n번 pop하기 때문에 for문이 가능하다
# https://app.codility.com/demo/results/training52WMRM-4WD/

def solution(S):
    nested = 1
    if not S:
        return nested
    
    op, cl = '(', ')'
    stack = []
    for s in S:
        if len(stack) > 0 and s == cl and stack[-1] == op:
            stack.pop(-1)
        else:
            stack.append(s)

    if len(stack) > 0:
        nested = 0
    return nested