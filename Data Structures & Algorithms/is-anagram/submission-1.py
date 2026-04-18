# input: two string s and t
# output: boolean value true if it is an anagram or false if it isn't
# logic: hash_table that can contain all the values of the string s and how many occurences the value has
# length of the strings must be equal


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            # inititalize the key with a value 1 or add the previous value if available 
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        return count_s == count_t