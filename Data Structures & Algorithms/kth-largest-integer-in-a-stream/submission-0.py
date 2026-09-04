class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.min_heap = nums
        self.k = k
        self.clean_up()

    def clean_up(self):
        if not self.min_heap:
            return
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        self.clean_up()
        return self.min_heap[0]
