from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0]*m for i in range(n)]
        for i, j in indices:
            mat[i] = [k+1 for k in mat[i]]
            for l in range(n):
                mat[l][j] += 1
        return sum([sum(map(lambda x: x%2, row)) for row in mat])
    
if __name__ == '__main__':
    sol = Solution()

    ans1 = sol.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]])
    assert (ans1 == 6), 'wrong'

    ans2 = sol.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]])
    assert (ans2 == 0), 'wrong'
