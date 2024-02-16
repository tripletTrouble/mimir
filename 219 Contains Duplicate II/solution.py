class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        x = {
            nums[0]: 0
        }

        i = 1
        for i in range(i, len(nums)):
            if x.get(nums[i]) != None:
                dis = i - x.get(nums[i])

                if dis <= k:
                    return True

            x[nums[i]] = i
            i+=1

        return False
