class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        """
            với mỗi thời điểm nếu đóng cửa chỉ cần quan tâm có bao nhiêu:
                N trước nó, vì N đến lúc mở cửa thì pen +1
                Y sau nó, vì Y đến lúc đóng cửa thì pen +1
        """

        prefix_N = [0] * (n + 1)
        prefix_Y = [0] * (n + 1)

        for i in range(n):
            current_n = 1 if customers[i] == "N" else 0
            current_y = 1 if customers[i] == "Y" else 0
            prefix_N[i + 1] = prefix_N[i] + current_n
            prefix_Y[i + 1] = prefix_Y[i] + current_y

        totalY = prefix_Y[n]

        cur_pen = []
        for i in range(n + 1):
            cur_pen.append(totalY - prefix_Y[i] + prefix_N[i])
        return cur_pen.index(min(cur_pen))


print(Solution().bestClosingTime("NYYYNNNYNN"))
