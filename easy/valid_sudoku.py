from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(dict)
        cols = defaultdict(dict)
        boxes = defaultdict(dict)
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                box_id = i // 3 * 3 + j // 3
                if num != ".":
                    if num in rows[i] or num in cols[j] or num in boxes[box_id]:
                        return False
                    else:
                        rows[i][num] = 1
                        cols[j][num] = 1
                        boxes[box_id][num] = 1
        return True


if __name__ == '__main__':
    sol = Solution()
    inp = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(inp))

    inp2 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(inp2))