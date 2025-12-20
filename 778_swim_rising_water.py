from typing import List
from heapq import heappush, heappop


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        Tìm đường đi từ (0,0) đến (n-1,n-1) sao cho giá trị lớn nhất (độ cao lớn nhất) trên đường đi đó là nhỏ nhất có thể.

        Để đi từ một ô sang ô kế bên, chỉ có thể di chuyển khi mực nước t đã cao hơn hoặc bằng độ cao của ô muốn đi tới (tức là height ≤ t).

        Ví dụ, nếu đường đi là 0 → 2 → 1, thì khi đi từ 0 sang 2, phải chờ đến lúc t = 2 (vì ô đó cao 2).
            → Vậy giá trị lớn nhất trên đường đi này là 2.
            → Nghĩa là cần ít nhất t = 2 để bơi qua được toàn bộ đường đó.
        """

        n = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r,c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))

        while minH:
            t, r, c = heappop(minH)

            visit.add((r, c))

            if r == n - 1 and c == n - 1:
                return t

            for dr, dc in directions:

                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == n
                    or neiC == n
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))

                heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])


print(
    Solution().swimInWater(
        [
            [0, 1, 2, 3, 4],
            [24, 23, 22, 21, 5],
            [12, 13, 14, 15, 16],
            [11, 17, 18, 19, 20],
            [10, 9, 8, 7, 6],
        ]
    )
)
