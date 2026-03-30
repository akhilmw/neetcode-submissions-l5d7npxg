class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                key = board[r][c]
                if key == ".":
                    continue
                if (key in rows[r] or key in cols[c] or key in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(key)
                cols[c].add(key)
                squares[(r // 3, c // 3)].add(key)
        

        return True
        