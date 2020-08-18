def __init__(self):
    self.ans = []

# recursion
def preorderTraversal(self, root: TreeNode) -> List[int]:
    if root:
        self.ans.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

    return self.ans

# iterative
def preorderTraversal(self, root: TreeNode) -> List[int]:
    output = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            output.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return output


def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        output = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            output.append(root.val)
            root = root.right

        return output


def postorderTraversal(self, root: TreeNode) -> List[int]:

    stack = []
    ans = []
    while root or stack:
        while root:
            if root.right:
                stack.append(root.right)
            stack.append(root)
            root = root.left

        node = stack.pop()
        if stack and stack[-1] is node.right:
            root = stack.pop()
            stack.append(node)
        else:
            ans.append(node.val)

    return ans