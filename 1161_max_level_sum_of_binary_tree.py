from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"  # Py 3.6


def grow_a_tree_from_list(root_lst: List[int]) -> Optional[TreeNode]:
    # this is better because it dont create node with None value
    root_node = TreeNode(val=root_lst[0])
    nodes = [root_node]
    for i, val in enumerate(root_lst[1:]):
        if val is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2) == 0
        node = TreeNode(val=val)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = defaultdict(int)
        level = 0

        def dfs(current, level):
            if not current:
                return 0

            level_sum[level] += current.val
            level += 1
            dfs(current.left, level)
            dfs(current.right, level)

        dfs(root, level)

        return max(level_sum, key=level_sum.get) + 1


print(
    Solution().maxLevelSum(
        grow_a_tree_from_list(
            [989, None, 10250, 98693, -89388, None, None, None, -32127]
        )
    )
)
