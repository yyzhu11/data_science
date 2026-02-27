#leetcode 136. Single Number
"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
Input: [2,2,1] Output: 1
"""


def singleOne(nlist):
    myDict = {}
    for i in nlist:
        myDict[i] = myDict.get(i, 0) + 1
    for i in myDict.keys():
        if myDict[i] == 1:
            return i

#print(singleOne([2,2,1]))

def SingleOne2(nlist):
    if not nlist:
        return None
    result = nlist[0]
    for i in range(1, len(nlist)):
        result = nlist[i] ^ result
    return result

#print(SingleOne2([2,2,1]))


##############################################################################################################
#leetcode: 169. Majority Element

"""
Description:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

Note:
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3], Output: 3
"""

def majorityElement(nlist):
    if not nlist:
        return None
    myDict = {}
    for i in nlist:
        myDict[i] = myDict.get(i, 0) + 1
    for i in myDict.keys():
        if myDict[i] > len(nlist) // 2:
            return i

#print(majorityElement([3,2,3]))


##############################################################################################################
#leetcode: 217. Contains Duplicate

"""
Description:
Given an array of integers, find if the array contains any duplicates.

Note:
Your function should return true if any value appears at least twice in the array, and it should return false 
if every element is distinct.

Example:
Input: [1,2,3,1]

Output: true
"""
def containDup(nlist):
    if not nlist:
        return False
    myDict = {}
    for i in nlist:
        if i in myDict.keys():
            return True
        else:
            myDict[i] = 1
    return False

#print(containDup([1,2,3,1]))
#print(containDup([1,2,3]))


##############################################################################################################
"""
1. Two Sum
Description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Note:
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1]
"""

def twoSum(nlist, target):
    if not nlist:
        return []
    n = len(nlist)
    myDict = {}
    for i in range(n):
        myDict[nlist[i]] = i
    for i in myDict.keys():
        if (target - i) in myDict.keys():
            return [myDict[i], myDict[target-i]]
    return []

#print(twoSum([2, 7, 11, 15],9))


##############################################################################################################
""" 
Leetcode167 - Two Sum II - Input array is sorted
Description:
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
Input: numbers = [2,7,11,15], target = 9

Output: [1,2]

Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

"""

def twoSum2(nlist, target):
    myDict = {}
    for i in range(len(nlist)):
        num = target - nlist[i]
        if num in myDict.keys():
            return [myDict[num]+1, i+1]
        myDict[nlist[i]] = i

#print(twoSum2([2,7,11,15],9))


##############################################################################################################
#Leetcode 219-Contains Duplicate II
"""
Description:
Given an array of integers and an integer k,find out whether there are two distinct indices i and j
in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example1:
Input: nums = [1,2,3,1], k = 3, Output: true

Example2:
Input: nums = [1,0,1,1], k = 1, Output: true

Example3:
Input: nums = [1,2,3,1,2,3], k = 2, Output: false
"""

def containDup2(nlist, k):
    if not nlist:
        return False
    myDict = {}
    for i in range(len(nlist)):
        if nlist[i] in myDict.keys():
            if abs(i - myDict[nlist[i]]) <= k:
                return True

        myDict[nlist[i]] = i
    return False

# print(containDup2([1,2,3,1],3))
# print(containDup2([1,0,1,1],1))
# print(containDup2([1,2,3,1,2,3],2))


##############################################################################################################
#Leetcode 242-Valid Anagram
"""
Description:
Given two strings s and t , write a function to determine if t is an anagram of s.

Note: You may assume the string contains only lowercase alphabets.

Example1:
Input: s = "anagram", t = "nagaram", Output: true

Example2:
Input: s = "rat", t = "car", Output: false

"""
from collections import Counter
def isAnagram(s, t):
    if not s and not t:
        return True

    scounter = Counter(s)
    tcounter = Counter(t)

    if scounter == tcounter:
        return True
    else:
        return False

#print(isAnagram("anagram", "nagaram"))
#print(isAnagram("rat", "car"))


##############################################################################################################
#Leetcode 268- Missing Number
"""
Description:
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

Example1:
Input: [3,0,1], Output: 2

Example2:
Input: [9,6,4,2,3,5,7,0,1], Output: 8

"""

def missingNum(nlist):
    numSum = sum(nlist)
    n = len(nlist)
    result = n*(n+1)//2
    return result-numSum

#print(missingNum([9,6,4,2,3,5,7,0,1]))


##############################################################################################################
#Leetcode 349-Intersection of Two Arrays
"""
Description:
Given two arrays, write a function to compute their intersection.
The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Note:
Each element in the result must be unique.
The result can be in any order.
Example1:
Input: nums1 = [1,2,2,1], nums2 = [2,2] , Output: [2]

Example2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4], Output: [9,4]

"""

def intersectionTwoArrays(num1, num2):
    numDict = {}
    result = []
    for i in num1:
        numDict[i] = 1
    for i in num2:
        if i in numDict.keys() and numDict[i] != 0:
            result.append(i)
            numDict[i] -= 1

    return result

#print(intersectionTwoArrays([1,2,2,1], [2,2]))
#print(intersectionTwoArrays([4,9,5], [9,4,9,8,4]))


##############################################################################################################
# Leetcode 350-Intersection of Two Arrays II

"""
Description:
Given two arrays, write a function to compute their intersection.

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Example1:
Input: nums1 = [1,2,2,1], nums2 = [2,2], Output: [2,2]

Example2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4], Output: [4,9]

"""

def intersectionTwoArraysII(num1, num2):
    numDict = {}
    result = []
    for i in num1:
        numDict[i] = numDict.get(i,0)+1
    for i in num2:
        if i in numDict.keys() and numDict[i] > 0:
            result.append(i)
            numDict[i] -= 1
    return result

#print(intersectionTwoArraysII([1,2,2,1],[2,2]))


##############################################################################################################
#Leetcode 389-Find the Difference

"""
Description:
Given two strings s and t which consist of only lowercase letters.String t is generated by random shuffling string s and
then add one more letter at a random position.Find the letter that was added in t.

Example:
s = "abcd"   t = "abcde", Output: e

Explanation:
"e" is the letter that was added.

s = "abba" t="abbba", output: b
"""

def addedOne(s, t):
    myDict = {}
    numS = len(s)
    numT = len(t)
    if numS > numT:
        s, t = t, s
    for i in s:
        myDict[i] = myDict.get(i,0) + 1
    for i in t:
        if i in myDict.keys() and myDict[i] > 0:
            myDict[i] -= 1
        else:
            return i

#print(addedOne("abcd", "abcde"))
#print(addedOne("abba", "abbba"))
##############################################################################################################
#Leetcode 442-Find All Duplicates in an Array
"""
Description:
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Example:
Input: [4,3,2,7,8,2,3,1], output [2,3]
Input: nums = [1,1,2], Output: [1]
Input: nums = [1,2,2], Output: [2]
"""
def findDup(nlist):
    if not nlist:
        return []
    result = []
    numsDict = {}

    for i in nlist:
        numsDict[i] = numsDict.get(i, 0) + 1
    for i in numsDict.keys():
        if numsDict[i] > 1:
            result.append(i)
    return result


def findDup2(nlist):
    n = len(nlist)
    result = []
    for i in range(len(nlist)):
        j = nlist[i] % n
        nlist[j] += n
    for i in range(len(nlist)):
        if nlist[i] > 2*n:
            if i == 0:
                result.append(n)
            else:
                result.append(i)
    return result

#print(findDup([4,3,2,7,8,2,3,1]))
#print(findDup([1,1,2]))

# print(findDup2([4,3,2,7,8,2,3,1]))
# print(findDup2([1,1,2]))
# print(findDup2([1,2,2]))


##############################################################################################################
#Leetcode 448-Find All Numbers Disappeared in an Array
"""
Description:
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
Find all the elements of [1, n] inclusive that do not appear in this array.
Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:[4,3,2,7,8,2,3,1] ,Output: [5,6]
"""

def findNumberDisappeared(nlist):
    return list(set(range(1,len(nlist)+1)) -set(nlist))

def findNumberDisappeared2(nlist):
    n = len(nlist)
    result = []
    for i in range(n):
        j = nlist[i] % n
        nlist[j] += n

    for i in range(n):
        if nlist[i] < n:
            if i == 0:
                result.append(n)
            else:
                result.append(i)
    return result



#print(findNumberDisappeared([4,3,2,7,8,2,3,1]))


#print(findNumberDisappeared2([4,3,2,7,8,2,3,1]))

##############################################################################################################
#Leetcode 575-Distribute Candies
"""
Description:
You have n candies, the ith candy is of type candies[i].

You want to distribute the candies equally between a sister and a brother so that each of them gets n / 2 candies (n is even).

The sister loves to collect different types of candies, so you want to give her the maximum number of different types of candies.

Return the maximum number of different types of candies you can give to the sister.

Example1:
Input: candies =  [1,1,2,3] , Output: 2

Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies.

Example2:
Input: candies = [1,1,2,2,3,3], Output: 3

Explanation: There are three different kinds of candies (1, 2 and 3), and two candies for each kind.Optimal distribution: 
The sister has candies [1,2,3]

and the brother has candies [1,2,3], too. The sister has three different kinds of candies.

Example3:
Input: candies = [1,1], Output: 1

Example4:
Input: candies = [1,11] , Output: 1

Example5:
Input: candies = [2,2], Output: 1

"""

def distributeCandy(nlist):
    n = len(nlist) //2
    m = len(set(nlist))

    return min(n, m)

#print(distributeCandy([1,1,2,3]))
#print(distributeCandy([1,1,2,2,3,3]))