from typing import List


class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        matrix = [[0] * (n + 1) for _ in range(n + 1)]

        for query in queries:
            r1, c1 = query[0], query[1]
            r2, c2 = query[2], query[3]
            matrix[r1][c1] += 1
            matrix[r1][c2 + 1] -= 1
            matrix[r2 + 1][c1] -= 1
            matrix[r2 + 1][c2 + 1] += 1

        # for r in range(n):
        #     for c in range(n):
        #         if r > 0:
        #             matrix[r][c] += matrix[r - 1][c]
        #         if c > 0:
        #             matrix[r][c] += matrix[r][c - 1]
        #         if r > 0 and c > 0:
        #             matrix[r][c] -= matrix[r - 1][c - 1]

        # return [row[:n] for row in matrix[:n]]
        res = [[0] * (n) for _ in range(n)]

        for r in range(n):
            for c in range(n):
                top = 0 if r == 0 else res[r - 1][c]
                left = 0 if c == 0 else res[r][c - 1]
                top_left = 0 if c == 0 or r == 0 else res[r - 1][c - 1]
                res[r][c] = matrix[r][c] + top + left - top_left

        return res


print(Solution().rangeAddQueries(3, [[1, 1, 2, 2], [0, 0, 1, 1]]))
