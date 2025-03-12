#######################################################################################
#stack,definition


#######################################################################################
#Leetcode 1381-Design a Stack With Increment Operation
"""
Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Design a stack which supports the following operations.
Implement the CustomStack class:
CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements
in the stack or do nothing if the stack reached the maxSize.
void push(int x) Adds x to the top of the stack if the stack hasn’t reached the maxSize.
Example:
Input:

["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"] 
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]

Output:

[null,null,null,2,null,null,null,null,null,103,202,201,-1]
"""


# customStack = CustomStack(3);
# customStack.push(1);
# customStack.push(2);
# print(customStack.stack)
# print(customStack.pop( ))
# print(customStack.stack)
# customStack.push(2);
# customStack.push(3);
# customStack.push(4);
# print(customStack.stack)
# customStack.increment(5, 100);
# print(customStack.stack)
# customStack.increment(2, 100);
# print(customStack.stack)
# print(customStack.pop( ))
# print(customStack.pop( ))
# print(customStack.pop( ))
# print(customStack.pop( ))

########################################################################################################
#Queue definition


########################################################################################################
#Leetcode 1047- Remove All Adjacent Duplicates In String
"""
Description:
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.
We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed the answer is unique.

Note:
<= S.length <= 20000.
consists only of English lowercase letters.
Example:
Input:"abbaca"
Output:"ca"
"""


#print(removeAllAdj("abbaca"))

########################################################################################################
#Leetcode 20-Valid Parentheses

"""
Description:
Given a string containing just the characters "(", ")", "{", "}", "[" and "]", determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note:
That an empty string is also considered valid.

Example1:
Input: "( )" Output: true

Example2:
Input: "( ) [ ] { }" Output: true

Example3:
Input: "( ]" Output: false

Example4:
Input: "( [ ) ]" Output: false

Example5:
Input: "{ [ ] }" Output: true

"""


# print(validParentheses("()"))
# print(validParentheses("( ) [ ] { }"))
# print(validParentheses("([)]"))
# print(validParentheses("{ [ ] }"))
########################################################################################################
#Leetcode 155- Min Stack
"""
Description:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop( ) -- Removes the element on top of the stack.
top( ) -- Get the top element.
getMin( ) -- Retrieve the minimum element in the stack.
Example:
Input:

["MinStack","push","push","push","getMin","pop","top","getMin"]

[ [ ],[-2],[0],[-3],[ ],[ ],[ ],[ ] ]

Output:

[null,null,null,null,-3,null,0,-2]
"""



########################################################################################################
#Leetcode 225-Implement Stack using Queues
"""
Description:
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
"""


########################################################################################################
#Leetcode 232-Implement Queue using Stacks
"""
Description:
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Note:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""



########################################################################################################
#Leetcode 641-Design Circular Deque
"""
Description:
Design your implementation of the circular double-ended queue (deque).Your implementation should support following operations:

MyCircularDeque(k): Constructor, set the size of the deque to be k.
insertFront(): Adds an item at the front of Deque. Return true if the operation is successful.
insertLast(): Adds an item at the rear of Deque. Return true if the operation is successful.
deleteFront(): Deletes an item from the front of Deque. Return true if the operation is successful.
deleteLast(): Deletes an item from the rear of Deque. Return true if the operation is successful.
getFront(): Gets the front item from the Deque. If the deque is empty, return -1.
getRear(): Gets the last item from Deque. If the deque is empty, return -1.
isEmpty(): Checks whether Deque is empty or not.
isFull(): Checks whether Deque is full or not.

"""


########################################################################################################
#Leetcode 682- Baseball Game
"""
Description:
You’re now a baseball game point recorder.
Given a list of strings, each string can be one of the 4 following types:

Integer (one round’s score): Directly represents the number of points you get in this round.
"+" (one round’s score): Represents that the points you get in this round are the sum of the last two valid round’s points.
"D" (one round’s score): Represents that the points you get in this round are the doubled data of the last valid round’s points.
"C" (an operation, which isn’t a round’s score): Represents the last valid round’s points you get were invalid and should be removed.
Each round’s operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.

Note:
The size of the input list will be between 1 and 1000.
Every integer represented in the list will be between -30000 and 30000.
Example1:
Input: ["5","2","C","D","+"]
Output: 30

Explanation:

Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get 2 points. The sum is: 7.
Operation 1: The round 2’s data was invalid. The sum is: 5.
Round 3: You could get 10 points (the round 2’s data has been removed). The sum is: 15.
Round 4: You could get 5 + 10 = 15 points. The sum is: 30.

Example2:
Input: ["5","-2","4","C","D","9","+","+"]
Output: 27

Explanation:

Round 1: You could get 5 points. The sum is: 5.
Round 2: You could get -2 points. The sum is: 3.
Round 3: You could get 4 points. The sum is: 7.
Operation 1: The round 3’s data is invalid. The sum is: 3.
Round 4: You could get -4 points (the round 3’s data has been removed). The sum is: -1.
Round 5: You could get 9 points. The sum is: 8.
Round 6: You could get -4 + 9 = 5 points. The sum is 13.
Round 7: You could get 9 + 5 = 14 points. The sum is 27.

"""


#print(baseballGame(["5","2","C","D","+"]))
#print(baseballGame(["5","-2","4","C","D","9","+","+"]))

########################################################################################################
#Leetcode 844-Backspace String Compare
"""
Description:
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Note:
1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and "#" characters.
Example1:
Input: S = "ab#c", T = "ad#c"
Output: true

Explanation: Both S and T become "ac".

Example2:
Input: S = "ab##", T = "c#d#"
Output: true

Explanation: Both S and T become "".

Example3:
Input: S = "a##c", T = "#a#c"
Output: true

Explanation: Both S and T become "c".

Example4:
Input: S = "a#c", T = "b"
Output: false

Explanation: S becomes "c" while T becomes "b".

Follow up:
Can you solve it in O(N) time and O(1) space?
"""




# print(backspaceStringCompare("ab#c", "ad#c"))
# print(backspaceStringCompare("ab##", "c#d#"))
# print(backspaceStringCompare("a#c", "b"))

#def backspaceStringCompare2(str1, str2):
#    for s in str1:

########################################################################################################
#Leetcode 933-Number of Recent Calls

"""
Description:
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Note:
Each test case will have at most 10000 calls to ping.
Each test case will call ping with strictly increasing values of t.
Each call to ping will have 1 <= t <= 10^9.
Example:
Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]

Output: [null,1,2,3,3]
"""



# counter = RecentCounter()
# print(counter.ping(1))
# print(counter.ping(100))
# print(counter.ping(3001))
# print(counter.ping(3002))

########################################################################################################
#Leetcode 1441-Build an Array With Stack Operations

"""
Description:
Given an array target and an integer n. In each iteration, you will read a number from list = {1,2,3..., n}.
Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.
You are guaranteed that the answer is unique.

Example1:
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]

Explanation:

Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Example2:
Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]

Example3:
Input: target = [1,2], n = 4
Output: ["Push","Push"]

Explanation:

You only need to read the first 2 numbers and stop.

Example4:
Input: target = [2,3,4], n = 4
Output: ["Push","Pop","Push","Push","Push"]

Constraints:
1 <= target.length <= 100
1 <= target[i] <= 100
1 <= n <= 100
target is strictly increasing.

"""



# print(stackOperation([1,2,3],3))
# print(stackOperation([1,2],4))
# print(stackOperation([2,3,4],4))

########################################################################################################
#Leetcode 496 (optional)-Next Greater Element I
"""
Description:
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1’s elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
Example1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].

Output: [-1,3,-1]

Explanation:

For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
For number 1 in the first array, the next greater number for it in the second array is 3.
For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].

Output: [3,-1]
"""
"""
Explanation:

For number 2 in the first array, the next greater number for it in the second array is 3.
For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

"""



#print(nextGreaterElement([4,1,2],[1,3,4,2] ))
#print(nextGreaterElement([2,4],[1,2,3,4] ))
