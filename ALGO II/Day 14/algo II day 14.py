class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        total, count, num = 0, 1, nums[0] - nums[1]
        for i in range(2, len(nums)):
            diff = nums[i-1] - nums[i]
            if num == diff:
                count += 1
            else:
                num = diff
                if count > 1:
					# this is just a math formula. When you reach the end of subarray, use it
                    total += (count + 1)*(count - 2)//2 + 1
                    count = 1                
        if count > 1:
            total += (count + 1)*(count - 2)//2 + 1
            
        return total
 