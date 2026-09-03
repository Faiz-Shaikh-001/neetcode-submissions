class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_count = {}
        prefix_count[0] = 1
        res = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
            res += prefix_count.get(remainder, 0)
            prefix_count[remainder] = prefix_count.get(remainder, 0) + 1
        
        return res