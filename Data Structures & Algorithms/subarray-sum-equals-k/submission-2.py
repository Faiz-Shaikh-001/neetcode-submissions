class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        hashmap = {0: 1}
        prefixSum = 0
        for num in nums:
            prefixSum += num
            if prefixSum - k in hashmap:
                ans += hashmap[prefixSum - k]
            hashmap[prefixSum] = hashmap.get(prefixSum, 0) + 1
        return ans