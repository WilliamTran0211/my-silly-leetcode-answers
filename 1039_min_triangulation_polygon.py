from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        def dp(i, j):
            if j < i + 2:
                return 0

            res = float("inf")
            for k in range(i + 1, j):
                res = min(res, values[i] * values[k] * values[j] + dp(i, k) + dp(k, j))

            return res

        return dp(0, len(values) - 1)


print(Solution().minScoreTriangulation([3, 7, 4, 5]))
