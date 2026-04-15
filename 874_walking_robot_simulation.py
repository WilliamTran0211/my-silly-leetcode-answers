from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Lưu trữ vật cản trong HashSet
        obstacle_set = set(map(tuple, obstacles))
        
        # Hướng: Bắc, Đông, Nam, Tây
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_idx = 0  # Bắt đầu hướng Bắc
        x, y = 0, 0
        max_dist = 0
        
        for cmd in commands:
            if cmd == -2:  # Quay trái
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:  # Quay phải
                dir_idx = (dir_idx + 1) % 4
            else:  # Di chuyển k bước
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    # Kiểm tra vật cản O(1)
                    if (next_x, next_y) in obstacle_set:
                        break  # Dừng lại trước vật cản
                    x, y = next_x, next_y
                    max_dist = max(max_dist, x*x + y*y)
        
        return max_dist