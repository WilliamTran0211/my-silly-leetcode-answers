from typing import List


class SegmentTree:
    def __init__(self, xs: List[int]):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.length = [0] * (4 * self.n)

    def update(self, node: int, l: int, r: int, ul: int, ur: int, val: int):
        if ur <= l or r <= ul:
            return

        if ul <= l and r <= ur:
            self.count[node] += val
        else:
            mid = (l + r) // 2
            self.update(2 * node + 1, l, mid, ul, ur, val)
            self.update(2 * node + 2, mid, r, ul, ur, val)

        if self.count[node] > 0:
            self.length[node] = self.xs[r] - self.xs[l]
        else:
            if l + 1 == r:
                self.length[node] = 0
            else:
                self.length[node] = (
                    self.length[2 * node + 1] + self.length[2 * node + 2]
                )

    def query(self) -> int:
        return self.length[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = []


        for x, y, l in squares:
            events.append((y, +1, x, x + l))  # add interval
            events.append((y + l, -1, x, x + l))  # remove interval
            xs.append(x)
            xs.append(x + l)


        events.sort()
        xs = sorted(set(xs))
        x_id = {x: i for i, x in enumerate(xs)}

        # 4. Segment tree
        st = SegmentTree(xs)

        prev_y = events[0][0]
        total_area = 0.0
        slices = []  # (y1, y2, width)

        # 5. Sweep line
        for y, typ, x1, x2 in events:
            height = y - prev_y
            if height > 0:
                width = st.query()
                area = width * height
                total_area += area
                slices.append((prev_y, y, width))

            l = x_id[x1]
            r = x_id[x2]
            st.update(0, 0, st.n, l, r, typ)

            prev_y = y

        # 6. Find y where area is split equally
        target = total_area / 2.0
        acc = 0.0

        for y1, y2, width in slices:
            slice_area = width * (y2 - y1)
            if acc + slice_area < target:
                acc += slice_area
            else:
                needed = target - acc
                if width == 0:
                    return y1  # edge case
                dy = needed / width
                return y1 + dy

        return 0.0