# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        prev = {}
        found_p = False
        found_q = False
        num_node = {}
        
        def trace(node):
            nonlocal found_p, found_q, prev, p, q
            num_node[node.val] = node
            if node.val == p.val:
                found_p = True
                print(p, 'p', node)
            elif node.val == q.val:
                print(q, 'q', node)
                found_q = True
            if not (found_p and found_q):
                if node.left:
                    prev[node.left.val] = node.val
                    trace(node.left)
                if node.right:
                    prev[node.right.val] = node.val
                    trace(node.right)
        
        def parent(lst, num):
            nonlocal prev, num_node
            lst.append(num_node[num])
            if num not in prev:
                return
            else:
                parent(lst, prev[num])
        
        trace(root)
        print(prev)
        p_par = []
        q_par = []
        parent(p_par, p.val)
        print()
        parent(q_par, q.val)
        print(p_par, q_par)

        pp = p_par.pop()
        qq = q_par.pop()
        while True:
            if len(p_par) == 0 or len(q_par) == 0:
                return root
            if len(p_par) > len(q_par):
                pp = p_par.pop(0)
            elif len(p_par) == len(q_par):
                pp = p_par.pop(0)
                qq = q_par.pop(0)
            else:
                qq = q_par.pop(0)
            if pp == qq:
                return pp
                



            