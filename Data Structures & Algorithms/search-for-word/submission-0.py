class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        rows, cols = len(board), len(board[0])
        dircs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(row, col, idx):

            if idx == n - 1:
                return True

            temp = board[row][col]
            board[row][col] = '#'
            for r, c in dircs:
                newR = row + r
                newC = col + c
                if 0 <= newR < rows and 0 <= newC < cols and board[newR][newC] != '#' and board[newR][newC] == word[idx + 1]:
                    if dfs(newR, newC, idx + 1):
                        return True
            board[row][col] = temp

            return False

        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False



        

        