class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_n = 0 
        # int so 32 bit
        for _ in range(32):
            # get least significant bit of n 
            # get the new bit pos of reversed n and or the lsb of n
            reversed_n = (reversed_n << 1 ) | (n&1)
            # shift n 
            n = n >> 1
        return reversed_n