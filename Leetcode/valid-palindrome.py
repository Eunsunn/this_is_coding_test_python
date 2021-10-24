# https://leetcode.com/problems/valid-palindrome/

from collections import deque
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1) My solution : O(N)
        n = len(s)
        target = ""
        for i in range(n):
            if s[i].isalpha():
                target += s[i].lower()
            elif s[i].isdigit():
                target += s[i]
        
        n_target = len(target)
        for i in range(n_target):
            if target[i] != target[n_target - 1 - i]:
                return False
        return True
    
        # 2) deque를 이용한 풀이 : O(N)
        n = len(s)
        q = deque()
        
        for char in s:
            if char.isalnum(): # isalnum() = isalpha() or isdigit()
                q.append(char.lower())
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True

        # 3) 슬라이싱을 이용해 간단하게 판별: O(N)
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # 알파벳, 숫자 외 제거
        return s == s[::-1]
            
            