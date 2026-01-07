from collections import defaultdict
from turtle import circle
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
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7

        def dfs(current, current_sum):
            if not current:
                return 0
            return (
                current.val
                + dfs(current.left, current_sum)
                + dfs(current.right, current_sum)
            )

        total_sum = dfs(root, 0)
        self.max_res = 0

        def find(current):
            if not current:
                return 0
            left_tree = find(current.left)
            right_tree = find(current.right)
            subtree = current.val + left_tree + right_tree
            self.max_res = max(self.max_res, subtree * (total_sum - subtree))

            return subtree

        find(root)

        return self.max_res % MOD


print(Solution().maxProduct(grow_a_tree_from_list([1, 2, 3, 4, 5, 6])))
