# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def search(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            if not node.left and not node.right:
                return 1

            left = search(node.left)
            right = search(node.right)
            nonlocal max_diameter
            if max_diameter < left + right:
                max_diameter = left + right

            return 1 + max(left, right)

        search(node=root)
        return max_diameter