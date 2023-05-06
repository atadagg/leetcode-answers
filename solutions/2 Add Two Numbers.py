# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Declare the future numbers as strings
        number1 = ""
        number2 = ""

        # Create doors for regulating empty lists
        door1 = True
        door2 = True

        # Create a while loop to convert the list into a string
        while door1 or door2:
            if l1:
                number1 = number1 + str(l1.val)
                l1 = l1.next
            else:
                door1 = False
            if l2:
                number2 = number2 + str(l2.val)
                l2 = l2.next
            else:
                door2 = False
        
        # Reverse the strings to get the correct number
        number1 = number1[::-1]
        number2 = number2[::-1]

        # Find the answer
        answer = str(int(number1) + int(number2))
        answer = str(answer[::-1])
        # Create a dummy linked list to return the answer
        result = ListNode(0)
        # pointer for the dummy node
        pointer = result

        for num in answer:
            # Create a new node with the answer's value
            new_node = ListNode(int(num))
            pointer.next = new_node
            pointer = pointer.next


        return result.next
