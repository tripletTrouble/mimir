from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        en = len(nums)-2
        cp = len(nums)-1
        res = False

        while en >= 0:
            print(en, en+nums[en])
            if en + nums[en] >= (len(nums)-1) or en + nums[en] >= cp:
                cp = en
                res = True
            
            if nums[en] == 0:
                res = False
            
            en-=1

        return res
        
        

