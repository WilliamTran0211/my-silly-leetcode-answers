from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        re_map = defaultdict(list)

        for tra in allowed:
            bot = tra[0:2]
            re_map[bot].append(tra[-1])

        wrong = set()

        def dfs(curr_row: str) -> bool:
            if len(curr_row) == 1:
                return True

            if curr_row in wrong:
                return False

            # build next pyramid level
            next_lvl = [""]
            for i in range(len(curr_row) - 1):
                bottom_set = curr_row[i : i + 2]

                if bottom_set not in re_map:
                    wrong.add(curr_row)
                    return False

                level = []
                # check next level
                for bt in next_lvl:
                    top = re_map[bottom_set]
                    for t in top:
                        level.append(bt + t)
                next_lvl = level

            # dfs next level
            for lvl in next_lvl:
                if dfs(lvl):
                    return True

            wrong.add(curr_row)
            return False

        return dfs(bottom)


print(
    Solution().pyramidTransition(
        bottom="BCD", allowed=["BCC", "BCA", "CDE", "CEA", "FFF"]
    )
)


# print(
#     Solution().pyramidTransition(
#         bottom="ABCD", allowed=["ABE", "ABF", "BCG", "CDH", "EGI", "FGI", "GIJ"]
#     )
# )
