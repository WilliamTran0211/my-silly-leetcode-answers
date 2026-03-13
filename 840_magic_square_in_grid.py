from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # magic grid (Ma Phương): the center must be 5
        # The total sum of the [1,2,3,..,9] = 45.
        # And the problem limit the grid are 3x3, that mean the total sum spilt into 3 =  15. This call Magic Constant (M)
        # cause 5 are in [1,2,3...,9] and we can only build 4 set with using all of the numbers from 1 to 9
        # that also mean that all number at the conner must be even
        res = 0
        for r in range(n - 2):
            for c in range(m - 2):
                if grid[r + 1][c + 1] != 5:
                    continue
                else:
                    corners = [
                        grid[r][c],
                        grid[r][c + 2],
                        grid[r + 2][c],
                        grid[r + 2][c + 2],
                    ]
                    if all(x % 2 == 0 for x in corners):
                        res += 1

        return res


print(
    Solution().numMagicSquaresInside(
        [
            [9, 9, 5, 1, 9, 5, 5, 7, 2, 5],
            [9, 1, 8, 3, 4, 6, 7, 2, 8, 9],
            [4, 1, 1, 5, 9, 1, 5, 9, 6, 4],
            [5, 5, 6, 7, 2, 8, 3, 4, 0, 6],
            [1, 9, 1, 8, 3, 1, 4, 2, 9, 4],
            [2, 8, 6, 4, 2, 7, 3, 2, 7, 6],
            [9, 2, 5, 0, 7, 8, 2, 9, 5, 1],
            [2, 1, 4, 4, 7, 6, 2, 4, 3, 8],
            [1, 2, 5, 3, 0, 5, 10, 8, 5, 2],
            [6, 9, 6, 8, 8, 4, 3, 6, 0, 9],
        ]
    )
)

[[4, 7, 8], 
 [9, 5, 1], 
 [2, 3, 6]]
