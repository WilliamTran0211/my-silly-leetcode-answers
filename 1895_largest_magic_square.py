from typing import List


class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        # Hint from leetcode: Hint 1 -> Check all squares in the matrix and find the largest one.
        
        n, m = len(grid), len(grid[0])

        prefix_row = [[0] * (m + 1) for _ in range(n)]
        prefix_col = [[0] * (n + 1) for _ in range(m)]
        prefix_diag = [[0] * (m + 1) for _ in range(n + 1)]
        prefix_diag_2 = [[0] * (m + 2) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                prefix_row[i][j + 1] = prefix_row[i][j] + grid[i][j]
                prefix_col[j][i + 1] = prefix_col[j][i] + grid[i][j]
                prefix_diag[i + 1][j + 1] = prefix_diag[i][j] + grid[i][j]
                prefix_diag_2[i + 1][j] = prefix_diag_2[i][j + 1] + grid[i][j]

        def check(r, c, size) -> bool:
            target = prefix_row[r][c + size] - prefix_row[r][c]

            # check rows
            for i in range(r, r + size):
                if prefix_row[i][c + size] - prefix_row[i][c] != target:
                    return False

            # check cols
            for j in range(c, c + size):
                if prefix_col[j][r + size] - prefix_col[j][r] != target:
                    return False

            # check diagonals
            if prefix_diag[r + size][c + size] - prefix_diag[r][c] != target:
                return False
            if prefix_diag_2[r + size][c] - prefix_diag_2[r][c + size] != target:
                return False

            return True

        for size in range(min(n, m), 1, -1):
            for r in range(n - size + 1):
                for c in range(m - size + 1):
                    if check(r, c, size):
                        return size

        return 1
