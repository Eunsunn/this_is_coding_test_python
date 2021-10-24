# https://leetcode.com/problems/group-anagrams/
# from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # n = len(strs), m = max(len(strs[i]))
        # O(n * mlog(m))
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return list(groups.values())

        # # My solution: 시간초과
        # # anagram: 어떤 문자가 몇번 나왔냐
        # groups = [] # anagram 그룹들
        # cnts = [] # 각 그룹별 문자가 몇번 나왔는지
        
        # # word가 들어갈 그룹 인덱스를 찾는다
        # def find_group(word):
        #     cur_cnt = Counter([char for char in word])
        #     ret = -1
        #     for g_idx in range(len(groups)):
        #         g_cnt = cnts[g_idx]
        #         if len(cur_cnt) != len(g_cnt):
        #             continue
        #         find = True
        #         # 단어 알파벳 -> anagram group 알파벳 비교
        #         for char in cur_cnt:
        #             if char not in g_cnt:
        #                 find = False
        #                 break
        #             if cur_cnt[char] != g_cnt[char]:
        #                 find = False
        #                 break
        #         # anagram group 알파벳 -> 단어 알파벳 비교
        #         for char in g_cnt:
        #             if char not in cur_cnt:
        #                 find = False
        #                 break
        #             if cur_cnt[char] != g_cnt[char]:
        #                 find = False
        #                 break
        #         if find:
        #             ret = g_idx
        #             break
        #     return ret
        
        # # 애너그램을 만든다
        # for word in strs:
        #     g_idx = find_group(word)
        #     if g_idx == -1:
        #         groups.append([word])
        #         cnts.append(dict(Counter([char for char in word])))
        #     else:
        #         groups[g_idx].append(word)
        # return groups


sol = Solution()
# strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
strs = ["a"]

print(sol.groupAnagrams(strs))