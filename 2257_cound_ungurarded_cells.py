from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        # total = n * m

        # grid = [[1 for i in range(n)] for i in range(m)]

        # for w1, w2 in walls:
        #     grid[w1][w2] = 0

        # for g1, g2 in guards:
        #     grid[g1][g2] = -2
        #     up, down, left, right = g1 - 1, g1 + 1, g2 - 1, g2 + 1

        #     if down >= 0:
        #         for i in range(g1, m):
        #             if grid[i][g2] != 0:
        #                 grid[i][g2] = -1
        #             else:
        #                 break
        #     if up >= 0:
        #         for i in range(g1, -1, -1):
        #             if grid[i][g2] != 0:
        #                 grid[i][g2] = -1
        #             else:
        #                 break
        #     if right >= 0:
        #         for i in range(g2, n):
        #             if grid[g1][i] != 0:
        #                 grid[g1][i] = -1
        #             else:
        #                 break
        #     if left >= 0:
        #         for i in range(g2, -1, -1):
        #             if grid[g1][i] != 0:
        #                 grid[g1][i] = -1
        #             else:
        #                 break

        # for r in range(m):
        #     for c in range(n):
        #         if grid[r][c] != 1:
        #             total -= 1

        # return total

        grid = [[0] * n for _ in range(m)]

        for r, c in guards:
            grid[r][c] = 1
        for r, c in walls:
            grid[r][c] = 2

        def mark_guard(r, c):
            for row in range(r + 1, m):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3

            for row in reversed(range(0, r)):
                if grid[row][c] in [1, 2]:
                    break
                grid[row][c] = 3

            for col in range(c + 1, n):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

            for col in reversed(range(0, c)):
                if grid[r][col] in [1, 2]:
                    break
                grid[r][col] = 3

        for r, c in guards:
            mark_guard(r, c)

        total = 0
        for row in grid:
            for n in row:
                if n == 0:
                    total += 1

        return total


print(
    Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]])
)
