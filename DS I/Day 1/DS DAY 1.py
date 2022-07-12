class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        l = 0
        r = l + 1
        while r < len(nums):
            if nums[l] == nums[r]:
                return True
            l = l + 1
            r = l + 1
            
        return False