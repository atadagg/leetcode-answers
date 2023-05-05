# Given a roman numeral, convert it to an integer.


class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary that maps each Roman numeral to its integer value
        roman_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        
        # Initialize the total number to 0
        total = 0
        
        # Loop through the string
        for i in range(len(s)):
            # Get the integer value of the current character from the dictionary
            curr_value = roman_dict[s[i]]
            
            # If the next character is larger than the current one, subtract the current value from the total
            if i < len(s)-1 and roman_dict[s[i+1]] > curr_value:
                total -= curr_value
            # Otherwise, add it to the total
            else:
                total += curr_value
        
        # Return the total
        return total
