class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # Return empty list if not digits
        if not digits:
            return []
        
        num_dict = {"2":["a", "b","c"],
                   "3":["d", "e", "f"],
                   "4":["g", "h", "i"],
                   "5":["j", "k", "l"],
                   "6":["m", "n", "o"],
                   "7":["p", "q", "r", "s"],
                   "8":["t", "u", "v"],
                   "9":["w", "x", "y", "z"]}
        
        # List to hold the intermediate result in recursion call
        collection = []
        
        # Base case of recursion. When digits = 1, return the direct mapping
        if len(digits) == 1:
            return num_dict[digits]
        
        # Recursively call the function until len(digits) == 1 and get base case
        combination = self.letterCombinations(digits[1:])
        
        # After recursive call, combine the first char with the combinration result in recusive call 
        char_list = num_dict[digits[0]]
        
        # For the char list of extra char
        for char in char_list: 
            # For all combinration result
            for com_char in combination:
                # Put the char before combinration result as it represents an earlier digits
                collection.append(char + com_char)
                    
        return collection