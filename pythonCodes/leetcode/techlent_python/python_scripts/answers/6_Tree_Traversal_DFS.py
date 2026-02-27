#Depth First Search(DFS)
'''
definition: treeNode, constructBT, depthFirstSearch(pre-order), DFS_inorder(in-order), DFS_postorder(post-order)
printBT
'''



#root = constructBT([1,2,3,4,5,None, None,6],0)
#print(depthFirstSearch(root))



# root = constructBT([1,2,3,4,5,None, None,6],0)
# print(DFS_inorder(root))




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


# root = constructBT([1,3,2,5,3,None,9], 0)
# print(maxRow(root))
#
# root = constructBT([1,2,3], 0)
# print(maxRow(root))
#
# root = constructBT([1,None,2], 0)
# print(maxRow(root))






