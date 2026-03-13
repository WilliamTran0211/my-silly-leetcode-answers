from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:

        temp_nums = []

        while len(nums) > 1:
            for i in range(len(nums) - 1):
                cal = (nums[i] + nums[i + 1]) % 10
                temp_nums.append(cal)
            nums = temp_nums.copy()
            temp_nums.clear()

        return nums[0]


nums = [1, 2, 3, 4, 5]
print(Solution().triangularSum(nums))
