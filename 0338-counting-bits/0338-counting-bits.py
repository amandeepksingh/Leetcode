class Solution:
    def countBits(self, n: int) -> List[int]: 
        arr = [0] * (n + 1)
        c = 0
        for i in range(1, n + 1):
            for _ in range(32):
                # bit shifting is the same as halfing 
                # countBits(n) = countBits(2n)
                # countBits(n) + 1 = countBits(2n+1)
                # so get the number of bits in half and then add 1 if odd else l
                arr[i] = arr[i >> 1] + (i&1)
        return arr