from collections import defaultdict
from typing import List


class Solution:
    def maxProfit(
        self,
        n: int,
        present: List[int],
        future: List[int],
        hierarchy: List[List[int]],
        budget: int,
    ) -> int:
        """
        cho 2 arr present và future là giá mua và giá bán cùa một cổ phiếu.

        budget là ngân sách giới hạn, tổng số tiền mua phải nhỏ hơn budget

        ! mỗi cổ phiếu chỉ mua dc 1 lần.
        ! không dc cộng lợi nhuận vào để tiếp tục mua cổ phiếu.

        hierarchy là arr chứa arr [u, v],  u là sếp của v.
        nếu u mua cổ phiếu thì v sẽ dc mua cổ phiếu với 1/2 giá

        => trả về max profit = Σ(future - giá mua thực tế)

        """
        # Tạo danh sách con cho từng node (chuyển về index 0-based)
        children = defaultdict(list)
        for u, v in hierarchy:
            children[u - 1].append(v - 1)

        # Giá trị âm vô cùng để đánh dấu trạng thái không khả thi
        INF = -(10**9)

        # Hàm DFS thực hiện quy hoạch động trên cây
        # Trả về tuple (dp0, dp1) cho node u:
        # - dp0[b]: lợi nhuận tối ưu với budget b khi node u KHÔNG được giảm giá
        # - dp1[b]: lợi nhuận tối ưu với budget b khi node u ĐƯỢC giảm giá
        def dfs(u):
            # Khởi tạo trạng thái cơ bản cho node u trước khi xét các con
            # base0: trạng thái khi u KHÔNG được mua với giá giảm
            # base1: trạng thái khi u ĐƯỢC mua với giá giảm
            base0 = [INF] * (budget + 1)
            base0[0] = 0  # Với budget = 0, lợi nhuận luôn là 0 (không mua gì)
            base1 = [INF] * (budget + 1)
            base1[0] = 0

            # Duyệt qua tất cả các node con của u
            # Đây là quá trình "gộp" kết quả từ các cây con
            for v in children[u]:
                # Gọi đệ quy để lấy kết quả DP từ node con v
                dp0_v, dp1_v = dfs(v)

                # --- GỘP VÀO BASE0 (khi u không được giảm giá) ---
                # Node con v cũng không được giảm giá vì parent (u) không được giảm giá
                new_base0 = [INF] * (budget + 1)
                # Duyệt qua tất cả các cách phân bổ budget giữa các node đã xét và node con v
                for j in range(budget + 1):
                    if base0[j] == INF:
                        continue  # Trạng thái không khả thi
                    for k in range(0, budget - j + 1):
                        # j: budget đã dùng cho các node trước đó
                        # k: budget dành cho node con v
                        if j + k <= budget and dp0_v[k] != INF:
                            # Cộng dồn lợi nhuận và cập nhật nếu tốt hơn
                            current_profit = base0[j] + dp0_v[k]
                            if new_base0[j + k] < current_profit:
                                new_base0[j + k] = current_profit
                base0 = new_base0  # Cập nhật base0 sau khi gộp node con v

                # --- GỘP VÀO BASE1 (khi u được giảm giá) ---
                # Node con v có thể được giảm giá nếu nó mua cổ phiếu (vì u được giảm giá)
                new_base1 = [INF] * (budget + 1)
                for j in range(budget + 1):
                    if base1[j] == INF:
                        continue
                    for k in range(0, budget - j + 1):
                        if j + k <= budget and dp1_v[k] != INF:
                            current_profit = base1[j] + dp1_v[k]
                            if new_base1[j + k] < current_profit:
                                new_base1[j + k] = current_profit
                base1 = new_base1  # Cập nhật base1 sau khi gộp node con v

            # --- TÍNH DP CHO NODE U SAU KHI ĐÃ GỘP TẤT CẢ CÁC CON ---

            # dp0_u: node u không được giảm giá (parent của u không mua hoặc u là root)
            dp0_u = [INF] * (budget + 1)

            # dp1_u: node u được giảm giá (parent của u đã mua cổ phiếu)
            dp1_u = [INF] * (budget + 1)

            # --- TÍNH DP0_U: TRƯỜNG HỢP U KHÔNG ĐƯỢC GIẢM GIÁ ---
            for b in range(budget + 1):
                # Tình huống 1: KHÔNG mua cổ phiếu u
                # Lợi nhuận = lợi nhuận từ các con khi u không được giảm giá
                if base0[b] != INF:
                    dp0_u[b] = base0[b]

                # Tình huống 2: MUA cổ phiếu u với GIÁ ĐẦY ĐỦ
                # Vì u không được giảm giá nếu mua sẽ mua với giá present[u]
                cost0 = present[u]
                if b >= cost0 and base1[b - cost0] != INF:
                    # Công thức: profit = profit_các_con + (future[u] - cost0)
                    # Dùng base1 vì nếu u mua, thì các con của u sẽ được giảm giá
                    profit = base1[b - cost0] + (future[u] - cost0)
                    if profit > dp0_u[b]:
                        dp0_u[b] = profit

            # --- TÍNH DP1_U: TRƯỜNG HỢP U ĐƯỢC GIẢM GIÁ ---
            for b in range(budget + 1):
                # Tình huống 1: KHÔNG mua cổ phiếu u
                # Dù được giảm giá nhưng vẫn có thể không mua
                if base0[b] != INF:
                    dp1_u[b] = base0[b]

                # Tình huống 2: MUA cổ phiếu u với GIÁ GIẢM 50%
                # Vì u được giảm giá (parent của u đã mua) nên giá chỉ còn một nửa
                cost1 = present[u] // 2  # Chia nguyên để lấy phần nguyên
                if b >= cost1 and base1[b - cost1] != INF:
                    # Công thức: profit = profit_các_con + (future[u] - cost1)
                    profit = base1[b - cost1] + (future[u] - cost1)
                    if profit > dp1_u[b]:
                        dp1_u[b] = profit

            # Trả về 2 mảng DP cho node u
            return dp0_u, dp1_u

        # --- BẮT ĐẦU GIẢI THUẬT TỪ ROOT (NODE 0) ---
        # Gọi DFS từ node gốc (giả sử là node 0)
        # Chỉ cần dp0_root vì root không có parent nên không được giảm giá
        dp0_root, _ = dfs(0)

        # Kết quả là giá trị lớn nhất trong dp0_root
        # (vì có thể không sử dụng hết budget vẫn đạt lợi nhuận tối ưu)
        return max(dp0_root)
