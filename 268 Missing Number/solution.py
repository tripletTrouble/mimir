class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0

        for i in range(len(nums)):
            if i+1 < len(nums):
                if nums[i+1] - nums[i] > 1:
                    return int((nums[i+1]+nums[i])/2)

            i+=1

        if nums[-1] > len(nums):
            return nums[-1]-1

        if nums[-1] == len(nums):
            return nums[0]-1

        return nums[-1]+1
        
