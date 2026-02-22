class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        check_bin = str(bin(n))

        for i in range(1, len(check_bin)):
            if check_bin[i - 1] == check_bin[i]:
                return False
        return True
