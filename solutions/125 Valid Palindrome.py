# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(filter(str.isalnum, s))

        new_s = new_s.lower()
        reverse_s = new_s[::-1]

        if new_s == reverse_s:
            print(new_s, reverse_s)
            return True
        else:
            return False
