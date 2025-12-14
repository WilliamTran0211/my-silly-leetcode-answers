class Solution:
    def numberOfWays(self, corridor: str) -> int:
        check_validate = corridor.count("S")
        if check_validate % 2 != 0 or check_validate < 2:
            return 0

        MOD = 10**9 + 7

        count_p = []
        count_s = 0
        curr_p = 0
        for c in corridor:
            if c == "S":
                if count_s < 2:
                    count_s += 1
                else:
                    count_p.append(curr_p)
                    curr_p = 0
                    count_s = 1
            if c == "P":
                if count_s == 2:
                    curr_p += 1
        res = 1
        for cnt in count_p:
            res *= cnt + 1
        return res % MOD


print(Solution().numberOfWays("SSPSSPSSSPPSPSPPS"))
