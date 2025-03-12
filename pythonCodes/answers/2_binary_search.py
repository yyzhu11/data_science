##########################################################################################################################################
#binary
#Example: Search Insert Position
"""
Description:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Note:
You may assume no duplicates in the array.

Example:
Input: [1,3,5,6], 5 Output: 2

Example 2:

Input: [1,3,5,6], 2 Output: 1

"""


##########################################################################################################################################
#Leetcode 69-Sqrt(x)

"""
Description:
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example1:
Input: 4 , Output: 2

Example2:
Input: 8, Output: 2

"""



##########################################################################################################################################
#Leetcode167 - Two Sum II - Input array is sorted
"""
Description:
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
Input: numbers = [2,7,11,15], target = 9, Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

##########################################################################################################################################
#Leetcode 278-First Bad Version
"""
Description:
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product

fails the quality check.Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version.

You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version:

call isBadVersion(3) -> false

call isBadVersion(5) -> true

call isBadVersion(4) -> true

Then 4 is the first bad version.

"""

##########################################################################################################################################
#Leetcode 349-Intersection of Two Arrays
"""
Description:
Given two arrays, write a function to compute their intersection.

Note:
Each element in the result must be unique./li>
The result can be in any order.
Example1:
Input: nums1 = [1,2,2,1], nums2 = [2,2], Output: [2]

Example2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4], Output: [9,4]
"""


##########################################################################################################################################
#Leetcode 367-Valid Perfect Square
"""
Description:
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up:
Do not use any built-in library function such as sqrt.

Example1:
Input: num = 16, Output: true

Example2:
Input: num = 14, Output: false
"""



##########################################################################################################################################
#Leetcode 374-Guess Number Higher or Lower

"""
Description:
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I’ll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower

1 : My number is higher

0 : Congrats! You got it!

Example:
Input: n = 10, pick = 6, Output: 6

"""


##########################################################################################################################################
#Leetcode 441-Arranging Coins
"""
Leetcode 441-Arranging Coins
Description:
You have a total of n coins that you want to form in a staircase shape, 
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example1:
X
XX
XX
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
(1,2, 3,...k)
"""



##########################################################################################################################################
#Leetcode 70-Climbing Stairs
"""
Description:
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example1:
Input: 2

Output: 2

Explanation: There are two ways to climb to the top.

1. 1 step + 1 step

2. 2 steps

Example2:
Input: 3

Output: 3

Explanation: There are three ways to climb to the top.

1. 1 step + 1 step + 1 step

2. 1 step + 2 steps

3. 2 steps + 1 step

Constraints:
1 <= n <= 45
"""

##########################################################################################################################################
#Leetcode 744-Find Smallest Letter Greater Than Target
"""
Description:
Given a list of sorted characters letters containing
only lowercase letters, and given a target letter
target, find the smallest element in the list that is larger than the given target.
Letters also wrap around.For example, if the target is target = "z" and letters =["a", "b"], the answer is "a".

Note:
letters has a length in range[2, 10000]. letters
consists of  lowercase letters, and contains
at least 2 unique letters. target is a lowercase letter.

"""
"""
Example:
Input:
letters = ["c", "f", "j"] target = "a" , Output: "c"

Input:
letters = ["c", "f", "j"] target = "c" Output: "f"

Input:
letters = ["c", "f", "j"] target = "d" Output: "f"

Input:
letters = ["c", "f", "j"] target = "g" Output: "j"

Input:
letters = ["c", "f", "j"] target = "j" Output: "c"

Input:
letters = ["c", "f", "j"] target = "k" Output: "c"

"""

##########################################################################################################################################
#Leetcode 852-Peak Index in a Mountain Array
"""
Description:
Let’s call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Note:
3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
Example1:
Input: [0,1,0], Output: 1

Example2:
Input: [0,2,1,0], Output: 1
"""



##########################################################################################################################################
#Leetcode 287 (optional)-Find the Duplicate Number
"""
Description:
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
Example1:
Input: [1,3,4,2,2], Output: 2

Example2:
Input: [3,1,3,4,2], Output: 3
"""

#-------------------------------additional from other books---------------------------------------------------------------------------
######################################################################################################################################
#Leetcode 50 
"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn)
"""
