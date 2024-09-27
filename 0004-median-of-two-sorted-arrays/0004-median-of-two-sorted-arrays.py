class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # brute force 
        n1, n2 = 0, 0
        combined = []
        while n1 != len(nums1) or n2 != len(nums2):
            if n1 != len(nums1) and n2 != len(nums2):
                combined.append(min(nums1[n1], nums2[n2]))
                if nums1[n1] < nums2[n2]:
                    n1 = n1 + 1
                else:
                    n2 = n2 + 1
            else:
                if n1 == len(nums1):
                    combined.append(nums2[n2])
                    n2 += 1
                else:
                    combined.append(nums1[n1])
                    n1 += 1
        if len(combined) % 2 != 0:
            return combined[len(combined)//2]
        return (combined[len(combined)//2] + combined[(len(combined)//2)  - 1])/2

        