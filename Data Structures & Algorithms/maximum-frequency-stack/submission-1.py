class FreqStack:

    def __init__(self):
        self.count = {}
        self.group = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        self.max_freq = max(self.max_freq, self.count[val])
        if self.max_freq not in self.group:
            self.group[self.max_freq] = []
        self.group[self.count[val]].append(val)

    def pop(self) -> int:
        element = self.group[self.max_freq].pop()
        if not self.group[self.max_freq]:
            del self.group[self.max_freq]
            self.max_freq -= 1
        self.count[element] -= 1
        return element

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()