from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        max_area = 0
        for r in range(n):
            for c in range(m):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            stack = []
            for i in range(m + 1):

                curr_height = 0 if i == m else heights[i]

                while stack and curr_height < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    if not stack:
                        width = i
                    else:
                        width = i - stack[-1] - 1

                    max_area = max(max_area, h * width)

                stack.append(i)

        return max_area


print(
    Solution().maximalRectangle(
        matrix=[
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
