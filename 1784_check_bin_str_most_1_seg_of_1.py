class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)

        for i in range(1, n):
            if s[i] == "1" and s[i - 1] == "1":
                continue
            else:
                if s[i:].count("1") != 0:
                    return False
                else:
                    return True
        return True


# ko có 0 ở đầu thì chỉ có 1 ở đầu, nếu 1 ở đầu thì chỉ cần xem trong đoạn còn lại liệu còn 1 số 1 nào đứng riêng lẻ

print(Solution().checkOnesSegment("100001111"))
