# https://app.codility.com/demo/results/trainingS6T5XF-JEC/

# 부호를 조작한 합의 절대값을 최소화
# <=> 전체 합에서 각 원소를 2배씩 뺀 값의 절댓값 최소화
# <=> 부분합을 (모든 원소 절대값의 합) // 2 에 가깝게 만든다

def solution(A):
    n = len(A)
    # base case: n=0 -> val=0
    if n == 0:
        return 0

    abs_ls = [abs(A[i]) for i in range(n)] # 절대값 리스트
    max_abs = max(abs_ls) # 절대값의 최대값
    count = [0] * (max_abs + 1) # 절대값 원소의 개수
    for val in abs_ls:
        count[val] += 1
    
    abs_sum = sum(abs_ls) # 절대값의 합
    dp = [-1] * (abs_sum + 1) # 각 수를 만들 수 있는지 여부
    dp[0] = 0

    # 절대값이 작은 수부터 더해가면서 부분합을 만든다
    for val in range(1, max_abs + 1):
        # 절대값이 존재하는 수를 본다
        if count[val] > 0:
            for partial_sum in range(abs_sum): # 만들 수
                # 1) 이미 만든 경우 -> val이 필요 없으므로 count[val] 개수만큼 남음
                if dp[partial_sum] >= 0:
                    dp[partial_sum] = count[val]
                # 2) val을 더해 partial_sum을 만드는 경우
                elif (partial_sum >= val and dp[partial_sum - val] > 0):
                    dp[partial_sum] = dp[partial_sum - val] - 1

    # 절반까지 순회하면서 정답을 찾는다
    ret = abs_sum
    for i in range(abs_sum // 2 + 1):
        if dp[i] >= 0:
            ret = min(ret, abs_sum - 2 * i)
    return ret


# 무수한 시도들
# greedy, 투포인터, BFS or 재귀를 통한 완전탐색 등
# abs_sum // 2 까지 근사하는 아이디어를 생각했지만
# 더하는 부분을 해결하지 못함...

# https://app.codility.com/demo/results/training3HYJND-B6P/
# https://app.codility.com/demo/results/training2M7X6C-FJG/
# https://app.codility.com/demo/results/training2SKK9S-ZFK/
# https://app.codility.com/demo/results/training5AJQEE-EUJ/
# https://app.codility.com/demo/results/trainingAARAN6-RDU/
# https://app.codility.com/demo/results/trainingZM363G-M83/
# https://app.codility.com/demo/results/trainingSHU3N8-HCC/
# https://app.codility.com/demo/results/training26JSEU-QCB/
