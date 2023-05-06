#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".





class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # declare a number of letters for the prefix
        prefix = 0
        # exception if there is only one word in the list
        if len(strs) == 1:
            return strs[0]
        
        # iterate over each character in the first string
        for i, char in enumerate(strs[0]):
            # check if the character is in all other strings
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != char:
                    # if the character is not in all strings, return the prefix
                    return strs[0][:prefix]
            # if the character is in all strings, increase the prefix length
            prefix += 1

        # Finish
        answer = strs[0][:prefix]
        return answer
