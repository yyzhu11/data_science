########################################################################################################
#Leetcode 1137 - N-th Tribonacci Number
"""
Description:
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.Given n, return the value of Tn.

Example:
Input: n = 4

Output: 4

Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example:
Input: n = 25

Output: 1389537
"""


########################################################################################################
#Leetcode 70 - Climbing Stairs
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

"""


########################################################################################################
#Example: Climb Stairs with Min Cost
"""
Leetcode 746 - Min Cost Climbing Stairs
Description:
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Note:
1.cost will have a length in the range [2, 1000].

2.Every cost[i] will be an integer in the range [0, 999].

Example 1:
Input: cost = [10, 15, 20]

Output: 15

Explanation:
Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

Output: 6

Explanation:
Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""


#print(minCostClimbingStairs([10, 15, 20]))

########################################################################################################
#Leetcode 121 - Best Time to Buy and Sell Stock
"""
Description:
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]

Output: 5

Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]

Output: 0

Explanation:
In this case, no transaction is done, i.e. max profit = 0.
"""



#print(bestTimeStock([7,1,5,3,6,4]))
#print(bestTimeStock([7,6,4,3,1]))

########################################################################################################
#Leetcode 53 - Maximum Subarray
"""
Description:
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6

Explanation:
[4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, 
which is more subtle.
"""



#print(maxSubarray([-2,1,-3,4,-1,2,1,-5,4]))

########################################################################################################
#Leetcode 62 - Unique Paths
"""
Description:
A robot is located at the top-left corner of a m x n grid (marked "Start" in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked "Finish" in the diagram below).

How many possible unique paths are there?
Input: m = 3, n = 2

Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

1. Right -> Right -> Down

2. Right -> Down -> Right

3. Down -> Right -> Right

Example 2:
Input: m = 7, n = 3

Output: 28

Constraints:
1 <= m, n <= 100
It’s guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
"""



#print(uniquePaths(3,2))

########################################################################################################
#Leetcode 70 - Climbing Stairs
"""
Description:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2

Explanation:
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3

Explanation:
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


#print(climbStairs(3))
########################################################################################################
#Leetcode 121 - Best Time to Buy and Sell Stock
"""
Description:
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5

Explanation:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Not 7-1 = 6, as selling price needs to be larger than buying price.

Solution :
Example 2:
Input: [7,6,4,3,1]
Output: 0

Explanation:
In this case, no transaction is done, i.e. max profit = 0. 
"""


#print(bestTimeStock([7,1,5,3,6,4]))

########################################################################################################
#Leetcode 122 - Best Time to Buy and Sell Stock II
"""
Description:
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note:
You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [7,1,5,3,6,4]
Output: 7

Explanation:
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4

Explanation:
Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0

Explanation:
In this case, no transaction is done, i.e. max profit = 0.
"""


# print(bestTimeStock2([7,1,5,3,6,4]))
# print(bestTimeStock2([1,2,3,4,5]))

########################################################################################################
#Leetcode 198 - House Robber
"""
Description:
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, the only constraint ,

stopping you from robbing each of them is that adjacent houses have security system connected 
and it will automatically contact the police ,
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4

Explanation:
Rob house 1 (money = 1) and then rob house 3 (money = 3).

Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12

Explanation:
Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 400
"""



#print(houseRobber([1,2,3,1]))
#print(houseRobber([2,7,9,3,1]))

########################################################################################################
#Leetcode 213 - House Robber II
"""
Description:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle.

That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically contact the police

if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: [2,3,2]
Output: 3

Explanation:
You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),because they are adjacent houses.

Example 2:
Input: [1,2,3,1]
Output: 4

Explanation:
Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""


# print(houseRobber2([2,3,2]))
# print(houseRobber2([1,2,3,1]))
#print(houseRobber2([1,2,3]))

########################################################################################################
#Leetcode 309 - Best Time to Buy and Sell Stock with Cooldown
"""
Description:
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example :
Input: [1,2,3,0,2]

Output: 3

Explanation:
transactions = [buy, sell, cooldown, buy, sell]
"""


#print(bestTimeStockCooldown([1,2,3,0,2]))

########################################################################################################
#Leetcode 714 - Best Time to Buy and Sell Stock with Transaction Fee
"""
Description:
Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; 
and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. 
You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.

Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2

Output: 8

Explanation:
The maximum profit can be achieved by:

Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""


#print(bestTimeStockFee([1, 3, 2, 8, 4, 9],2))

########################################################################################################
#Leetcode 746 - Min Cost Climbing Stairs
"""
Description:
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
Example 1:
Input: cost = [10, 15, 20]
Output: 15

Explanation:
Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6

Explanation:
Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
"""


#print(mincostStairs([10, 15, 20]))
#print(mincostStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

########################################################################################################
#Leetcode 1480 - Running Sum of 1d Array
"""
Description:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]

Output: [1,3,6,10]

Explanation:
Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]

Output: [1,2,3,4,5]

Explanation:
Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 2:
Input: nums = [3,1,2,10,1]

Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000/li>
-10^6 <= nums[i] <= 10^6
"""


#print(sumArray([3,1,2,10,1]))

########################################################################################################
#Leetcode 1143(optional) - Longest Common Subsequence
"""
Description:
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:
Input: text1 = ""abcde"", text2 = "ace"

Output: 3

Explanation:
The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"

Output: 3

Explanation:
The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"

Output: 0

Explanation:
There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length <= 1000
1 <= text2.length <= 1000
The input strings consist of lowercase English characters only.
"""



#print(maxSubString("abcde", "ace"))
#print(maxSubString("abc", "abc"))

########################################################################################################
#Leetcode 583(optional) - Delete Operation for Two Strings
"""
Description:
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, 
where in each step you can delete one character in either string.

Note:
The length of given words won’t exceed 500.
Characters in given words can only be lower-case letters.
Example 1:
Input: "sea", "eat"

Output: 2

Explanation:
You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: nums = word1 = "leetcode", word2 = "etco"

Output: 4

"""


#print(deleteOpStrings("leetcode","etco"))
