#I'm lowkey proud

#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       # Converting the list into a set because every element of a set has to be unique then converting it back into a list
        res = [*set(nums)] 
       # And comparing the length of the list we made and the original list's lengths to know if there were any duplicate numbers
        if len(res) != len(nums):
            return True
        else:
            return False
