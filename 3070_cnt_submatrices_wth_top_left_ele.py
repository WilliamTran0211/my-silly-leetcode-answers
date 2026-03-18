from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]
                if i > 0 and j > 0:
                    grid[i][j] -= grid[i - 1][j - 1]

        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] <= k:
                    count += 1
        return count


print(Solution().countSubmatrices([[7, 6, 3], [6, 6, 1]], 18))
