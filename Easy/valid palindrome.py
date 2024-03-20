'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert to lowercase and remove non-alphanumeric characters
        s = s.lower()
        newStr = ""
        for ch in s:
            if ch.isalnum():
                newStr += ch
        # return true if the string is the same as its reverse
        return newStr == newStr[::-1]
        