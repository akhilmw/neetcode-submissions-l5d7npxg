class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        dircs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col, 0))

        while queue:
            r, c, d = queue.popleft()
            for dr, dc in dircs:
                newR = r + dr
                newC = c + dc
                if 0 <= newR < rows and 0 <= newC < cols:
                    if grid[newR][newC] == 2147483647:
                        grid[newR][newC] = d + 1
                        queue.append((newR, newC, d + 1))
            
