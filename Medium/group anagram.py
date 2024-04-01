'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # To avoid raising a key error, we'll use defaultdict, and use list as default store
        res = defaultdict(list)
        for st in strs:
            count = [0]*26
            # count the occurences of each letter for every string
            for ch in st:
                count[ord(ch)-ord("a")] += 1
            # use the count as the key and the word as the val
            res[tuple(count)].append(st)
        return res.values()