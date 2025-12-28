from typing import List


class Solution:
    def countNegatives2(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        i = n - 1
        j = 0
        res = 0

        while i >= 0 and j < m:
            if grid[i][j] < 0:
                res += m - j
                i -= 1
            else:
                j += 1
        return res

    def countNegatives1(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        i = 0
        j = 0

        res = 0

        while i < n:
            check_num = grid[i][j]

            if check_num < 0:
                res += 1

            if j < m:
                j += 1

            if j >= m:
                i += 1
                j = 0

        return res


print(
    Solution().countNegatives(
        grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    )
)
