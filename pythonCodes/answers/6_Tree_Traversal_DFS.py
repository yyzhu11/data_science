#Depth First Search(DFS)
'''
definition: treeNode, constructBT, depthFirstSearch(pre-order), DFS_inorder(in-order), DFS_postorder(post-order)
printBT
'''
class treeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def constructBT(nlist, index):
    if not nlist:
        return None
    if index >= len(nlist) or nlist[index] is None:
        return None
    root = treeNode(nlist[index])
    if (2*index + 1) < len(nlist):
        root.left = constructBT(nlist, 2*index + 1)
    if (2*index + 2) < len(nlist):
        root.right = constructBT(nlist, 2*index + 2)
    return root

def depthFirstSearch(root): #pre-order
    if not root:
        return []
    result = []
    result.append(root.val)
    if root.left:
        result += depthFirstSearch(root.left)
    if root.right:
        result += depthFirstSearch(root.right)
    return result


#root = constructBT([1,2,3,4,5,None, None,6],0)
#print(depthFirstSearch(root))

def DFS_inorder(root):
    if not root:
        return []
    result = []
    if root.left:
        result += DFS_inorder(root.left)
    result.append(root.val)
    if root.right:
        result += DFS_inorder(root.right)
    return result

# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(DFS_inorder(root))

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

from collections import deque
def printBT(root):
    result = []
    queue = deque()
    if root:
        queue.append(root)
        while len(queue) > 0 and queue.count(None) != len(queue):
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

    return result



#root = constructBT([1,2,3,4,5,None,None,6],0)
#print(DFS_postorder(root))

########################################################################################################
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
   9   20
   /    \
  15     7
          \
           8
 
return its depth = 3.

[1,null,2]

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2

"""
def maximumDepthBT(root):
    if not root:
        return 0
    result = 1 + max(maximumDepthBT(root.left), maximumDepthBT(root.right))
    return result



# root = constructBT([3,9,20,None,None,15,7],0)
# print(maximumDepthBT(root))

# root = constructBT([1, None, 2],0)
# print(maximumDepthBT(root))

########################################################################################################
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
"""
"""
Output: ["1->2->5", "1->3"]
"""
class Solution():
    def __init__(self):
        self.result = []

    def getAllPath(self, root):
        if not root:
            return []
        self.binaryTreePath(root, "", self.result)
        print(self.result)

    def binaryTreePath(self, root, path, result):
        if not root.left and not root.right:
            result.append(path+str(root.val))

        if root.left:
            self.binaryTreePath(root.left, path+str(root.val)+"->", result)

        if root.right:
            self.binaryTreePath(root.right, path+ str(root.val) + "->", result)


# root = constructBT([1,2,3,None,5],0)
# solution = Solution()
# solution.getAllPath(root)

########################################################################################################
#Leetcode94 - Binary Tree Inorder Traversal
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
"""
def btInorder(root):
    if not root:
        return []
    result = []
    if root.left:
        result += btInorder(root.left)
    result.append(root.val)
    if root.right:
        result += btInorder(root.right)

    return result



# root = constructBT([1, None, 2, None, None, 3],0)
# print(btInorder(root))
########################################################################################################
#Leetcode 111 - Minimum Depth of Binary Tree

"""
Description:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note:
A leaf is a node with no children.
Example:
Given binary tree [3,9,20,null,null,15,7],

      3
    / \
   9  20
     /  \
    15   7
 
return its minimum depth = 2.
"""

def minimumDepthBT(root):
    if not root:
        return 0
    return 1 + min(minimumDepthBT(root.right), minimumDepthBT(root.left))

# root = constructBT([3,9,20,None,None,15,7],0)
# print(minimumDepthBT(root))

########################################################################################################
#Leetcode 112 - Path Sum

"""
Description:
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note:
A leaf is a node with no children.
Example:
Given the below binary tree and sum = 22,

      5
    / \
   4   8
  /   / \
 11  13  4
/  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
class Solution():
    def __init__(self):
        self.sum = 0

    def isExist(self, root, target):
        if not root:
            return False
        result = []
        self.pathSum(root, self.sum, result)
        print(result)
        if target in result:
            return True
        else:
            return False

    def pathSum(self, root, sumTotal, result):
        if not root.left and not root.right:
            sumTotal += root.val
            result.append(sumTotal)
        if root.left:
            self.pathSum(root.left, sumTotal + root.val, result)
        if root.right:
            self.pathSum(root.right, sumTotal + root.val, result)



# root = constructBT([5,4,8,11, None, 13, 4, 7, 2, None, None, None,None, None,1],0)
# print(printBT(root))
# solution = Solution()
# print(solution.isExist(root, 22))


# root = constructBT([1, 2, 3],0)
# solution = Solution()
# print(solution.isExist(root, 5))

########################################################################################################
#Leetcode 144 - Binary Tree Preorder Traversal
"""
Description:
Given a binary tree, return the preorder traversal of its nodes’ values.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Example:
Input: [1,null,2,3]

   1
    \
     2
    /
   3
Output: [1,2,3]
"""

########################################################################################################
#Leetcode 199 - Binary Tree Right Side View
"""
Description:
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:
Input: [1,2,3,null,5,null,4]

Output: [1, 3, 4]

Explanation:

      1            <---
    /   \
   2     3         <---
    \     \
     5     4       <---
"""
class Solution():
    def findIt(self, root):
        if not root:
            return []
        result = [root.val]
        self.rightSideView(root, result)
        print(result)

    def rightSideView(self, root, result):
        if not root.right and not root.left:
            return
        if root.right:
            result.append(root.right.val)
            self.rightSideView(root.right, result)
        elif not root.right and root.left:
            result.append(root.left.val)
            self.rightSideView(root.left, result)


# root = constructBT([1,2,3,None,5, None,4],0)
# solution = Solution()
# solution.findIt(root)

# root = constructBT([1,None,3],0)
# solution = Solution()
# solution.findIt(root)
########################################################################################################
#Leetcode 394 (optional) - Decode String
"""
Description:
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

ou may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
For example, there won’t be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Example 4:
Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"
"""
def encodeString(string):
    stack = []
    numList = []

    for s in string:
        #print(stack)
        if s == ']':
            newStr = ''
            while stack:
                c = stack.pop()
                if c == '[':
                    break
                else:
                    newStr = c + newStr
            #stack.pop() #pop '['
            num = stack.pop()
            newStr2 = newStr * num
            stack.append(newStr2)
        elif s == '[':
            if len(numList) > 0:
                str1 = ''.join(i for i in numList)
                num = int(str1)
                numList = []
                stack.append(num)
            stack.append(s)
        elif not s.isdigit():
            stack.append(s)
        elif s.isdigit():
            numList.append(s)
    return ''.join(i for i in stack)

#print(encodeString('3[a]2[bc]'))
#print(encodeString('2[abc]3[cd]ef'))
#print(encodeString('3[a2[c]]'))

########################################################################################################
#Leetcode 513 - Find Bottom Left Tree Value
"""
Description:
Given a binary tree, find the leftmost value in the last row of the tree.

Note:
You may assume the tree (i.e., the given root node) is not NULL.

Example 1:
Input:

     2
    / \
   1   3
 
Output: 1

Example 2:
Input:

     1
    / \
   2   3
  /   / \
 4   5   6
    /
   7
Output: 7
"""
class Solution():
    def findSolution(self, root):
        if not root:
            return None
        result = [[root.val, 0]]
        depth = 0
        self.findLeftmostValue(root,depth, result)
        print('*******')
        print(result[-1][0])

    def findLeftmostValue(self, root, depth, result):
        #if not root.left and not root.right:
            #result[depth][0] = root.val
            #result.append([root.val, depth])
        if root.left:
            if result[-1][1] < depth + 1:
                result.append([root.left.val, depth+1])
                #print(result)
            #result[depth+1][0] = root.left.val
            print(result)
            self.findLeftmostValue(root.left, depth+1, result)
        if root.right:
            if result[-1][1] < depth + 1:
                result.append([root.right.val, depth+1])
                #print(result)
            #result[depth+1][0] = root.right.val
            print(result)
            self.findLeftmostValue(root.right, depth+1, result)

# root = constructBT( [1,2,3,None,5,None,4],0)
# solution = Solution()
# solution.findSolution(root)

# root = constructBT( [2,1,3],0)
# solution = Solution()
# solution.findSolution(root)

# root = constructBT( [1,2,3,4,None,5,6, None, None, None, None, 7],0)
# solution = Solution()
# solution.findSolution(root)


########################################################################################################
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
"""
def maxRow(root):
    if not root:
        return []
    result = []
    queue = deque()
    queue.append(root)
    result.append(root.val)
    while queue:
        currentRow = []
        n = len(queue)
        #print(n)
        for i in range(n):
            node = queue.popleft()
            if node and node.left:
                currentRow.append(node.left.val)
                queue.append(node.left)
            if node and node.right:
                currentRow.append(node.right.val)
                queue.append(node.right)
        if len(currentRow)>0:
            result.append(max(currentRow))
    return result

# root = constructBT([1,3,2,5,3,None,9], 0)
# print(maxRow(root))
#
# root = constructBT([1,2,3], 0)
# print(maxRow(root))
#
# root = constructBT([1,None,2], 0)
# print(maxRow(root))






