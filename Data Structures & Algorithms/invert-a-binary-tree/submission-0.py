# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Call sum_tree(4):

# It checks if root is None. It's not (it's 4).

# It needs to calculate: 4 + sum_tree(node_2) + sum_tree(node_5)

# It pauses and waits for sum_tree(node_2) to finish.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        else:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            return root

