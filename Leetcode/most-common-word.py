# https://leetcode.com/problems/most-common-word

import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 1) My solution
        ban_set = set([ban.lower() for ban in banned])
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-z]', ' ', paragraph)
        
        cnt = {}
        for word in paragraph.split():
            if (not word) or (word in ban_set):
                continue
            if word in cnt:
                cnt[word] += 1
            else:
                cnt[word] = 0
        
        words = list(cnt.keys())
        words.sort(key=lambda x: cnt[x], reverse=True)
        return words[0]
    
        # 2) Counter solution
        # 단어(\w)가 아닌(^) 문자를 공백으로 정규표현식 후 lower, split
        words = [word for word in re.sub(r'[^\w]', '', paragraph).lower().split()
                if word not in banned]
        
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]