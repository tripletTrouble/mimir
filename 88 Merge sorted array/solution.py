from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            i = 0
            while i < m+n:
                nums1[i] = nums2[i]
                i+=1

        if n > 0 and m > 0:
            i = 0
            j = 0
            lm = len(nums1)
            while i < lm and j < n:
                if nums1[i] == 0 and i >= m:
                    nums1[i] = nums2[j]
                    j+=1
                    i+=1
                    continue
                    
                if nums2[j] <= nums1[i]:
                    x = lm-1
                    while x >= i:
                        nums1[x] = nums1[x-1]
                        x-=1
                    nums1[i] = nums2[j]
                    j+=1
                    m+=1
                i+=1

        return nums1
        

        