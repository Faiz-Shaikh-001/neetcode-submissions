class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq

        counts = Counter(nums)
        return heapq.nlargest(k, counts, key=counts.get)