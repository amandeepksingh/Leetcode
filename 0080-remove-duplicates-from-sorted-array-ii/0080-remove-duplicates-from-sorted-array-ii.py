class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        freq_dict = dict()
        for i in range(len(nums)): 
            if freq_dict.get(nums[i], 0) < 2:
                print("at", nums[i])
                print("k", k)
                nums[k] = nums[i]
                k = k + 1
                freq_dict[nums[i]] = freq_dict.get(nums[i], 0) + 1
                print(freq_dict[nums[i]])
            elif freq_dict.get(nums[i], 0) >= 2:
                print("else")
                
            print(nums)
        return k

            

