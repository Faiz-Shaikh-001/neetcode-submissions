# input: two string s and t
# output: boolean value true if it is an anagram or false if it isn't
# logic: hash_table that can contain all the values of the string s and how many occurences the value has
# length of the strings must be equal


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_table = {}

        for char in s:
            if char not in hash_table:
                hash_table[char] = 1
                continue
            hash_table[char] += 1

        for char in t:
            if char not in hash_table:
                return False
            hash_table[char] -= 1
        
        for key in hash_table:
            if hash_table[key] != 0:
                return False
            
        return True