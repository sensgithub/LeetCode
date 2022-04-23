class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = 0 # start 
        curr_char = 0 #index
        max_len = 0  #the max length of the string
        dictionary = {} # dictionary to follow the index throughout
            
        # while current char(index) is not equal to the length of the string
        while curr_char < len(s):
            
            # check the position of the index in the dictionary 
            # and whether the position of the index in the dictionary is higher or equal to the start
            if s[curr_char] in dictionary and dictionary[s[curr_char]] >= start:
                # update start
                start = dictionary[s[curr_char]] + 1
            # max length 
            max_len = max(max_len, curr_char - start + 1)
            # update current character
            # and increment it each time 
            dictionary[s[curr_char]] = curr_char
            curr_char += 1
            
        #finally return the max length
        return max_len