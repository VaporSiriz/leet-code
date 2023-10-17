# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def search(self, node: Optional[TreeNode], max_diameter: int):
        if not node:
            return 0, max_diameter
        if not node.left and not node.right:
            return 1, max_diameter
        #print(f"{node.val}")
        
        left, max_diameter = self.search(node.left, max_diameter)
        right, max_diameter = self.search(node.right, max_diameter)
        #print(f"{node.val} left:{left}, right:{right}")
        if max_diameter < left + right:
            max_diameter = left + right
        #print(f"{node.val} left:{left}, right:{right}, max_diameter:{max_diameter}")
        
        return left+1 if left > right else right+1, max_diameter
        
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        _, max_diameter = self.search(node=root, max_diameter=0)
        return max_diameter