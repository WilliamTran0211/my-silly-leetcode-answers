from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        """
        ý tưởng: nếu tổng số lượng số âm trong matrix là số chẵn thì có thề đổi tất cả thành số dương vì mỗi lần đổi phải đổi 2 số liền kề.
        nếu là số lẻ thì lúc nào cũng còn lại 1 số âm.
        => đếm số lượng số âm và tìm số âm nhỏ nhất.
        => đồng thời tính tổng của matrix với tất các số đều dương = total_matrix_sum.

        Biết rằng chênh lệch giữa tổng dương và tổng có 1 số âm là 2x => total_matrix_sum - 2 * số âm nhỏ nhất

        2x?

        nếu tất cà các số là dương thì tổng của nó là sum1 = S(các số còn lại) + x
        vậy ta biết nếu số lượng số âm là lẻ thì dù thay đổi như nào luôn luôn còn lại 1 số âm nên lúc đó tổng sẽ là: sum2 = S(các số còn lại)+(-x) = S(các số còn lại) - x
        vậy chênh lệch giữa 2 trường hợp này là sum1-sum2= S(các số còn lại) + x -( S(các số còn lại) - x ) = S(các số còn lại) + x - S(các số còn lại) + x = 2x

        """
        n = len(matrix)
        neg_cnt = 0
        min_num_abs = float("inf")
        total = 0
        for i in range(n):
            for j in range(n):
                num = matrix[i][j]
                total += abs(num)
                if num < 0:
                    neg_cnt += 1

                min_num_abs = min(min_num_abs, abs(num))

        if neg_cnt % 2 == 0:
            return total

        return total - 2 * min_num_abs


print(
    Solution().maxMatrixSum(
        matrix=[[-3, -4, -1, -2], [-2, -2, 1, 1], [1, 6, -5, -3], [-3, -3, -9, -1]]
    )
)


print(Solution().maxMatrixSum(matrix=[[1, 2, 3], [-1, -2, -3], [1, 2, 3]]))
