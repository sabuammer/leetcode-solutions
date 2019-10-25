# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        curr_sum = 0

        def traverse(node):
            nonlocal curr_sum
            if node.left and node.right:
                traverse(node.right)
                curr_sum += node.val
                node.val = curr_sum
                traverse(node.left)
            if node.right and not node.left:
                traverse(node.right)
                curr_sum += node.val
                node.val = curr_sum
            if node.left and not node.right:
                curr_sum += node.val
                node.val = curr_sum
                traverse(node.left)
            if not node.left and not node.right:
                curr_sum += node.val
                node.val = curr_sum
                return

        traverse(root)

        return root
