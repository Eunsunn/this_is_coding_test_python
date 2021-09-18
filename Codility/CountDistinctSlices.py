# https://app.codility.com/demo/results/training9ZF5HE-G8B/

def solution(M, A):
    n = len(A)
    max_val = int(1e9)

    # O(N)
    # A[i]와 값이 같은 가장 큰 인덱스 (i 이하)
    collision_idx = [-1] * n
    collision_dict = {} # 값 : 인덱스
    for i in range(n):
        if A[i] in collision_dict:
            collision_idx[i] = collision_dict[A[i]]
        collision_dict[A[i]] = i
    
    # O(N)
    # [임의의 인덱스, end_idx] 경우의 수 세기 (start_idx <= 임의 인덱스 <= end_idx) (양쪽 인덱스를 포함하는 slice)
    # <=> 범위에서 임의의 인덱스를 선택하는 경우의 수
    cnt = 0
    start_idx = 0
    for end_idx in range(n):
        # 충돌이 난 경우 start_idx를 증가시킨다 (if문 생략해도 동일)
        # if collision_idx[end_idx] > -1: 
        start_idx = max(start_idx, collision_idx[end_idx] + 1)
        cnt += (end_idx - start_idx + 1)
        # 조기종료
        if cnt > max_val:
            cnt = max_val
            break
    return cnt