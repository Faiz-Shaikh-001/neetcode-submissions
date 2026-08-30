class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        req_count = len(nums) // 3
        res = []
        for k, v in freq.items():
            if v > req_count:
                res.append(k)
        
        return res