from collections import defaultdict
from typing import List


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        zeros = defaultdict(int)
        for i in range(0, n):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 0:
                    zeros[i] += 1
                else:
                    break

        steps = 0

        for i in range(n):
            need_0 = n - i - 1

            j = i

            while j < n and zeros[j] < need_0:
                j += 1

            if j == n:
                return -1

            while j > i:
                temp = zeros[j - 1]
                zeros[j - 1] = zeros[j]
                zeros[j] = temp
                steps += 1
                j -= 1

        return steps


print(Solution().minSwaps(grid=[[0, 0, 1], [1, 1, 0], [1, 0, 0]]))
