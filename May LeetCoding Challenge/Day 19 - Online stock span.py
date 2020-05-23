class StockSpanner:

    def __init__(self):
        self.s = []
        
    def next(self, price: int) -> int:
        w = 1
        while self.s and self.s[-1][0] <= price:
            w += self.s.pop()[1]
        self.s.append((price, w))
        return w
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
