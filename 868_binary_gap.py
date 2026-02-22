class Solution:
    def binaryGap(self, n: int) -> int:
        bin_str = bin(n)[2:]

        if bin_str.count("1") == 1:
            return 0

        print(bin_str)

        res = 0

        prev_1_idx = -1
        for i in range(len(bin_str)):
            if bin_str[i] == "1":
                if prev_1_idx == -1:
                    prev_1_idx = i
                else:
                    res = max(res, abs(prev_1_idx - i))
                    prev_1_idx = i
        return res


print(Solution().binaryGap(1041))
