# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        def traverse(node, path_str):
            if not node:
                return
            path_str += '->{}'.format(node.val)
            if node.left:
                traverse(node.left, path_str)
            if node.right:
                traverse(node.right, path_str)
            if not node.left and not node.right:
                path_arr.append(path_str)
        
        if not root:
            return []
        elif not root.left and not root.right:
            return ["{}".format(root.val)]
        path_arr = []
        root_str = str(root.val)
        traverse(root.left, root_str)
        traverse(root.right, root_str)
        return path_arr