'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''
# Intuition: We will keep track of the frequency of all the characters in the window. If the window size - max frequency > k, we will shrink the window.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        res = 0
        l = 0
        for r in range(len(s)):
            counter[s[l]] = 1 + counter.get(s[r], 0)
            while (r-l+1) - max(counter.values()) > k:
                counter[s[l]] -= 1 # decrement the frequency of the character that's going out of the window
                l += 1 # shrink the window
            res = max(res, r-l+1)
        return res