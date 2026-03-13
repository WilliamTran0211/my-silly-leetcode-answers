from typing import Optional

from leetcode_utils import TreeNode


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        arr = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node)
            inorder(node.right)

        inorder(root)

        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = arr[mid]

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root

        return build(0, len(arr) - 1)
