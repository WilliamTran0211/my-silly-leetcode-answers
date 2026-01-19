from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Prefix sum
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ps[i][j] = (
                    mat[i - 1][j - 1]
                    + ps[i - 1][j]
                    + ps[i][j - 1]
                    - ps[i - 1][j - 1]
                )

        def check(k):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    total = (
                        ps[i][j]
                        - ps[i - k][j]
                        - ps[i][j - k]
                        + ps[i - k][j - k]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


print(
    Solution().maxSideLength(
        mat=[[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]],
        threshold=4,
    )
)
