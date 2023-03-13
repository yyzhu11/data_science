#Leetcode169 - Majority Element
"""
Description:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times，

You may assume that the array is non-empty and the majority element always exist in the array.

[3,3,3,3,4,5,6]

Example1:
Input: [3,2,3]

Output: 3

Example2:
Input: [2,2,1,1,1,2,2]Output: 2
"""

# print(findMajority([2,2,1,1,1,2,2]))
# print(findMajority([3,2,3]))

###########################################################################################
#Leetcode283 - Move Zeroes
"""
Space comlexity:O(1) vs O(N)

Description:
Given an array nums, write a function to move all 0’s to the end of it while maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
Example:
Input: [0,1,0,3,12], Output: [1,3,12,0,0]

"""

#print(moveZeroes([0,1,0,3,12]))

###########################################################################################
#Leetcode26 - Remove Duplicates from Sorted Array
"""
Description:
Given a sorted array nums, remove the duplicates in -place
such that each element appear only once and return the new length.

Do not allocate extra space
for another array, you must do this by modifying the input array in -place with O(1) extra memory.

Example 1:
Given nums = [1, 1, 2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:
Given nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
"""


#print(removeDup([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

#######################################################################################
#Leetcode438 - Find All Anagrams in a String
"""
Description:
Given a string s and a non-empty string p, find all the start indices of p’s anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:
Input: s: "cbaebabacd" p: "abc"
Output: [0, 6]

Explanation:

The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:
Input:s: "abab" p: "ab"
Output: [0, 1, 2]

Explanation:

The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


#print(findAllAnagram("cbaebabacd","abc"))
#print(findAllAnagram("abab","ab"))


# print(findAllAnagram2("cbaebabacd","abc"))
# print(findAllAnagram2("abab","ab"))

#######################################################################################
#Leetcode 27-Remove Element

"""
Description:
Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn’t matter what you leave beyond the new length.

Example1:
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.It doesn’t matter what you leave beyond the returned length.

Example2:
Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.It doesn’t matter what values are set beyond the returned length.

"""



# print(removeVal([3,2,2,3],3))
# print(removeVal([0,1,2,2,3,0,4,2],2))

#######################################################################################
#Leetcode 125-Valid Palindrome

"""
Description:
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note:
For the purpose of this problem, we define empty string as valid palindrome.

Example1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example2:
Input: "race a car"
Output: false

"""


#print(isValidPalindrom("A man, a plan, a canal: Panama"))

#######################################################################################
#Leetcode167 - Two Sum II - Input array is sorted
"""
Description:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
Input: numbers = [2,7,11,15], target = 9

Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


#print(twoSum([2,7,11,15],9))

#######################################################################################
#Leetcode 344-Reverse String
"""
Description:
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Example1:
Input: ["h","e","l","l","o"]

Output: ["o","l","l","e","h"]

Example2:
Input: ["H","a","n","n","a","h"]

Output: ["h","a","n","n","a","H"]

"""



#print(reverseString(["H","a","n","n","a","h"]))

#######################################################################################
#Leetcode 345-Reverse Vowels of a String
"""
Description:
Write a function that takes a string as input and reverse only the vowels of a string.

Note:
The vowels does not include the letter "y".

Example1:
Input: "hello"
Output: "holle"

Example2:
Input: "leetcode"
Output: "leotcede"
"""


# print(reverseVowels("hello"))
# print(reverseVowels("leetcode"))


#######################################################################################
#Leetcode 905-Sort Array By Parity

"""
Description:
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Note:
<= A.length <= 5000
0 <= A[i] <= 5000
Example:
Input: [3,1,2,4]

Output: [2,4,3,1]

The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
"""

#print(sortByParity([3,1,2,4]))

#######################################################################################
#Leetcode 922-Sort Array By Parity II

"""
Description:
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Note:
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
Example:
Input: [4,2,5,7]
Output: [4,5,2,7]

Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""




#print(sortByParity2([4,2,5,7]))

#######################################################################################
#Leetcode 977-Squares of a Sorted Array

"""
Description:
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
Example1:
Input: [-4,-1,0,3,10]

Output: [0,1,9,16,100]

Example2:
Input: [-7,-3,2,3,11]

Output: [4,9,9,49,121]
"""


# print(sortSqured([-4,-1,0,3,10]))
#
# print(sortSqured([-7,-3,2,3,11]))

#######################################################################################
#Leetcode 1004 (optional)-Max Consecutive Ones III

"""
Description:
Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

Note:
1 <= A.length <= 20000
0 <= K <= A.length
A[i] is 0 or 1
Example1:
Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6

Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example2
Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10

Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""



#print(maxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0], 2))

#print(maxConsecutiveOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))