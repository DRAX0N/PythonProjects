"""
1022. Sum of Root To Leaf Binary Numbers
Easy
Topics
premium lock icon
Companies
Hint
You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    #def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
    #    def bin_to_dec(s):
    #        return int(s, 2)
    #    
    #    def number_of_branches(root: Optional[TreeNode]):
    #        amount = 1
    #        while amount < len(root):
    #            amount *=2
    #        return amount
    #    
    #    def treenode_to_str(node):
    #        if node is None:
    #            return ""
    #        return str(node.val) + treenode_to_str(node.left) + treenode_to_str(node.right)
    #    
    #    
#
#
#
    #    branches = number_of_branches(root)
    #    print(branches)
    #    numbers = [[]]*branches
    #    jump = 1
    #    start_s = [[root[0]]]*branches
    #    elements = 1
    #    while root:
    #        for j in range(elements):
    #            for i in range(branches):
    #                numbers[i].append(root[0])
#
    #            root.pop(0)
    #        j*=2
    #        branches/=2
#
#
    #    #lenghts: 1, 3, 7, 15, 31
    #    #branch:  1, 2, 4, 8, 16
    #    for element in root:
    #        pass
    #    
    #    
#
    #    return 0

    def sumRootToLeaf(self, root, val=0):
        if not root: return 0
        val = val * 2 + root.val
        if root.left == root.right: return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)
    
if __name__ == '__main__':
    #root = [1,0,1,0,1,0,1]
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    new = Solution()
    print(new.sumRootToLeaf(root))