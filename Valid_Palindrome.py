class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if not s:
            return True
        s1 = ""
        for i in s:
            if ord('A') <= ord(i) <= ord('z') or i.isdigit():
                s1 += i
        start = 0
        end = len(s1) - 1
        while start <= end:
            if s1[start].lower() != s1[end].lower():
                return False
            start += 1
            end -= 1

        return True

