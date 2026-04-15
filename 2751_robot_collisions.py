from collections import defaultdict
from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:

        n = len(positions)
        # Tạo list các robot với index, position, health, direction
        robots = []
        for i in range(n):
            robots.append([i, positions[i], healths[i], directions[i]])  # [index, pos, health, dir]
        
        # Sắp xếp theo vị trí
        robots.sort(key=lambda x: x[1])
        
        stack = []  # mỗi phần tử: [index, health, direction]
        
        for robot in robots:
            idx, pos, health, direct = robot
            
            if direct == 'R':
                stack.append([idx, health, direct])
            else:  # direct == 'L'
                # Xử lý va chạm với các robot đi R trong stack
                while stack and stack[-1][2] == 'R' and health > 0:
                    if stack[-1][1] > health:
                        # Robot trong stack thắng
                        stack[-1][1] -= 1
                        health = 0
                    elif stack[-1][1] < health:
                        # Robot hiện tại thắng
                        health -= 1
                        stack.pop()
                    else:
                        # Hòa, cả hai chết
                        stack.pop()
                        health = 0
            
                # Nếu robot vẫn còn sống, thêm vào stack
                if health > 0:
                    stack.append([idx, health, direct])
        
        # Sắp xếp kết quả theo index ban đầu
        result = [0] * n
        for robot in stack:
            result[robot[0]] = robot[1]
        
        # Lọc các robot còn sống (health > 0)
        return [h for h in result if h > 0]


print(
    Solution().survivedRobotsHealths(
        positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"
    )
)
