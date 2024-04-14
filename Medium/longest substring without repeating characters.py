'''
Given a string s, find the length of the longest substring without repeating characters
'''
# Intuition: Sliding window approach, initialize one pointer at the beginning and use another pointer to iterate through the string.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l]) # remove the element at the beginning of the window
                l += 1
            hashset.add(s[r])
            res = max(res, r-l+1)
        return res