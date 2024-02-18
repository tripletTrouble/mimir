class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            ri = 0
        
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[ri] = nums[i]
                    if ri != i:
                        nums[i] = 0
                    ri+=1
