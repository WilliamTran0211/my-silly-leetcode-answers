from re import I
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # i = 0

        # while i <= len(bits):
        #     if bits[i] == 0:
        #         if i == len(bits) - 1:
        #             break
        #         i += 1
        #     if bits[i] == 1:
        #         i += 2
        #         if i >= len(bits):
        #             return False

        # return True


print(Solution().isOneBitCharacter([1, 0, 0]))
print(Solution().isOneBitCharacter([1, 1, 1, 0]))
print(Solution().isOneBitCharacter([1, 1, 0]))
print(Solution().isOneBitCharacter([1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0]))
