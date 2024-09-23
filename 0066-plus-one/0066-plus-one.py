class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        if set(digits) == set ([9]):
            return [1] + [0]*len(digits)
        
        i = 0 

        while flag:
            digits[-1 - i] = digits[-1- i] + 1
            if digits[-1 - i ] > 9: 
                if [-1 - i] == - len(digits):
                    digits.append[0]
                else: 
                    digits[-1 - i ] = digits[-1 - i ] - 10
                    i = i + 1 
            else:
                flag = False
        return digits