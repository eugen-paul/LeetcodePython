from typing import List, Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ----


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.last_val = None
        self.min_diff = 10_000_000

        def get_dif(node: Optional[TreeNode]):
            if node is None:
                return

            get_dif(node.left)

            if self.last_val:
                self.min_diff = min(self.min_diff, abs(node.val - self.last_val.val))

            self.last_val = node

            get_dif(node.right)

        get_dif(root)
        return self.min_diff


def deserialize(string):
    if string == '[]':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None and q is None:
        return True
    if p is None or q is None or p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    resp = list()

    def travel(node: Optional[TreeNode], level: int):
        if not node:
            return

        if len(resp) <= level:
            resp.append(list())

        travel(node.left, level + 1)
        resp[level].append(node.val)
        travel(node.right, level + 1)

    travel(root, 0)

    return resp


def do_test(i: int, s, r):
    c = Solution()
    resp = c.minDiffInBST(deserialize(s))
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "[4,2,6,1,3]", 1)
    do_test(1, "[1,0,48,null,null,12,49]", 1)
    do_test(2, "[10,5,48,null,null,12,61]", 2)
    do_test(3, "[27,null,34,null,58,50,null,44]", 6)
    do_test(4, "[5,12]", 7)
