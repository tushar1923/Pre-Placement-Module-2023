class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        def dfs(i, curr):
            if i >= len(nums):
                return 
            curr.append(nums[i])
            res.append(curr.copy())
            dfs(i+1, curr)
            curr.pop()
            dfs(i+1, curr)
            
            
        dfs(0, [])
        
        return res
