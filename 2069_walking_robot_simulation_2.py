from typing import List


class Robot:

    direct = {"North": (0, 1), "East": (1, 0), "South": (0, -1), "West": (-1, 0)}

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.pos = [0, 0]
        self.dir = "East"

        self.perimeter = 2 * (width + height) - 4

    def turn(self) -> None:
        rotation = {"East": "North", "North": "West", "West": "South", "South": "East"}
        self.dir = rotation[self.dir]

    def step(self, num: int) -> None:

        if self.perimeter == 0:
            return

        num %= self.perimeter

        if num == 0:
            num = self.perimeter

        for _ in range(num):
            x, y = self.pos
            dx, dy = self.direct[self.dir]
            next_x, next_y = x + dx, y + dy

            if 0 <= next_x < self.width and 0 <= next_y < self.height:
                self.pos = [next_x, next_y]
            else:
                self.turn()
                dx, dy = self.direct[self.dir]
                self.pos = [x + dx, y + dy]

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.dir
