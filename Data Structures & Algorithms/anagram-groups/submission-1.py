class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            if len(strs) <= 1:
                return [strs]
            
            final_arr = []

            while len(strs) != 0:
                current_string = strs[0]
                temp_arr = []
                indexes_to_remove = []

                for i, s in enumerate(strs):
                    if self.isAnagram(current_string, s):
                        indexes_to_remove.append(i)
                        temp_arr.append(s)

                strs = self.remove_values(strs, indexes_to_remove)
                final_arr.append(temp_arr)
            
            final_arr = sorted(final_arr, key=len)
            return final_arr


    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}

        for i in range(len(s)):
            # inititalize the key with a value 1 or add the previous value if available 
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        return count_s == count_t
    
    def remove_values(self, s, i):
        indexes = i[::-1]
        for x in indexes:
            s.pop(x)

        return s