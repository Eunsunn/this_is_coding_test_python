# https://leetcode.com/problems/longest-palindromic-substring/submissions/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for size in range(n, 1, -1):
            for i in range(n - size + 1):
                target = s[i : i + size]
                if target == target[::-1]:
                    return target
        return s[0]