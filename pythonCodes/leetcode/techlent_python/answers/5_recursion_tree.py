#recursion
#Example: Tribonacci
#Leetcode 1137 - N-th Tribonacci Number

"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.Given n, return the value of Tn.

Example 1:
Input: n = 4
Output: 4

Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:
Input: n = 25
Output: 1389537

"""
def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

#print(tribonacci(25))

def tribonacci2(n):
    T0 = 0
    T1 = 1
    T2 = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    for i in range(3, n+1):
        T3 = T0 + T1 + T2
        T0 = T1
        T1 = T2
        T2 = T3
    return T3

#print(tribonacci2(25))
########################################################################################################
#Tree

class treeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

########################################################################################################
#Leetcode104 - Maximum Depth of Binary Tree
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
return its depth = 3.
"""
from collections import deque
def constructBT(nlist, i):
    n = len(nlist)
    if i>= n or nlist[i] == None:
        return None
    root = treeNode(nlist[i])
    if (2*i + 1) < n:
        root.left = constructBT(nlist, 2*i + 1)
    if (2*i + 2)< n:
        root.right = constructBT(nlist, 2*i + 2)
    return root

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


#root = constructBT([3,9,20,None,None,15,7],0)

#print(printBT(root))
def maxDepthBT(root):
    if not root:
        return 0
    return max(maxDepthBT(root.right) +1, maxDepthBT(root.left) + 1)

#print(maxDepthBT(root))

########################################################################################################
#Leetcode67 - Add Binary
"""
Description:
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"

Output: "100"

Example 2:
Input: a = "1010", b = "1011"

Output: "10101"
"""
def addBinary(a, b):
    if not a:
        return b
    elif not b:
        return a

    if a[-1] == '0' and b[-1] == '0':
        return addBinary(a[:-1],b[:-1]) + '0'
    elif a[-1] == '1' and b[-1] == '0':
        return addBinary(a[:-1],b[:-1]) + '1'
    elif a[-1] == '0' and b[-1] == '1':
        return addBinary(a[:-1],b[:-1]) + '1'
    elif a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[:-1],b[:-1]),'1') + '0'


#print(addBinary("1010", "1011"))

########################################################################################################
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
def sameTree(root1, root2):
    if not root1 and not root2:
        return True
    elif not root1 and root2:
        return False
    elif root1 and not root2:
        return False
    return sameTree(root1.right, root2.right) and sameTree(root1.left, root2.left)


########################################################################################################
#Leetcode 108 - Convert Sorted Array to Binary Search Tree
"""
Description:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],One possible answer is: [0,-3,9,-10,null,5], 
which represents the following height balanced BST:

      0
    / \
  -3   9
  /   /
-10  5

"""
def balancedBST(nlist):
    if not nlist:
        return None
    mid = len(nlist) // 2
    root = treeNode(nlist[mid])
    root.left = balancedBST(nlist[0:mid])
    root.right = balancedBST(nlist[mid+1:])
    return root
#root = balancedBST([-10,-3,0,5,9])
#print(printBT(root))

########################################################################################################
#Leetcode 559 - Maximum Depth of N-ary Tree
"""
Description:
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, 
each group of children is separated by the null value (See examples).
Input: root = [1,null,3,2,4,null,5,6]
Output: 3

[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

"""
def maxDepthNaryTree(root):
    if not root:
        return 0
    result = 0
    for child in root.children:
        result = max(result, maxDepthNaryTree(child))
    return 1 + result


########################################################################################################
#Leetcode 589 - N-ary Tree Preorder Traversal
"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. 
Each group of children is separated by the null value (See examples)

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
"""

def preorderNaryTree(root):
    if not root:
        return []
    result = []
    result.append(root.val)
    for child in root.children:
            result = result + preorderNaryTree(child)

    return result



########################################################################################################
#Leetcode 617 - Merge Two Binary Trees
"""
Description:
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise,

the NOT null node will be used as the node of new tree.

Note:
The merging process must start from the root nodes of both trees.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""
def mergeTree(root1, root2):
    if not root1 and not root2:
        return None
    elif not root1 and root2:
        return root2
    elif root1 and not root2:
        return root1
    root = treeNode(root1.val + root2.val)
    root.left = mergeTree(root1.left, root2.left)
    root.right = mergeTree(root1.right, root2.right)

    return root

# root1 = constructBT([1,3,2,5],0)
# root2 = constructBT([2,1,3,None,4,None,7],0)
# root3 = mergeTree(root1, root2)
# print(printBT(root3))
########################################################################################################
#Leetcode 669 - Trim a Binary Search Tree

"""
Description:
Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L).

You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

Example 1:
Input: 
    1
   / \
  0   2

  L = 1
  R = 2

Output: 
    1
      \
       2
Example 2:
Input: 
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

Output: 
      3
     / 
   2   
  /
 1
"""
def trimBT(root, L, R):
    if not root:
        return None
    if root.val <= R and root.val >= L:
        if root.left and root.left.val < L:
            root.left = trimBT(root.left.right, L, R)
        if root.right and root.right.val > R:
            print(root.right.val)
            root.right = trimBT(root.right.left, L, R)
    elif root.val > R:
        root = trimBT(root.left. L, R)

    elif root.val < L:
        root = trimBT(root.right, L, R)
    return root

#root = constructBT([1, 0, 2],0)
#root1 = trimBT(root, 1, 2)
#print(printBT(root1))

# node1 = treeNode(1, None, None)
# node2 = treeNode(2, node1, None)
# node0 = treeNode(0, None, node2)
# node4 = treeNode(4, None, None)
# root = treeNode(3, node0, node4)
# #print(printBT(root))
# root1 = trimBT(root, 1, 3)
# print(printBT(root1))

########################################################################################################
#Leetcode 700 - Search in a Binary Search Tree
"""
Description:
Given the root node of a binary search tree (BST) and a value. 
You need to find the node in the BST that the node’s value equals the given value.

Return the subtree rooted with that node. If such node doesn’t exist, you should return NULL.

Example:
Given the tree:
    4
   / \
  2   7
 / \
1   3

And the value to search: 2
You should return this subtree:

    2     
    / \   
   1   3
In the example above, if we want to search the value 5, 
since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, 
therefore you would see the expected output (serialized tree format) as [], not null.
"""
def searchBT(root, target):
    if not root:
        return None
    if root.val == target:
        return root
    elif root.val > target:
        return searchBT(root.left, target)
    else:
        return searchBT(root.right, target)

# root = constructBT([4,2,7,1,3], 0)
# root1 = searchBT(root, 2)
# print(printBT(root1))

########################################################################################################
#Leetcode 938 - Range Sum of BST
"""
Description:
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
The binary search tree is guaranteed to have unique values.

Note:
The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15

Output: 32
Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
"""

def rangeSumBT(root, L, R):
    if not root:
        return 0
    sum = 0
    if root.val >= L and root.val <= R:
        sum += root.val
    sum += rangeSumBT(root.right, L, R) + rangeSumBT(root.left, L, R)
    return sum


#root = constructBT([10,5,15,3,7,None,18],0)
#print(rangeSumBT(root,7,15))

# root = constructBT([10,5,15,3,7,13,18,1,None,6],0)
# print(rangeSumBT(root,6,10))
########################################################################################################
#Leetcode 965 - Univalued Binary Tree
"""
Description:
A binary tree is univalued if every node in the tree has the same value.Return true if and only if the given tree is univalued.

Note:
The number of nodes in the given tree will be in the range [1, 100].
Each node’s value will be an integer in the range [0, 99].
Example 1:

Input: [1,1,1,1,1,null,1]

Output: true

Example 1:

Input: [2,2,2,5,2]

Output: false
"""
def univaluedBT(root):
    if not root:
        return True
    if root.val == 1:
        return univaluedBT(root.left) and univaluedBT(root.right)
    else:
        return False


# root = constructBT([2,2,2,5,2],0)
# print(univaluedBT(root))
#
# root = constructBT([1,1,1,1,1,None,1],0)
# print(univaluedBT(root))


