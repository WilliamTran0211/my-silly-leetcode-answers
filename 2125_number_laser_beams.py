from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0

        previous_beam = 0
        for row in bank:
            check_row = list(map(lambda x: int(x), list(row)))
            current_beams = sum(check_row)
            if current_beams == 0:
                continue
            else:
                if previous_beam != 0:
                    res += previous_beam * current_beams
                previous_beam = current_beams

        return res


print(Solution().numberOfBeams(["011001", "000000", "010100", "001000"]))
