# https://leetcode.com/problems/reverse-string/

from copy import deepcopy

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # My solution : O(N)
        n = len(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return s
    
        # # Pythonic solution: O(N)
        # return s.reverse()
        
        # # Wrong Answer
        # return s[::-1] # local에서는 된다..! (왜???)

s = ["h", "e", "l", "l", "o"]
s = ["ab", "cd", "ef", "gh"]