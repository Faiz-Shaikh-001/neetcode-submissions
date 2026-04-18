class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        freq = list(counts.items())
        freq = sorted(freq, key=lambda x: x[1], reverse=True)
        return [num for num, _ in freq[:k]][::-1]