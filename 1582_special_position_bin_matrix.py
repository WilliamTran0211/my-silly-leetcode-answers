from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        row_cnt = [0] * n
        col_cnt = [0] * m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    row_cnt[i] += 1
                    col_cnt[j] += 1
        res = 0

        for i in range(n):
            for j in range(m):

                if mat[i][j] == 1 and row_cnt[i] == 1 and col_cnt[j] == 1:
                    res += 1

        return res
