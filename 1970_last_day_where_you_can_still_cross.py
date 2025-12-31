from typing import List


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:

        def dfs(r, c, grid, visited):
            if (
                r < 0
                or c < 0
                or r >= row
                or c >= col
                or (r, c) in visited
                or grid[r][c] == 1
            ):
                return False

            if r == row - 1:
                return True

            visited.add((r, c))
            new_path = (
                dfs(r + 1, c, grid, visited)
                or dfs(r - 1, c, grid, visited)
                or dfs(r, c + 1, grid, visited)
                or dfs(r, c - 1, grid, visited)
            )
            return new_path

        def can_cross(from_day):
            grid = [[0] * col for _ in range(row)]
            for i in range(from_day):
                r, c = cells[i]  # flood
                grid[r - 1][c - 1] = 1
            visited = set()
            for c in range(col):
                if grid[0][c] == 0:
                    if dfs(0, c, grid, visited):
                        return True

            return False

        # this while loop is Binary search for middle points
        low, high = 0, row * col
        res = 0
        while low <= high:
            mid = (low + high) // 2
            if can_cross(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1

        return res
