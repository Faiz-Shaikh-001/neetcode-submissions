class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1

        if not self.stack:
            self.stack.append(price)
        elif self.stack[-1] > price:
            self.stack.append(price)
        else:
            temp = []
            while self.stack and self.stack[-1] <= price:
                temp.append(self.stack.pop())
            
            span = len(temp) + 1
            while temp:
                self.stack.append(temp.pop())
            self.stack.append(price)
        return span


            

 


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)