class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        
        def dfs(i):
            if i == N - 1:
                return 0
            
            if nums[i] == 0:
                return float('inf')
            
            num_jumps = float('inf')
            for j in range(i + 1, min(i + nums[i] + 1, N)):
                num_jumps = min(num_jumps, dfs(j) + 1)
            
            return num_jumps
        
        return dfs(0)
