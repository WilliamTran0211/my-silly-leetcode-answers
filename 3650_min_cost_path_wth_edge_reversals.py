from collections import defaultdict
from math import inf
from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, w in edges:
            g[x].append((y, w))
            g[y].append((x, 2 * w))

        dist = [inf] * n
        visited = [False] * n
        dist[0] = 0
        heap = [(0, 0)]  # (Distance, Node)

        while heap:
            cur_dist, x = heapq.heappop(heap)

            if x == n - 1:
                return cur_dist

            # already processed
            if visited[x]:
                continue
            visited[x] = True

            # relaxing neighbors
            for y, w in g[x]:
                new_dist = cur_dist + w
                if new_dist < dist[y]:
                    dist[y] = new_dist
                    heapq.heappush(heap, (new_dist, y))

        return -1


print(
    Solution().minCost(
        10,
        [
            [3, 4, 11],
            [6, 0, 17],
            [1, 4, 2],
            [5, 3, 18],
            [5, 2, 18],
            [1, 8, 11],
            [3, 9, 13],
            [3, 8, 13],
            [7, 0, 5],
            [7, 9, 12],
            [6, 1, 18],
            [9, 7, 5],
            [0, 5, 3],
            [4, 1, 5],
            [1, 2, 1],
            [2, 8, 4],
            [6, 9, 11],
            [9, 6, 2],
            [9, 1, 24],
            [0, 8, 17],
            [3, 5, 13],
            [2, 9, 3],
            [9, 4, 1],
            [2, 3, 15],
            [6, 7, 8],
            [9, 5, 10],
            [7, 3, 2],
            [8, 5, 3],
            [3, 2, 4],
            [7, 6, 7],
            [5, 8, 3],
            [9, 3, 3],
            [6, 3, 10],
            [8, 3, 5],
            [7, 8, 13],
            [0, 1, 2],
        ],
    )
)
