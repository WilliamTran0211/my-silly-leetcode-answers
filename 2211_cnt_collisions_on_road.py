from collections import defaultdict


class Solution:
    def countCollisions(self, directions: str) -> int:

        reform = list(directions)

        while reform[0] == "L":
            reform.pop(0)
        while reform and reform[-1] == "R":
            reform.pop(-1)

        return reform.count("L") + reform.count("R")


print(Solution().countCollisions("LLRLRSLLRRS"))
print(Solution().countCollisions("LLRR"))
print(
    Solution().countCollisions(
        "SRLRRLLRSSLRLSRRLLSRLLRLSRRLLSRRLSLRLSRLLSRRLLRLSRLRRLLSR"
    )
)
print(Solution().countCollisions("RSSLRRLLSRLLSRRLRLLSRLSRRLLSRLLRSLLRSSRLLRLSRLLRLSR"))
