from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        pre_x = [[0 for _ in range(m)] for _ in range(n)]
        pre_y = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                pre_x[i][j] = (
                    (1 if grid[i][j] == "X" else 0)
                    + (pre_x[i - 1][j] if i > 0 else 0)
                    + (pre_x[i][j - 1] if j > 0 else 0)
                    - (pre_x[i - 1][j - 1] if (i > 0 and j > 0) else 0)
                )

                pre_y[i][j] = (
                    (1 if grid[i][j] == "Y" else 0)
                    + (pre_y[i - 1][j] if i > 0 else 0)
                    + (pre_y[i][j - 1] if j > 0 else 0)
                    - (pre_y[i - 1][j - 1] if (i > 0 and j > 0) else 0)
                )
        count = 0
        for i in range(n):
            for j in range(m):
                if pre_x[i][j] == pre_y[i][j] and pre_x[i][j] > 0:
                    count += 1
        return count


print(Solution().numberOfSubmatrices([["X", "Y", "."], ["Y", ".", "."]]))
