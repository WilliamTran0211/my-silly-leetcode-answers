from typing import List
from math import sqrt


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                for k in range(j + 1, len(points)):
                    x1, x2 = points[i]
                    y1, y2 = points[j]
                    z1, z2 = points[k]
                    area = 1 / 2 * abs(x1 * (y2 - z2) + y1 * (z2 - x2) + z1 * (x2 - y2))
                    print(area)
                    res = max(res, area)

        return res


print(Solution().largestTriangleArea([[4, 6], [6, 5], [3, 1]]))
