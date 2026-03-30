class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        col_set = set()
        right_diagonal = set()
        left_diagonal = set()
        ans = []
        def place(row):
            
            if row == n:
                copy = ["".join(r) for r in board]
                ans.append(copy)
                return

            for col in range(n):
                if col not in col_set and (row + col) not in right_diagonal and (row - col) not in left_diagonal:
                    board[row][col] = 'Q'
                    col_set.add(col)
                    right_diagonal.add(row + col)      
                    left_diagonal.add(row - col)
                    place(row + 1)
                    board[row][col] = '.'
                    col_set.remove(col)
                    right_diagonal.remove(row + col)      
                    left_diagonal.remove(row - col)
        
        place(0)

        return ans
            