# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def traverse(node, level):
            if node.left and not node.right:
                level += 1
                traverse(node.left, level)
                level -= 1
            elif node.right and not node.left:
                level += 1
                traverse(node.right, level)
                level -= 1
            elif node.left and node.right:
                level += 1
                traverse(node.left, level)
                traverse(node.right, level)
                level -= 1
            if level not in order_dict:
                order_dict[level] = [node.val]
            else:
                order_dict[level].append(node.val)
                
        if not root:
            return []
        
        order_dict = {}
        ret_val = []
        level = 1
        
        traverse(root, level)
        for i in range(len(order_dict), 0, -1):
            ret_val.append(order_dict[i])
        return ret_val
        
        
        