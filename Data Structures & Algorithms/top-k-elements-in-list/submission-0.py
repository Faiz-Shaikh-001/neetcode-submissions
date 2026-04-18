class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        counts = []

        for num in nums_set:
            counts.append((num, nums.count(num)))

        counts = sorted(counts, key=lambda count: count[1], reverse=True)
        result = [counts[i][0] for i in range(k)][::-1]
        
        return result