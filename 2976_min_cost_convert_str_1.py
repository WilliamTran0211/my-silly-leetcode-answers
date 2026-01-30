from math import inf
from typing import List
import heapq


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        # Floyd–Warshal

        def convert_char_alpha(char):
            return ord(char) - 97

        dist = [[0 if i == j else inf for j in range(26)] for i in range(26)]

        for i in range(len(original)):
            origin = convert_char_alpha(original[i])
            change = convert_char_alpha(changed[i])

            dist[origin][change] = min(dist[origin][change], cost[i])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        total_cost = 0

        for i in range(len(source)):
            x = convert_char_alpha(source[i])
            y = convert_char_alpha(target[i])

            if x == y:
                continue

            if dist[x][y] == inf:
                return -1

            total_cost += dist[x][y]

        return total_cost


print(
    Solution().minimumCost(
        source="abcd",
        target="acbe",
        original=["a", "b", "c", "c", "e", "d"],
        changed=["b", "c", "b", "e", "b", "e"],
        cost=[2, 5, 5, 1, 2, 20],
    )
)  # 28
