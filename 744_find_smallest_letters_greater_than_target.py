from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        n = len(letters)

        if target >= letters[-1]:
            return letters[0]

        low, high = 0, n - 1
        ans = letters[0]
        while low <= high:
            mid = (low + high) // 2
            if letters[mid] > target:
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1

        return ans


print(Solution().nextGreatestLetter(letters=["c", "f", "j"], target="a"))

print(
    Solution().nextGreatestLetter(
        ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"], "e"
    )
)

print(Solution().nextGreatestLetter(["c", "f", "j", "k", "m", "p"], "l"))
