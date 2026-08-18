class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        global_max = 0 
        rows = len(grid)
        cols = len(grid[0])
        visit = set()    

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0 or (r,c) in visit):
                return 0
            
            visit.add((r,c))
            area = 1
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            for d_r,d_c in directions:
                area += dfs(r+ d_r,c+ d_c)

            return area


        def bfs(r,c):
            stack = [(r,c)]
            visit.add((r,c))
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            size = 1

            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (0 <= nr and 0 <= nc and rows > nr and cols > nc and (nr,nc) not in visit and grid[nr][nc] == 1):
                        stack.append((nr,nc))
                        visit.add((nr,nc))
                        size += 1

            return size



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    global_max = max(global_max, bfs(r, c))



        return global_max