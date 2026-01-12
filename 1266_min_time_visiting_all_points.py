from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        time = 0

        for i in range(1, len(points)):
            first = points[i - 1]
            x, y = first[0], first[1]
            curr_x, curr_y = points[i][0], points[i][1]
            dx = abs(curr_x - x)
            dy = abs(curr_y - y)
            time += max(dx, dy)

        return time


"""
What if....
what if we don't need to visit points in order? 
What if we can choose whatever point to visit? 

How should we find the minimum time to visit every point?

Điều này sẽ làm bài toán trở nên siêu khó 
"""
