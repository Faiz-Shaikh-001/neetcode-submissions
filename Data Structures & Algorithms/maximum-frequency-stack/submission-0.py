class FreqStack:

    def __init__(self):
        self.order = []
        self.counts = {}

    def push(self, val: int) -> None:
        self.order.append(val)
        self.counts[val] = self.counts.get(val, 0) + 1

    def pop(self) -> int:
        max_freq = max(self.counts.values())
        max_freq_elements = [k for k, v in self.counts.items() if v == max_freq]
        for i in range(len(self.order) - 1, -1, -1):
            if self.order[i] not in max_freq_elements:
                continue
            
            element = self.order.pop(i)
            self.counts[element] -= 1
            if self.counts[element] == 0:
                del self.counts[element]
            
            break
        return element

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()