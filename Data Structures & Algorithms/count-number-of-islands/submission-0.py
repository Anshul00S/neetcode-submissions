class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])


        visit = set()

        total = 0

        def dfs(r,c):
            if (r == ROWS or c == COLS or r < 0 
            or c < 0 or (r,c) in visit or grid[r][c] == "0"):
                return 0
            
            visit.add((r,c))

            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r,c-1)

            return 1


        
        for r in range(ROWS):
            for c in range(COLS):
                total += dfs(r,c)

        return total
            