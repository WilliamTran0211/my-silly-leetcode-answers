from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        res = 0
        while left < right:
            res = max(res, abs(right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
