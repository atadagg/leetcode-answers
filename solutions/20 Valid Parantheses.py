#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

 #   Open brackets must be closed by the same type of brackets.
 #   Open brackets must be closed in the correct order.
 #   Every close bracket has a corresponding open bracket of the same type.






class Solution:
    def isValid(self, s: str) -> bool:
        
        opening_brackets = "([{"
        closing_brackets = ")]}"

        stack = []
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in closing_brackets:
                if not stack or stack.pop() != opening_brackets[closing_brackets.index(char)]:
                    return False
        

        return len(stack) == 0
