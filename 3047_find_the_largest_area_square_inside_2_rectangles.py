from typing import List


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:

        intersect_rc = []

        n = len(bottomLeft)

        for i in range(n):
            x1, y1, x2, y2 = (
                bottomLeft[i][0],
                bottomLeft[i][1],
                topRight[i][0],
                topRight[i][1],
            )

            for j in range(i + 1, n):
                x3, y3, x4, y4 = (
                    bottomLeft[j][0],
                    bottomLeft[j][1],
                    topRight[j][0],
                    topRight[j][1],
                )

                left = max(x1, x3)
                bottom = max(y1, y3)
                right = min(x2, x4)
                top = min(y2, y4)

                if left < right and bottom < top:
                    intersect_rc.append([left, bottom, right, top])

        max_side = 0
        for rc in intersect_rc:
            left, bottom, right, top = rc[0], rc[1], rc[2], rc[3]
            side = min(right - left, top - bottom)
            max_side = max(max_side, side)
        return max_side * max_side
