from collections import defaultdict
from typing import Optional, List


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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        tìm sub tree chứa tất cả các node sâu nhất
        """
        if not root.left and not root.right:
            return root

        self.res = None
        self.res_level = -1

        def dfs(current):
            if not current:
                return None, 0
            left_tree, left_lvl = dfs(current.left)
            right_tree, right_lvl = dfs(current.right)

            if left_lvl > right_lvl:
                return left_tree, left_lvl + 1
            if right_lvl > left_lvl:
                return right_tree, right_lvl + 1

            return current, left_lvl + 1

        return dfs(root)[0]


print(
    "ans",
    Solution().subtreeWithAllDeepest(
        grow_a_tree_from_list([3, 5, 1, 6, 2, 0, 8, 9, 10, 7, 4])
    ),
)  # [5,6,2,9,10,7,4]


print(
    "ans",
    Solution().subtreeWithAllDeepest(
        grow_a_tree_from_list(
            [3, 5, 1, 6, 2, 0, 8, 9, 10, 7, 4, None, None, None, None, None, None, 11]
        )
    ),
)
