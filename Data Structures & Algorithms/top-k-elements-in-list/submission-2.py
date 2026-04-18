class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        output = defaultdict()

        for num in nums:
            output[num] = output.get(num, 0) + 1

        return list(dict(sorted(output.items(), reverse=True, key=lambda item: item[1])))[:k]