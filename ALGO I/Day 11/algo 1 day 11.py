class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n+1))
        results = []
        
        def backtrack(i, ans):
            if len(ans) == k:
                results.append(ans[:])
                return
            
            for num in nums[i:]:
                ans.append(num)
                # i+1 to control the search space vertically i.e. to use each element only once
                backtrack(i+1, ans)
                ans.pop()
                # to control the search space horizontally i.e. to only use successive elements
                i += 1
                
        backtrack(0, [])
        
        return results
