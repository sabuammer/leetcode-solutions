# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def bfs(node):
            stack = []
            stack.append(node)
            bfs_str = ''
            while stack:
                curr_node = stack.pop()
                if curr_node:
                    bfs_str += str(curr_node.val)
                    stack.append(curr_node.left)
                    stack.append(curr_node.right)
                else:
                    bfs_str += '~'
            
            return bfs_str
        
        return bfs(p) == bfs(q)