# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        reversed_string = string[::-1]
        return string == reversed_string
