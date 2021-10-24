# https://leetcode.com/problems/reorder-data-in-log-files

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # My solution : 신기하게 풀이랑 똑같다 ㅋㅋ
        # n = len(logs), m = max(len(logs[i])) 일 때
        # O(NM)
        letter, digit = [], []
        for i in range(len(logs)):
            if logs[i].split()[1].isalpha():
                letter.append(logs[i])
            else:
                digit.append(logs[i])
        
        # O(???)
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        letter.extend(digit)
        return letter