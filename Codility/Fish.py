# https://app.codility.com/demo/results/trainingD552M2-8XX/

def solution(A, B):
    # stack = [[size, direction]]
    stack = []
    
    def eat_fist():
        # 더이상 잡아먹을 물고기가 없을 때까지 반복
        while len(stack) > 1 and stack[-2][1] == 1 and stack[-1][1] == 0:
                # 앞 물고기가 큰 경우
                if stack[-2][0] > stack[-1][0]:
                    stack.pop(-1)
                # 뒤 물고기가 큰 경우
                else:
                    stack.pop(-2)
    
    for i in range(len(A)):
        stack.append([A[i], B[i]])
        eat_fist()
    return len(stack)