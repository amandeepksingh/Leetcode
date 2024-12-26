class Solution:
    def hammingWeight(self, n: int) -> int:
        ct = 0
        for _ in range(32):
            ct = ct + int(n&1)
            n = n >> 1
        return ct 