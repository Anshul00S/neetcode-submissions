class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        fresh = 0
        queue = deque()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))
        dirs = [[1, 0], [0, 1],[-1,0],[0,-1]]
        while queue and fresh > 0:

            for _ in range(len(queue)):
                canidate_location = queue.popleft()
                row = canidate_location[0]
                col = canidate_location[1]
                
                for r,c in dirs:
                    nr = row + r
                    nc = col + c

                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] != 1):
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr,nc))
            time += 1

        return time if fresh == 0 else -1




        