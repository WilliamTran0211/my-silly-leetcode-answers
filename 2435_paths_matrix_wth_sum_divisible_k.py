from typing import List


class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        row, col = len(grid), len(grid[0])

        cache = [[[-1] * k for _ in range(col)] for _ in range(row)]
        MOD = 10**9 + 7

        def dfs(r, c, remain):
            if r == row - 1 and c == col - 1:
                remain = (remain + grid[r][c]) % k
                return 0 if remain else 1
            if r == row or c == col:
                return 0
            if cache[r][c][remain] > -1:
                return cache[r][c][remain]

            cache[r][c][remain] = dfs(r + 1, c, (remain + grid[r][c]) % k) + dfs(
                r, c + 1, (remain + grid[r][c]) % k
            )

            return cache[r][c][remain]

        return dfs(0, 0, 0) % MOD


print(Solution().numberOfPaths([[5, 2, 4], [3, 0, 5], [0, 7, 2]], 3))
