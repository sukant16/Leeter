from typing import List
from itertools import product


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        empty = 0
        m, n = len(grid), len(grid[0])

        def dfs_paths(x, y, rem, visited):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] < 0 or rem < 0:
                return
            if grid[x][y] == 2 and rem == 0:
                self.ans += 1
            if (x, y) in visited:
                return

            visited.add((x,y))
            nebors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dx, dy in nebors:
                temp = grid[x][y]
                grid[x][y] = -2
                dfs_paths(x+dx, y+dy, rem-1, visited)
                grid[x][y] = temp
            visited.discard((x, y))

        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                sx, sy = i, j
            if grid[i][j] != -1:
                empty += 1
        dfs_paths(sx, sy, empty-1, set() )
        return self.ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
    print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
