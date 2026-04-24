# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # lst = []
        count = 0
        def helper(node):
            # nonlocal lst
            nonlocal count
            if node.left:
                # helper(node.left)
                tmp = helper(node.left)
                if tmp != None:
                    return tmp
            # lst.append(node.val)
            # if k <= len(lst):
            #     return lst[k-1]
            count += 1
            if k == count:
                return node.val
            if node.right:
                # helper(node.right)
                return helper(node.right)
        # helper(root)
        # return lst[k-1]
        return helper(root)