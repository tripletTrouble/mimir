from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        u = nums[0]

        for i in range(1, len(nums)):
            if i+1 < len(nums):
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    u = nums[i]
            if i == len(nums)-1:
                if nums[i] != nums[i-1]:
                    u = nums[i]

        return u
        