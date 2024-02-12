from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        res = [0 for _ in nums]
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        i = 2

        while i < len(nums):
            res[i] = max(res[i-2] + nums[i], res[i-1])
            i+=1
        
        return res[-1]


        
        