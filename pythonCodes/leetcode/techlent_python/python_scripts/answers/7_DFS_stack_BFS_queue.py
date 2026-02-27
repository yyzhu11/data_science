########################################################################################################
#Tree definition
# treeNode, constructBT, preorder,



#preorder


# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(recursive_DFS(root))

########################################################################################################################
#DFS with Stack - Preorder



# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(DFS_stack(root))
########################################################################################################################
#DFS with Stack: Inorder


# root = constructBT([1,2,3,4,5,None, None,6],0)
#
# print(DFS_inorder(root))

########################################################################################################################
#BFS with Queue


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


# root = constructBT([3,9,20,None,None,15,7], 0)
# print(maximumDepthBT(root))



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


#root = constructBT([1,2,3,4,5,None,None,6],0)
#print(DFS_postorder(root))



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

