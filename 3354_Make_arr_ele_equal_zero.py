from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        counting = 0
        for idx, num in enumerate(nums):
            if num == 0:
                # go right curr + 1
                curr = idx
                direction = 1
                nums_cp = nums.copy()
                while curr >= 0 and curr <= n - 1:
                    if nums_cp[curr] == 0:
                        curr += direction
                        continue
                    else:
                        nums_cp[curr] -= 1
                        curr += direction * (-1)
                        direction *= -1

                if all(x == 0 for x in nums_cp):
                    counting += 1

                # go left curr - 1
                curr = idx
                direction = -1
                nums_cp = nums.copy()
                while curr >= 0 and curr <= n - 1:
                    if nums_cp[curr] == 0:
                        curr += direction
                        continue
                    else:
                        nums_cp[curr] -= 1
                        curr += direction * (-1)
                        direction *= -1
                if all(x == 0 for x in nums_cp):
                    counting += 1

        return counting


print(
    Solution().countValidSelections(
        [
            46,
            53,
            45,
            49,
            53,
            45,
            47,
            44,
            46,
            37,
            50,
            39,
            53,
            52,
            48,
            42,
            40,
            48,
            43,
            41,
            51,
            45,
            41,
            43,
            49,
            44,
            45,
            45,
            43,
            51,
            51,
            46,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            35,
            39,
            40,
            41,
            34,
            40,
            40,
            32,
            27,
            27,
            41,
            40,
            39,
            42,
            32,
            52,
            32,
            29,
            35,
            40,
            32,
            37,
            28,
            34,
            42,
            33,
            38,
            40,
            40,
            40,
            38,
            38,
            30,
            38,
            38,
            43,
            36,
            36,
            38,
            40,
        ]
    )
)
