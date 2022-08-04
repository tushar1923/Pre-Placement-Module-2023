class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]=="0":
                return 
            grid[i][j] = "0"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        island =0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    island+=1
                    dfs(i,j)
        return island
