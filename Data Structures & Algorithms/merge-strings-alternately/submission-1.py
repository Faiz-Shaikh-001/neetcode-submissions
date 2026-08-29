class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0

        small_word, large_word = word1, word2
        if len(small_word) > len(large_word):
            small_word, large_word = word2, word1
        
        while i < len(small_word):
            res += word1[i] + word2[i]
            i += 1

        return res + large_word[i:]