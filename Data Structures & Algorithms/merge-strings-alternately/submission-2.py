class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''

        small_word, large_word = word1, word2
        if len(small_word) > len(large_word):
            small_word, large_word = word2, word1
        
        for i in range(len(small_word)):
            res += word1[i] + word2[i]

        return res + large_word[len(small_word):]