from collections import defaultdict
from tabnanny import check
from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        n_sum = 0

        smallest_one = float("inf")
        smallest_two = float("inf")

        for n in nums:
            n_sum += n
            if n % 3 == 1:
                smallest_two = min(smallest_two, smallest_one + n)
                smallest_one = min(smallest_one, n)

            if n % 3 == 2:
                smallest_one = min(smallest_one, n + smallest_two)
                smallest_two = min(smallest_two, n)

        if n_sum % 3 == 0:
            return n_sum

        if n_sum % 3 == 1:
            return n_sum - smallest_one

        if n_sum % 3 == 2:
            return n_sum - smallest_two


print(Solution().maxSumDivThree([3, 6, 5, 1, 8]))
