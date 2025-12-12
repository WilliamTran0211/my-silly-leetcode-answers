from collections import defaultdict
from math import gcd
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        line = defaultdict(int)

        s = defaultdict(int)

        def normalize_dir(dx, dy):
            g = gcd(dx, dy)
            dx0, dy0 = dx // g, dy // g
            # canonical sign: make dx0 > 0, or if dx0 == 0 then dy0 > 0
            if dx0 < 0 or (dx0 == 0 and dy0 < 0):
                dx0, dy0 = -dx0, -dy0
            return dx0, dy0

        for i in range(len(points) - 1):
            xi, yi = points[i]

            for j in range(i + 1, len(points)):
                xj, yj = points[j]

                cal_x = xj - xi
                cal_y = yj - yi
                if cal_x == 0 and cal_y == 0:
                    continue

                dx0, dy0 = normalize_dir(cal_x, cal_y)

                line[(i, j, xi, yi, xj, yj)] = (dx0, dy0)
        res = 0

        groups = defaultdict(list)
        for l in line.items():
            dx, dy = l[1]
            groups[(dx, dy)].append(l[0])
        seen = set()
        count_parallelogram = 0
        for g in groups.items():
            if len(g[1]) >= 2:
                dx0, dy0 = g[0]
                small_group = g[1]
                length = len(small_group)
                for i in range(length - 1):

                    i1, j1, x1, y1, x2, y2 = small_group[i]

                    s1 = x1 * dy0 - y1 * dx0
                    for j in range(i + 1, length):
                        i2, j2, x3, y3, x4, y4 = small_group[j]

                        s2 = x3 * dy0 - y3 * dx0
                        pts = {
                            i1,
                            j1,
                            i2,
                            j2,
                        }  # check if all the point are different in the point list
                        key = tuple(sorted(pts))
                        if key in seen:
                            continue

                        if len(pts) == 4:

                            if s1 != s2:
                                v1 = (x3 - x1, y3 - y1)
                                v2 = (x4 - x2, y4 - y2)
                                cross = v1[0] * v2[1] - v1[1] * v2[0]
                                if cross != 0:
                                    res += 1
                                    seen.add(key)
                                else:
                                    count_parallelogram += 1
                                    seen.add(key)

        return res + count_parallelogram

    def countTrapezoids2(self, points: List[List[int]]) -> int:
        n = len(points)
        inf = 10**9 + 7
        slope_to_intercept = defaultdict(list)
        mid_to_slope = defaultdict(list)
        ans = 0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x1 - x2
                dy = y1 - y2

                if x2 == x1:
                    k = inf
                    b = x1
                else:
                    k = (y2 - y1) / (x2 - x1)
                    b = (y1 * dx - x1 * dy) / dx

                mid = (x1 + x2) * 10000 + (y1 + y2)
                slope_to_intercept[k].append(b)
                mid_to_slope[mid].append(k)

        # Counting logic would go here (see breakdown)
        return ans


print(
    Solution().countTrapezoids(
        [
            [-452, -195],
            [-19, 181],
            [-186, -369],
            [61, 363],
            [-443, 18],
            [-166, 64],
            [-226, 59],
            [-460, -172],
            [-107, 397],
            [165, 337],
            [-452, -19],
            [168, 363],
            [-2, -457],
            [-75, 233],
            [490, 14],
            [417, 213],
            [48, 65],
            [-226, 363],
            [-61, 396],
            [-397, -154],
            [-61, -196],
            [-211, -357],
            [-423, -164],
            [132, 162],
            [-157, -295],so i can say the scope of education records are already include the dismissal status/reason. so it also are the PII cause the education records are PII. althought the dismissal status/reason are  non-directory PII
            [178, 232],
            [178, -369],
            [-99, 387],
            [-61, 23],
            [98, 370],
            [48, 314],
            [-460, 271],
            [-11, 127],
            [-17, 23],
            [-440, 496],
            [417, -48],
            [-61, 181],
            [-226, 340],
            [168, -268],
            [-452, 387],
            [-226, -106],
            [-17, -213],
            [-61, 110],
            [73, -329],
            [461, 268],
            [461, 387],
            [-226, -369],
            [256, 146],
            [-332, 397],
            [-17, 473],
            [-72, -357],
            [-18, 428],
            [-249, -106],
            [191, 47],
            [73, -400],
            [-460, -134],
            [-323, 146],
            [-381, 397],
            [48, -390],
            [-290, -205],
            [-61, 368],
            [299, 412],
            [420, 55],
            [191, 147],
            [-423, 363],
            [358, 290],
            [458, 386],
            [151, 67],
            [-116, 89],
            [461, 284],
            [96, 146],
            [245, 290],
            [-175, -333],
            [-452, 14],
            [272, 54],
            [-226, 259],
            [-211, -107],
            [31, 18],
            [-162, 368],
            [-17, 454],
            [-328, 76],
            [-460, 412],
            [260, 335],
            [73, -257],
            [-452, -48],
            [-359, -357],
            [296, 47],
            [68, 3],
            [-45, 144],
            [-12, -48],
            [-366, 323],
            [448, 473],
            [-359, 356],
            [-11, -194],
            [287, 412],
            [166, 232],
            [-61, -369],
            [-6, 470],
            [247, 31],
            [296, 335],
            [-434, 108],
            [-61, -257],
            [-226, 146],
            [-175, 368],
            [-218, 397],
            [-423, 440],
            [423, 146],
            [151, 233],
            [-152, -369],
            [385, 473],
            [-187, 85],
            [-345, 368],
            [48, -421],
            [151, 89],
            [385, 27],
        ]
    )
)
