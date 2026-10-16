class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
            return False
        
        counter = {}
        for letter in s:
            if letter in counter:
                counter[letter] += 1
            else:
                counter[letter] = 1
                

        for letter in t:
            if letter not in counter:
                return False
            else: 
                counter[letter] -= 1

        for letter in counter:
            if counter[letter] != 0:
                return False
        
        return True

        