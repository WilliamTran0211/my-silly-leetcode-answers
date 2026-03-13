from collections import deque


class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        start_zeros = s.count("0")

        # Nếu chuỗi đã toàn là '1' ngay từ đầu
        if start_zeros == 0:
            return 0

        queue = deque([start_zeros])
        visited = {start_zeros}
        steps = 0

        while queue:
            # Xử lý theo từng level (số bước)
            size = len(queue)
            for _ in range(size):
                c = queue.popleft()

                # Nếu đã đạt được mục tiêu toàn '1' (0 bit '0')
                if c == 0:
                    return steps

                # Tính khoảng giá trị x (số bit 0 được lật)
                min_x = max(0, k - (n - c))
                max_x = min(c, k)

                # Thử tất cả các lượng x có thể lật để tạo trạng thái tiếp theo
                for x in range(min_x, max_x + 1):
                    next_c = c + k - 2 * x  # Số bit '0' mới

                    if next_c not in visited:
                        visited.add(next_c)
                        queue.append(next_c)

            # Chuyển qua cấp tiếp theo
            steps += 1

        return -1
