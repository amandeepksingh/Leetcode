class Solution:
    def fib(self, n: int) -> int:
        cache = {0:0, 1:1}
        if n not in cache:
            cache[n] = self.fib(n-1) + self.fib(n-2)
        return cache[n]

