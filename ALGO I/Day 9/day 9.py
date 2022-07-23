class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        visited = set()
        fresh = 0
        rotten = deque([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        
        if fresh == 0:
            return 0
        
        def bfs(q, ans, fresh):
            while q:
                lenq = len(q)
                for i in range(lenq):
                    i, j = q.popleft()
                    for tx, ty in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                        nx = tx + i
                        ny = ty + j

                        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 1:
                            grid[nx][ny] = 2
                            fresh -= 1
                            q.append((nx, ny))
                            
                    
                
                ans += 1
            
            return -1 if fresh else ans
        
        return bfs(rotten, -1, fresh)