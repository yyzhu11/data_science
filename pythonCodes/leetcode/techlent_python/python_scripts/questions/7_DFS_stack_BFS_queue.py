########################################################################################################
#Tree definition
# treeNode, constructBT, preorder,

class treeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructBT(nlist, index):
    if not nlist:
        return None
    if index >= len(nlist) or nlist[index] is None:
        return None
    root = treeNode(nlist[index])
    if 2*index + 1 < len(nlist):
        root.left = constructBT(nlist, 2*index + 1)
    if 2*index + 2 < len(nlist):
        root.right = constructBT(nlist, 2 * index + 2)
    return root

#preorder
def recursive_DFS(root):
    if not root:
        return []
    result = []
    result.append(root.val)
    result += recursive_DFS(root.left)
    result += recursive_DFS(root.right)
    return result

# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(recursive_DFS(root))

########################################################################################################################
#DFS with Stack - Preorder

def DFS_stack(root):
    if not root:
        return []
    stack = []
    result = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(DFS_stack(root))
########################################################################################################################
#DFS with Stack: Inorder
def DFS_inorder(root):
    if not root:
        return []
    stack = []
    result = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            result.append(node.val)
            root = node.right
    return result

# root = constructBT([1,2,3,4,5,None, None,6],0)
#
# print(DFS_inorder(root))

########################################################################################################################
#BFS with Queue
from collections import deque
def BFS_queue(root):
    if not root:
        return []
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(BFS_queue(root))

########################################################################################################################
#Leetcode 102 - Binary Tree Level Order Traversal
"""
Description:
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level)

Example:
Given binary tree [3,9,20,null,null,15,7],

     3
    / \
   9  20
     /  \
    15   7
 
return its level order traversal as:

[
    [3],
    [9,20],
    [15,7]
  ]
"""

def levelTraversalBT(root):
    if not root:
        return []
    queue = deque()
    result = []
    next = []
    current = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        current.append(node.val)
        #print(current)
        if node.left:
            next.append(node.left)
        if node.right:
            next.append(node.right)
        if not queue:
            queue = deque(next)
            next = []
            result.append(current)
            current = []

    return result

# root = constructBT([3,9,20,None,None,15,7],0)
# print(levelTraversalBT(root))

########################################################################################################################
#Leetcode 94 - Binary Tree Inorder Traversal

"""
Description:
Given a binary tree, return the inorder traversal of its nodes’ values.

Example:
Input: [1,null,2,3]

   1
    \
     2
    /
   3
Output: [1,3,2]

Follow up:
Recursive solution is trivial, could you do it iteratively?
"""

def btInorder(root):
    if not root:
        return []
    stack = []
    result = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            result.append(node.val)
            root = node.right

    return result

# root = constructBT([1, None, 2, None, None, 3],0)
# print(btInorder(root))

########################################################################################################################
#Leetcode 100 - Same Tree
"""
Description:
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:

     1         1
    / \       / \
   2   3     2   3

  [1,2,3],   [1,2,3]
Output: true

Example 2:
Input:

     1         1
    /           \
   2             2

  [1,2],     [1,null,2]
Output: false

Example 3:
Input:

     1         1
    / \       / \
   2   1     1   2

  [1,2,1],   [1,1,2]
Output: false
"""
def isSameTree(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 and root2:
        return False
    if root1 and not root2:
        return False
    queue1 = deque()
    queue2 = deque()
    queue1.append(root1)
    queue2.append(root2)
    while queue1 and queue2:
        node1 = queue1.popleft()
        node2 = queue2.popleft()
        if node1.val != node2.val:
            return False
        if node1.left and node2.left:
            queue1.append(node1.left)
            queue2.append(node2.left)
        elif node1.left and not node2.left:
            return False
        elif not node1.left and node2.left:
            return False
        if node1.right and node2.right:
            queue1.append(node1.right)
            queue2.append(node2.right)
        elif node1.right and not node2.right:
            return False
        elif not node1.right and node2.right:
            return False
    return True


# root1 = constructBT([1,2,3],0)
# root2 = constructBT([1,2,3],0)
# print(isSameTree(root1,root2))

# root1 = constructBT([1,2],0)
# root2 = constructBT([1,None,2],0)
# print(isSameTree(root1,root2))


# root1 = constructBT([1,2,1],0)
# root2 = constructBT([1,1,2],0)
# print(isSameTree(root1,root2))

########################################################################################################################
#Leetcode 100 - Same Tree use stack

def isSameTree2(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 and root2:
        return False
    if root1 and not root2:
        return False
    stack = []
    while stack or root1 or root2:
        if root1 and root2:
            stack.append(root1)
            stack.append(root2)
            root1 = root1.left
            root2 = root2.left
        elif not root1 and not root2:
            node1 = stack.pop()
            node2 = stack.pop()
            if node1.val != node2.val:
                return False
            root1 = node1.right
            root2 = node2.right
        else:
            return False
    return True


# root1 = constructBT([1,2,3],0)
# root2 = constructBT([1,2,3],0)
# print(isSameTree2(root1,root2))

# root1 = constructBT([1,2],0)
# root2 = constructBT([1,None,2],0)
# print(isSameTree2(root1,root2))


# root1 = constructBT([1,2,1],0)
# root2 = constructBT([1,1,2],0)
# print(isSameTree(root1,root2))

########################################################################################################################
#Leetcode 101 - Symmetric Tree
"""
Description:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example:
This binary tree [1,2,2,3,4,4,3] is symmetric:

     1
    / \
   2   2
  / \ / \
 3  4 4  3
 
But the following [1,2,2,null,3,null,3] is not:

     1
    / \
   2   2
    \   \
    3    3
    
"""

class Solution():
    def findSolution(self, root):
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self,root1, root2):
        if not root1 and not root2:
            return True
        if root1 and not root2:
            return False
        elif not root1 and root2:
            return False
        stack = []
        stack.append(root1)
        stack.append(root2)
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if node1.val != node2.val:
                return False
            if node1.left and node2.right:
                stack.append(node1.left)
                stack.append(node2.right)
            elif not node1.left and node2.right:
                return False
            elif node1.left and not node2.right:
                return False
            if node1.right and node2.left:
                stack.append(node1.right)
                stack.append(node2.left)
            elif not node1.right and node2.left:
                return False
            elif node1.right and not node2.left:
                return False
        return True

# root = constructBT([1,2,2,3,4,4,3],0)
# solution = Solution()
# print(solution.findSolution(root))

# root = constructBT([1, 2, 2, None, 3, None, 3],0)
# solution = Solution()
# print(solution.findSolution(root))

########################################################################################################################
#Leetcode 104 - Maximum Depth of Binary Tree
"""
Description:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note:
A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

     3
    / \
   9  20
     /  \
    15   7
 
return its depth = 3
"""
def maximumDepthBT(root):
    if not root:
        return 0
    stack = []
    maxDepth = 1
    stack.append([root,1])
    while stack:
        nodelist = stack.pop()
        maxDepth = max(maxDepth, nodelist[1])
        if nodelist[0].right:
            #maxDepth = max(maxDepth, nodelist[1]+1)
            stack.append([nodelist[0].right, nodelist[1]+1])
        if nodelist[0].left:
            #maxDepth = max(maxDepth, nodelist[1] + 1)
            stack.append([nodelist[0].left, nodelist[1] + 1])

    return maxDepth

# root = constructBT([3,9,20,None,None,15,7], 0)
# print(maximumDepthBT(root))

def maximumDepthBT2(root):
    if not root:
        return 0
    queue = deque()
    queue.append([root,1])
    maxDepth = 1
    while queue:
        nodelist = queue.popleft()
        maxDepth = max(maxDepth, nodelist[1])
        if nodelist[0].left:
            queue.append([nodelist[0].left, nodelist[1]+1])
        if nodelist[0].right:
            queue.append([nodelist[0].right, nodelist[1]+1])
    return maxDepth

# root = constructBT([3,9,20,None,None,15,7], 0)
# print(maximumDepthBT2(root))
########################################################################################################################
#Leetcode 144 - Binary Tree Preorder Traversal
"""
Description:
Given a binary tree, return the preorder traversal of its nodes’ values.

Example:
Input: [1,null,2,3]

  1
    \
     2
    /
   3
Output: [1,2,3]
"""

def preorderTraversalBT(root):
    if not root:
        return []
    stack = []
    result = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result

# root = constructBT( [1,None,2,None, None, 3],0)
# print(preorderTraversalBT(root))

########################################################################################################################
#Leetcode 145 - Binary Tree Postorder Traversal
"""
Description:
Given the root of a binary tree, return the postorder traversal of its nodes’ values.

Follow up:
Recursive solution is trivial, could you do it iteratively?

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Example 4:

Input: root = [1,2]
Output: [2,1]

Example 5:

Input: root = [1,null,2]
Output: [2,1]
"""
def DFS_postorder(root):
    if not root:
        return []
    result = []
    if root.left is not None:
        result += DFS_postorder(root.left)
    if root.right is not None:
        result += DFS_postorder(root.right)
    result.append(root.val)
    return result

#root = constructBT([1,2,3,4,5,None,None,6],0)
#print(DFS_postorder(root))

def postOrderBT(root):
    if not root:
        return []
    queue = deque()
    result = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        result.append(node.val)
        #print(result)
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    #print('result:',result)
    result.reverse()
    #print('result:', result)
    return result

# root = constructBT([1,None,2,None, None,3],0)
# print(postOrderBT(root))

########################################################################################################################
#Leetcode 226 - Invert Binary Tree
"""
Description:
Invert a binary tree.

Example:
Input:

      4
    /   \
   2     7
  / \   / \
 1   3 6   9
 
Output:

      4
    /   \
   7     2
  / \   / \
 9   6 3   1
 
"""

def invertBT(root):
    if not root:
        return None
    queue = deque()
    queue.append(root)
    root1 = treeNode(root.val)
    queue.append(root1)
    while queue:
        node = queue.popleft()
        node1 = queue.popleft()
        if node.left:
            node1.right = treeNode(node.left.val)
            queue.append(node.left)
            queue.append(node1.right)
        if node.right:
            node1.left = treeNode(node.right.val)
            queue.append(node.right)
            queue.append(node1.left)
    return root1
# root = constructBT([4,2,7,1,3,6,9],0)
# root1 = invertBT(root)
# print(levelTraversalBT(root1))

########################################################################################################################
#Leetcode 257 - Binary Tree Paths
"""
Description:
Given a binary tree, return all root-to-leaf paths.

Note:
A leaf is a node with no children.

Example:
Input:

      1
    /   \
   2     3
    \
     5
   
Output: ["1->2->5", "1->3"]
"""

def btPath(root):
    if not root:
        return []
    result = []
    current  = ""
    queue = deque()
    queue.append([root, current])
    while queue:
        nodelist = queue.popleft()
        nodelist[1] += str(nodelist[0].val)
        if not nodelist[0].right and not nodelist[0].left:
            result.append(nodelist[1])
        if nodelist[0].left:
            queue.append([nodelist[0].left, nodelist[1]+"->"])
        if nodelist[0].right:
            queue.append([nodelist[0].right, nodelist[1]+"->"])
    return result

# root = constructBT([1,2,3,None, 5],0)
# print(btPath(root))

########################################################################################################################
#Leetcode 515 - Find Largest Value in Each Tree Row
"""
Description:
Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

Example 1:
Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]

Example 2:
Input: root = [1,2,3]
Output: [1,3]

Example 3:
Input: root = [1]
Output: [1]

Example 4:
Input: root = [1,null,2]
Output: [1,2]

Example 5:
Input: root = []
Output: []
"""

def largestValLevel(root):
    if not root:
        return []
    queue = deque()
    current = []
    next = []
    result = []
    queue.append(root)
    while queue:
        node = queue.popleft()
        current.append(node.val)

        if node.left:
            next.append(node.left)
        if node.right:
            next.append(node.right)

        if not queue:
            print(current)
            maxNum = max(current)
            result.append(maxNum)
            current = []
            queue = deque(next)
            next = []
    return result
# root = constructBT([1,3,2,5,3,None,9],0)
# print(largestValLevel(root))

########################################################################################################################
#Leetcode 559 - Maximum Depth of N-ary Tree
"""
Description:
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

Example 2:
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 5
"""

def naryMaxDepth(root):
    if not root:
        return 0
    stack = []
    maxDepth = 0
    stack.append([root,1])
    while stack:
        nodelist = stack.pop()
        maxDepth = max(maxDepth, nodelist[1])
        for child in nodelist[0].children:
            if child:
                stack.append([child,nodelist[1]+1])





########################################################################################################################
#Leetcode 589 - N-ary Tree Preorder Traversal
"""
Leetcode 589 - N-ary Tree Preorder Traversal
Description:
Given an n-ary tree, return the preorder traversal of its nodes’ values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:
Recursive solution is trivial, could you do it iteratively?

Example 1:
"""
def naryTreePreorder(root):
    if not root:
        return []
    stack = []
    result = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        for child in node.children().reverse():
            if child:
                stack.append(child)
