class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows, cols = len(grid), len(grid[0])
        dircs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        INF = 2147483647
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))

        while queue:
            
            row, col = queue.popleft()
            for r, c in dircs:
                new_r = row + r
                new_c = col + c
                if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == INF:
                    grid[new_r][new_c] = grid[row][col] + 1
                    queue.append((new_r, new_c))





