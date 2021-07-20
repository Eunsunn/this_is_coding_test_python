# https://app.codility.com/demo/results/training4J6YHP-927/
# large_max : 0.244s
def solution(H):
    n = len(H)
    check = [False] * n
    sorted_idx = sorted(range(n), key=lambda x: H[x])
    cnt = 0
    # 최악의 경우(피라미드) 처리: O(N**2) -> O(N)
    # 단조 증감 구간을 찾는다
    def find_monotonous():
        n = len(H)  
        inc, dec = [], []
        for i in range(len(H) - 1):
            if H[i] <= H[i + 1]:
                inc.append(i)
            else:
                dec.append(i)
        if n > 1:
            if H[-2] <= H[-1]:
                inc.append(n)
            else:
                dec.append(n)
        return inc, dec
    inc, dec = find_monotonous()
    if inc and dec and inc[-1] < dec[0]:
        return len(set(H))

    # 가장 낮은 높이 쌓기
    check[sorted_idx[0]] = True
    cnt += 1
    # 낮은 높이부터 쌓기
    for i in range(1, n):
        idx1, idx2 = sorted_idx[i - 1], sorted_idx[i]
        check[idx2] = True
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        # 직전과 높이가 같고, 그 사이에 낮은 높이가 없는 경우 -> 추가 블럭 x
        if H[idx1] == H[idx2] and sum(check[idx1 + 1 : idx2]) == 0:
            continue
        cnt += 1
    return cnt
            
        

# https://app.codility.com/demo/results/training7NDUTS-JW8/
# large_max: 0.388s
# 왜 얘가 더 느리지: 시간복잡도는 동일, check의 대입때문에??
def solution(H):
    n = len(H)
    check = 1 << (n + 1) # check bitmask
    sorted_idx = sorted(range(n), key=lambda x: H[x])
    cnt = 0

    # check의 i번째를 1로 바꾼다 (O(1))
    def update_check(check, i):
        return check | (1 << i)
    # [i, j]에 True가 있는지 확인한다 (i < j) (O(??))
    def check_interval(check, i, j):
        if i > j:
            return 0
        mask = int(2 ** (j - i + 1) - 1)
        mask = mask << i # 아마 O(N)
        return check & mask # 아마 O(N)
    
    # 최악의 경우(피라미드) 처리 : O(N**2) -> O(N)
    def find_monotonous():
        n = len(H)
        inc, dec = [], []
        for i in range(n - 1):
            if H[i] <=  H[i + 1]:
                inc.append(i)
            else:
                dec.append(i)
        if n > 1:
            if H[-2] <= H[-1]:
                inc.append(n)
            else:
                dec.append(n)
        return inc, dec
    inc, dec = find_monotonous()
    if inc and dec and inc[-1] < dec[0]:
        return len(set(H))

    # 가장 낮은 높이 쌓기
    check = update_check(check, sorted_idx[0])
    cnt += 1
    # 낮은 높이부터 쌓기
    for i in range(1, n):
        idx1, idx2 = sorted_idx[i - 1], sorted_idx[i]
        check = update_check(check, idx2)
        if idx1 > idx2:
            idx1, idx2 = idx2, idx1
        # 이전 블럭과 높이가 같고, 두 블럭 사이에 낮은게 없음 -> 추가 블럭 x
        if H[idx1] == H[idx2] and check_interval(check, idx1 + 1, idx2 - 1) == 0:
            continue
        cnt += 1
    return cnt