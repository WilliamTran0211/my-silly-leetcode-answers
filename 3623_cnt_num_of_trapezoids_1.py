from collections import defaultdict
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        be_line = defaultdict(int)
        mod = 10**9 + 7

        res = 0
        for x, y in points:
            be_line[y] += 1

        be_line = dict(sorted(be_line.items(), key=lambda item: item[0]))
        line_form = list(be_line.values())
        total_line_before = 0
        for line in line_form:
            total_line = (line * (line - 1)) // 2
            if total_line_before != 0:
                res += total_line_before * total_line
            total_line_before += total_line

        return res % mod


print(
    Solution().countTrapezoids(
        [[-90, -84], [818, -3], [74, -3], [-7, -3], [54, -8], [4, -8]]
    )
)
