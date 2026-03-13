from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        group_x = defaultdict(list)
        group_y = defaultdict(list)

        min_x_y = defaultdict(lambda: inf)
        max_x_y = defaultdict(lambda: -inf)

        min_y_x = defaultdict(lambda: inf)
        max_y_x = defaultdict(lambda: -inf)

        for x, y in buildings:
            group_x[x].append(y)
            group_y[y].append(x)

            min_x_y[x] = min(min_x_y[x], y)
            max_x_y[x] = max(max_x_y[x], y)

            min_y_x[y] = min(min_y_x[y], x)
            max_y_x[y] = max(max_y_x[y], x)

        res = 0
        for x, y in buildings:
            if len(group_x[x]) >= 3 and len(group_y[y]) >= 3:
                if min_x_y[x] < y < max_x_y[x] and min_y_x[y] < x < max_y_x[y]:
                    res += 1
        return res


print(
    Solution().countCoveredBuildings(
        10, [[3, 2], [5, 2], [7, 2], [3, 4], [5, 4], [7, 4], [5, 1], [5, 6]]
    )
)
