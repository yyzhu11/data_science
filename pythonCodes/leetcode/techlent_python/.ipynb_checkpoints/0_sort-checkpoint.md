<font size=8> Chapter 0: Sort </font>

```
from functools import cmp_to_key

def compare():

users.sort(key=cmp_to_key(compare))
users.sort(key=lambda x: x[1]) 

sorted(users, key=lambda user: user['age'])
sorted(words, key=len, reverse=True)

```

## Leetcode 1460. Make Two Arrays Equal by Reversing Subarrays

You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

- Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
- Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
- Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.


```python
def twoArrayEqual(target, arr):
    return sorted(target) == sorted(arr)
```


```python
target = [1,2,3,4]
arr = [2,4,1,3]
twoArrayEqual(target, arr)
```




    True




```python
target = [7]
arr = [7]
twoArrayEqual(target, arr)
```




    True




```python
target = [3,7,9]
arr = [3,7,11]
twoArrayEqual(target, arr)
```




    False



# Leetcode 853. Car Fleet (Medium)

There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

You are given two integer arrays position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

A car fleet is a single car or a group of cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

Return the number of car fleets that will arrive at the destination.

- Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

Output: 3

Explanation:

The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

- Example 2:

Input: target = 10, position = [3], speed = [3]

Output: 1

Explanation:

There is only one car, hence there is only one fleet.

- Example 3:

Input: target = 100, position = [0,2,4], speed = [4,2,1]

Output: 1

Explanation:

The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.


```python

```


```python

```


```python

```


```python

```


```python

```


```python
def carFleet(target, position, speed):
    sorted_indices = sorted(range(len(position)), key=lambda i: position[i])
    pre = 0
    fleet = 0
    for index in sorted_indices[::-1]:
        time = (target - position[index]) / speed[index]
        if time > pre:
            fleet += 1
            pre = time
    return fleet
```


```python
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
carFleet(target, position, speed)
```




    3




```python
target = 10
position = [3]
speed = [3]
carFleet(target, position, speed)
```




    1




```python
target = 100
position = [0,2,4]
speed = [4,2,1]
carFleet(target, position, speed)
```




    1




```python

```

# Leetcode 973. K Closest Points to Origin (Medium)

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

- Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]

Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

- Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


```python

```


```python

```


```python

```


```python
def kClosestPoints(points, k):
    points.sort(key= lambda point: point[0]*point[0] + point[1]*point[1])
    return points[:k]
```


```python
points = [[1,3],[-2,2]]
k = 1
kClosestPoints(points, k)
```




    [[-2, 2]]




```python
points = [[3,3],[5,-1],[-2,4]]
k = 2
kClosestPoints(points, k)
```




    [[3, 3], [-2, 4]]



# Leetcode 1030. Matrix Cells in Distance Order

You are given four integers row, cols, rCenter, and cCenter. There is a rows x cols matrix and you are on the cell with the coordinates (rCenter, cCenter).

Return the coordinates of all cells in the matrix, sorted by their distance from (rCenter, cCenter) from the smallest distance to the largest distance. You may return the answer in any order that satisfies this condition.

The distance between two cells (r1, c1) and (r2, c2) is |r1 - r2| + |c1 - c2|.

- Example 1:

Input: rows = 1, cols = 2, rCenter = 0, cCenter = 0
Output: [[0,0],[0,1]]

Explanation: The distances from (0, 0) to other cells are: [0,1]
- Example 2:

Input: rows = 2, cols = 2, rCenter = 0, cCenter = 1
Output: [[0,1],[0,0],[1,1],[1,0]]

Explanation: The distances from (0, 1) to other cells are: [0,1,1,2]
The answer [[0,1],[1,1],[0,0],[1,0]] would also be accepted as correct.
- Example 3:

Input: rows = 2, cols = 3, rCenter = 1, cCenter = 2
Output: [[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]

Explanation: The distances from (1, 2) to other cells are: [0,1,1,2,2,3]
There are other answers that would also be accepted as correct, such as [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]].


```python
def matrixCellDistance(rows, cols, rCenter, cCenter):
    result = []
    for i in range(rows):
        for j in range(cols):
            result.append([i,j])
    result.sort(key=lambda x: abs(x[0]-rCenter)+abs(x[1]-cCenter))
    return result
```


```python
rows = 2
cols = 2
rCenter = 0
cCenter = 1
matrixCellDistance(rows, cols, rCenter, cCenter)
```




    [[0, 1], [0, 0], [1, 1], [1, 0]]



# Leetcode 274. H-Index (Medium)

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

- Example 1:

Input: citations = [3,0,6,1,5]
Output: 3

Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
- Example 2:

Input: citations = [1,3,1]
Output: 1


```python
def hIndex(citations):
    citations.sort(reverse=True)
    hindex = 0
    for i in range(len(citations)):
        hindex = max(hindex, min(citations[i], i+1))
    return hindex
```


```python
citations = [3,0,6,1,5]
hIndex(citations)
```




    3




```python
citations = [1,3,1]
hIndex(citations)
```




    1




```python
citations = [0,0,2]
hIndex(citations)
```




    1




```python
def hIndex(citations):
    citations.sort(reverse=True)
      
    for h in range(len(citations), 0, -1):
        print(h, citations[h - 1])
        if citations[h - 1] >= h:
            return h
      
        # If no valid h-index found, return 0
    return 0
```


```python
citations = [0,0,2]
hIndex(citations)
```

    3 0
    2 0
    1 2
    




    1




```python

```

# Leetcode 179. Largest Number (Medium)

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

- Example 1:

Input: nums = [10,2]
Output: "210"

- Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


```python

```


```python

```


```python

```


```python
from functools import cmp_to_key
def largestNumber(nums):
    # a, b = char
    def compare(a, b):
        if (a + b) < (b+a):
            return 1
        else:
            return -1
    nums_str = [str(num) for num in nums]
    nums_str.sort(key=cmp_to_key(compare))
    print(nums_str)
    if nums[0]=='0':
        return '0'
    return ''.join(nums_str)
```


```python
nums = [10,2]
largestNumber(nums)
```

    ['2', '10']
    




    '210'




```python
nums = [3,30,34,5,9]
largestNumber(nums)
```




    '9534330'




```python

```

# Leetcode 1054. Distant Barcodes (Medium)

In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

- Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]

- Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]


```python

```


```python

```


```python
def distantBarcodes(barcodes):
    counter = Counter(barcodes)
    barcodes.sort(key=lambda barcode: (-counter[barcode], barcode))
    n = len(barcodes)
    result = [0] * n
    # even positions
    result[::2] = barcodes[:(n+1)//2]
    # odd position
    result[1::2] = barcodes[(n+1)//2:]
    return result
```


```python
barcodes = [1,1,1,2,2,2]
distantBarcodes(barcodes)
```




    [1, 2, 1, 2, 1, 2]




```python
barcodes = [1,1,1,1,2,2,3,3]
distantBarcodes(barcodes)
```




    [1, 2, 1, 2, 1, 3, 1, 3]



# Leetcode 1057. Campus Bikes (Medium)
On a campus represented as a 2D grid, there are N workers and M  bikes, with N <= M. Each worker and  bike is a 2D coordinate on this grid. Bikes

Our goal is to assign a bike to each worker. Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between each other, and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the same shortest Manhattan distance, we choose the pair with the smallest worker index; if there are multiple ways to do that, we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.

- Example 1:

![image.png](0_sort_files/b422a6bf-1731-44ab-a6a0-77468fa6b15a.png)

Input: workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
Output: [1,0]

Explanation: 
Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].

- Example 2:

![image.png](0_sort_files/83a72c9b-0cb6-474a-8a5b-3c0206c7637f.png)

Input: workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
Output: [0,2,1]

Explanation: 
Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is assigned to Bik


```python
from itertools import product
def assignCampusBikes(workers, bikes):
    num_workers = len(workers)
    num_bikes = len(bikes)
    distance_pairs = []
    for worker_idx, bike_idx in product(range(num_workers), range(num_bikes)):
        distance = abs(workers[worker_idx][0] - bikes[bike_idx][0]) + abs(workers[worker_idx][1] - bikes[bike_idx][1])
        distance_pairs.append((distance, worker_idx, bike_idx))
    distance_pairs.sort()
    result=[0]*num_workers
    worker_assigned = [False]*num_workers
    bike_assigned = [False]*num_bikes

    for distance, worker_idx, bike_idx in distance_pairs:
        if not worker_assigned[worker_idx] and not bike_assigned[bike_idx]:
            result[worker_idx] = bike_idx
            worker_assigned[worker_idx] = True
            bike_assigned[bike_idx] = True
    return result
```


```python
workers = [[0,0],[2,1]]
bikes = [[1,2],[3,3]]
assignCampusBikes(workers, bikes)
```




    [1, 0]




```python
workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
assignCampusBikes(workers, bikes)
```




    [0, 2, 1]



# Bubble sort 

- Start at the beginning of the list.
- Compare the first element with the second element.
- Swap them if the first element is greater than the second.
- Move to the next pair of adjacent elements (second and third, third and fourth, and so on) and repeat the comparison and swap process.
- Complete a pass through the entire array. After this, the largest element will be in its correct final position at the end of the list.
- Repeat the entire process for the remaining unsorted portion of the list. The number of elements to check decreases by one in each subsequent pass.
- Stop when a full pass through the list occurs without any swaps, which means the list is sorted.

nlist = [7, 3, 5, 1, 9, 4]


```python
def bubbleSort(nums):
    n = len(nums)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums
```


```python

```


```python

```


```python

```


```python
def bubbleSort(nlist):
    n = len(nlist)    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist
```


```python
bubbleSort([7, 3, 5, 1, 9, 4])
```




    [1, 3, 4, 5, 7, 9]




```python

```

# Selection sort

-  first smallest number in the array starting 0
put in array[0]

-  find the smallest number in the array starting 1
put in array[1]


```python
def selectionSort(nums):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[min_index]:
                min_num = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums
    
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```


```python
def selectionSort(nlist):
    n = len(nlist)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nlist[j] < nlist[min_index]:
                min_index = j
        nlist[i], nlist[min_index] = nlist[min_index], nlist[i]
    return nlist
```


```python
selectionSort([7, 3, 5, 1, 9, 4])
```




    [1, 3, 4, 5, 7, 9]




```python

```

# Insertion sort

- Start with the second element of the array (index 1), as the first element (index 0) is considered a sorted sub-list of one element.
- Pick the current element from the unsorted part and store it as a key.
- Compare the key with the elements in the sorted part, moving backward from the element just before the key.
- Shift any elements in the sorted part that are greater than the key one position to the right to create space.
- Insert the key into the position where the shifting stops (i.e., immediately after an element smaller than or equal to the key).
- Repeat the process (steps 2-5) for all remaining elements in the unsorted portion until the entire array is sorted

Animation: https://yongdanielliang.github.io/animation/web/InsertionSortNew.html


```python
def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        for j in range(0,i):
            if key < nums[j]:
                nums[j+1:i+1] = nums[j:i]
                nums[j] = key
                break
    return nums        
```


```python

```


```python

```


```python

```


```python

```


```python

```


```python
def insertionSort(nlist):
    n = len(nlist)
    for i in range(1, n):
        key = nlist[i]
        for j in range(0,i):
            if key < nlist[j]:            
                nlist[j+1:i+1] = nlist[j:i]
                nlist[j] = key
                break
    return nlist
```


```python
def insertionSort2(nlist):
    n = len(nlist)
    for i in range(1, n):
        key = nlist[i]
        j = i -1
        while j >= 0 and key < nlist[j]:
            nlist[j+1] = nlist[j]
            j -= 1
        nlist[j+1] = key
    return nlist
```


```python
insertionSort2([7, 3, 5, 1, 9, 4])
```




    [1, 3, 4, 5, 7, 9]




```python

```

## Leetcode 147. Insertion Sort List (Medium)

Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

![image.png](0_sort_files/f932c122-dfe0-4bf6-92c7-a62bbd4a8ae4.png)

- Example 1:

![image.png](0_sort_files/c027848f-268a-4dfc-a400-69ebcd0d9dea.png)

Input: head = [4,2,1,3]
Output: [1,2,3,4]

- Example 2:

![image.png](0_sort_files/922dc6c7-c446-43d5-bde9-7a629d1320b4.png)

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]


```python
import numpy as np
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def createLinkedList(nlist):
    if not nlist:
        return None
    Head = ListNode(nlist[0])
    i = 1
    prevNode = Head
    while i < len(nlist):
        curNode = ListNode(nlist[i])
        prevNode.next= curNode
        prevNode = curNode
        i +=1
    return Head
def printLinkedList(head):
    result=[]
    nextNode = head    
    while nextNode:
        result.append(nextNode.val)
        nextNode = nextNode.next
    return result
```


```python
def insertSortList(head):
    if head is None or head.next is None:
        return head
    dummy = ListNode(-np.inf)
    dummy.next = head
    prev = head
    curr = head.next
    while curr:
        if prev.val <= curr.val:
            prev = curr
            curr = curr.next
            continue
        insert_pos = dummy
        while insert_pos.next.val < curr.val:
            insert_pos = insert_pos.next

        #delete the node curr
        next_node = curr.next
        prev.next = next_node
        #insert curr into insert.pos
        curr.next = insert_pos.next
        insert_pos.next = curr

        curr = next_node
    return dummy.next
```


```python
head = createLinkedList([4,2,1,3])
new_head = insertSortList(head)
printLinkedList(new_head)
```




    [1, 2, 3, 4]




```python
head = createLinkedList([-1,5,3,4,0])
new_head = insertSortList(head)
printLinkedList(new_head)
```




    [-1, 0, 3, 4, 5]




```python

```


```python

```

# Merge sort

The process involves two main phases: dividing and merging. 

- Divide: The algorithm starts by repeatedly splitting the unsorted list into two halves until each sublist has only a single element. A list with one element is considered sorted by definition.

- Merge (Conquer and Combine): The single-element sublists are then merged in a sorted manner. In this phase, adjacent pairs of sublists are compared element by element, and the smaller element is placed into a new combined, sorted sublist. This process continues, merging larger and larger sorted sublists until a single, fully sorted list is produced.


```python
def mergeList(left, right):
    result = []
    m = len(left)
    n = len(right)
    while i < m and j < n:
        if left[i] < right[i]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < m:
        result.extend(left[i:])
    if j < n:
        result.extend(left[j:])

def mergeSort(nums):
    n = len(nums)
```


```python

```


```python

```


```python

```


```python

```


```python
def mergeList(left, right):
    i=j=0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```


```python
def mergeSort(nlist):
    n = len(nlist)
    if n <= 1:
        return nlist
    mid = n // 2
    left = mergeSort(nlist[:mid])
    right = mergeSort(nlist[mid:])
    
    return mergeList(left, right)
```


```python
mergeSort([7, 3, 5, 1, 9, 4])
```




    [1, 3, 4, 5, 7, 9]




```python

```

## Leetcode 88. Merge Sorted Array 
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

- Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

- Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

- Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


```python
def mergeList2(left,m, right,n):
    i=j=0
    result = []
    while i < m and j < n:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < m:
        result.extend(left[i:])
    if j < n:
        result.extend(right[j:])
    return result
```


```python
mergeList2([1,2,3,0,0,0],3, [2,5,6],3 )
```




    [1, 2, 2, 3, 5, 6]




```python
mergeList2([1],1, [],0 )
```




    [1]




```python
mergeList2([0],0, [1],1 )
```




    [1]




```python

```

# Quick sort

QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. .

There are mainly three steps in the algorithm:

- Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
- Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right.
- Recursively Call: Recursively apply the same process to the two partitioned sub-arrays.
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted

Animation: https://yongdanielliang.github.io/animation/web/QuickSortNew.html


```python
# use the first one as pivot
def quickSort(nlist):
    n = len(nlist)
    if n <= 1:
        return nlist
    right = []
    left = []
    for i in range(1, n):
        pivot = nlist[0]
        if nlist[i] > pivot:
            right.append(nlist[i])
        else:
            left.append(nlist[i])
    return quickSort(left) + [pivot] + quickSort(right)
```


```python
quickSort([7, 3, 5, 1, 9, 4])
```




    [1, 3, 4, 5, 7, 9]




```python

```


```python
 
```


```python
def quickSelection(nums, l, r):
    #pivot l
    pivot = nums[l]
    i, j = l + 1, r
    while True:
        while i < r and nums[i] <= pivot:
            i += 1
        while l < j and nums[j] >= pivot:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]

    nums[l], nums[j] = nums[j], nums[l]
    return j


def quickSort(nums, l, r):
    if l < r:
        # Find the pivot index
        pivot_index = quickSelection(nums, l, r)        
        # Recursively sort elements before and after the pivot
        quickSort(nums, l, pivot_index - 1)
        quickSort(nums, pivot_index + 1, r)

    return nums
```


```python
nums = [7, 3, 5, 1, 9, 4]
quickSort(nums, 0, len(nums)-1)
```




    [1, 3, 4, 5, 7, 9]




```python
nums = [5, 2, 8, 1, 6]
quickSort(nums, 0, len(nums)-1)
```




    [1, 2, 5, 6, 8]



## Leetcode 215. Kth Largest Element in an Array (Medium)

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
- Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
- Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


```python
def findKthLargest(nums, k):
    l = 0 
    r = len(nums) - 1
    target = len(nums) - k
    
    while l < r:
    	mid = quickSelection(nums, l, r);
    	if mid == target:
    		return nums[mid]
    
    	if mid < target:
    		l = mid + 1
    	else:
    		r = mid - 1

    return nums[l]
```


```python
nums = [3,2,1,5,6,4]
k = 2
findKthLargest(nums, k)
```




    5




```python
nums = [3,2,3,1,2,4,5,5,6]
k = 4
findKthLargest(nums, k)
```




    4



## Leetcode 912. Sort an Array (Medium)

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

- Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
- Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessarily unique.


```python

```

# Count sort

Counting Sort is a non-comparison-based sorting algorithm that sorts elements by counting the occurrences of each unique value. Unlike algorithms like QuickSort or Merge Sort that compare numbers against each other, Counting Sort uses the values themselves as array indices to map out their correct positions

- Find the Maximum Value
- Count the Frequencies
- Compute Prefix Sums (Cumulative Counts)
- Build the Output Array


```python
def countSort(nums):
    max_val = max(nums)
    min_val = min(nums)
    range_nums = max_val - min_val + 1
    count_nums = [0] * range_nums
    result = [0] * len(nums)

    for num in nums:
        count_nums[num - min_val] += 1
    
    for i in range(1, len(count_nums)):
        count_nums[i] += count_nums[i-1]

    for num in reversed(nums):
        result[count_nums[num - min_val] -1] = num
        count_nums[num - min_val] -= 1
        
    return result
```


```python
unsorted_list = [4, -2, 2, 8, -2, 3, 1]
countSort(unsorted_list)
```




    [-2, -2, 1, 2, 3, 4, 8]




```python

```


```python
countSort([7, 3, 5, 1, 9, 4])
```

# Bucket sort

桶排序的意思是为每个值设立一个桶，桶内记录这个值出现的次数（或其他属性）
然后对桶进行排序


```python
from collections import Counter, defaultdict
def bucketSort(nums):
    n = len(nums)
    if n <= 1:
        return nums   
        
    counter = Counter(nums)
    maxCount = max(counter.values())
    buckets = defaultdict(list)
    for key, value in counter.items():        
        buckets[value].append(key)

    sorted_nums = []
    for i in range(maxCount, 0, -1):
        while i in buckets and buckets[i]:
            buckets[i].sort()
            sorted_nums += [buckets[i].pop(0)]*i
        
    return sorted_nums
```


```python
nums = [7, 3, 5, 1, 9, 4]
bucketSort(nums)
```




    [1, 3, 4, 5, 7, 9]



## Leetcode 347. Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

- Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

- Example 2:

Input: nums = [1], k = 1

Output: [1]

- Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]


```python
from collections import Counter, defaultdict
def topK(nums, k):
    counter = Counter(nums)
    maxCount = max(counter.values())
    buckets = defaultdict(list)
    for key, val in counter.items():
        buckets[val].append(key)

    result = []
    for i in range(maxCount, 0, -1):
        while i in buckets and buckets[i]:
            result.append(buckets[i].pop(0))
            if len(result) == k:
                return result
    
    return result
```


```python
nums = [1,1,1,2,2,3]
k = 2
topK(nums, k)
```




    [1, 2]




```python
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
topK(nums, k)
```




    [1, 2]



## Leetcode 451. Sort Characters By Frequency (Medium)

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

- Example 1:

Input: s = "tree"
Output: "eert"

Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
- Example 2:

Input: s = "cccaaa"
Output: "aaaccc"

Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
- Example 3:

Input: s = "Aabb"
Output: "bbAa"

Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


```python
def sortCharByFreq(s):
    counter = Counter(s)
    maxCount = max(counter.values())
    buckets = defaultdict(list)
    for key, val in counter.items():
        buckets[val].append(key)

    result = []
    for i in range(maxCount, 0, -1):
        while i in buckets and buckets[i]:
            result += [buckets[i].pop(0)]*i
            #print(result)
    
    return ''.join(result)
```


```python
s = "tree"
sortCharByFreq(s)
```

    ['e', 'e']
    ['e', 'e', 't']
    ['e', 'e', 't', 'r']
    




    'eetr'




```python

```


```python

```


```python
s = "Aabb"
sortCharByFreq(s)
```

# Heap Sort


```python

```

## Leetocde 1086. High Five

Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.

- Example 1:

Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]

Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.

- Example 2:

Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]

Output: [[1,100],[7,100]]


```python
from collections import defaultdict
from heapq import nlargest

def highFive(items):
    buckets = defaultdict(list)
    max_student_id = 0
    for item in items:
        buckets[item[0]].append(item[1])
        max_student_id = max(max_student_id, item[0])
    result = []
    for i in range(1, max_student_id+1):
        if buckets[i]:
            top_5_average = sum(nlargest(5, buckets[i]))//5
            result.append([i, top_5_average])
    return result
```


```python
items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
highFive(items)
```




    [[1, 87], [2, 88]]




```python
items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
highFive(items)
```




    [[1, 100], [7, 100]]



# Leetcode 939. Minimum Area Rectangle (Medium)

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

rectangle: (x', y1), (x', y2), (x, y1), and (x, y2)

area = (x - x') × (y2 - y1)

- Example 1:

![image.png](0_sort_files/243935cf-5ffe-489e-91bc-f7a5db7d5fd8.png)

Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

- Example 2:

![image.png](0_sort_files/f9af1929-884f-42a9-9879-1ba92e099fd7.png)

Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


```python
from collections import defaultdict
import numpy as np
def miniAreaRectangle(points):
    x_to_y = defaultdict(list)
    for x, y in points:
        x_to_y[x].append(y)

    y_pair_to_last_x = {}
    min_area = np.inf
    for current_x in sorted(x_to_y):
        ylist = x_to_y[current_x]
        ylist.sort()
        for i, y1 in enumerate(ylist):
            for y2 in ylist[i+1:]:
                if (y1, y2) in y_pair_to_last_x:
                    x1 = y_pair_to_last_x[(y1, y2)]
                    area = (current_x - x1) * (y2-y1)
                    min_area = min(min_area, area)
                y_pair_to_last_x[(y1, y2)] = current_x
    return min_area
```


```python
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
miniAreaRectangle(points)
```




    4




```python
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
miniAreaRectangle(points)
```




    2



# Leetcode 963. Minimum Area Rectangle II (Medium)

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].
Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.
Answers within 10-5 of the actual answer will be accepted.

- Example 1:

![image.png](0_sort_files/5a778f5a-5d53-4140-b087-00b5ae7ea610.png)

Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000

Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.

- Example 2:

![image.png](0_sort_files/d2e376ec-fcf1-442f-97f4-525990da907a.png)

Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000

Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.

- Example 3:

![image.png](0_sort_files/8e03628c-fbb3-438e-acf4-ac13a16ba25b.png)

Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0

Explanation: There is no possible rectangle to form from these points.

- p1, p2, p3
- v21[0] * v31[0] + v21[1] * v31[1] == 0
- P4 = P2 + P3 - P1


```python
import numpy as np
from itertools import permutations
def miniAreaRectangleII(points):
    points = set(map(tuple, points))
    num_points = len(points)
    if num_points <4:
        return 0
    ans = float('inf')
    for p1, p2, p3 in permutations(points, 3):
        v21 = ((p2[0] - p1[0]), (p2[1] - p1[1]))
        v31 = ((p3[0] - p1[0]), (p3[1] - p1[1]))
        if v21[0]*v31[0] + v21[1]*v31[1] == 0:
        #if ((p2[0] - p1[0]) * (p3[0] - p1[0]) +(p2[1] - p1[1]) * (p3[1] - p1[1])) == 0:
            p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])
            if p4 in points:
                area = math.sqrt(v21[0] ** 2 + v21[1] ** 2) * math.sqrt(v31[0] ** 2 + v31[1] ** 2)                
                ans = min(ans, area)
                
    if ans < float('inf'):
        return ans
    return 0
```


```python
points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
miniAreaRectangleII(points)
```




    1.0




```python
points = [[1,2],[2,1],[1,0],[0,1]]
miniAreaRectangleII(points)
```




    2.0000000000000004




```python
points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
miniAreaRectangleII(points)
```




    1.0




```python
points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
miniAreaRectangleII(points)
```




    0



# Leetcode 280. Wiggle Sort (Medium)

Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

You may assume the input array always has a valid answer.

- Example 1:

Input: nums = [3,5,2,1,6,4]

Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.


- Example 2:

Input: nums = [6,6,5,6,3,8]

Output: [6,6,5,6,3,8]


```python
# odd >= even,
def wiggleSort(nums):
    n = len(nums)
    for i in range(1, n):
        if (i%2 == 0 and nums[i-1] < nums[i]) or (i%2 == 1 and nums[i-1] > nums[i]):
            nums[i], nums[i-1] = nums[i-1], nums[i]
    return nums
```


```python
nums = [3,5,2,1,6,4]
wiggleSort(nums)
```




    [3, 5, 1, 6, 2, 4]




```python
nums = [6,6,5,6,3,8]
wiggleSort(nums)
```




    [6, 6, 5, 6, 3, 8]



# Leetcode 324. Wiggle Sort II (Medium)

Given an integer array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
You may assume the input array always has a valid answer.

- Example 1:

Input: nums = [1,5,1,1,6,4]
Output: [1,6,1,5,1,4]
Explanation: [1,4,1,5,1,6] is also accepted.

- Example 2:

Input: nums = [1,3,2,2,3,1]
Output: [2,3,1,3,1,2]


```python
def wiggleSortII(nums):
    sorted_nums = sorted(nums)
    n = len(nums)
    left = (n-1)//2
    right = n-1
    for i in range(n):
        if i%2 == 0:
            nums[i] = sorted_nums[left]
            left -= 1
        else:
            nums[i] = sorted_nums[right]
            right -= 1
    return nums
```


```python
nums = [1,5,1,1,6,4]
wiggleSortII(nums)
```




    [1, 6, 1, 5, 1, 4]




```python
nums = [1,3,2,2,3,1]
wiggleSortII(nums)
```




    [2, 3, 1, 3, 1, 2]



# Leetcode 969. Pancake Sorting (Medium)

Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.

- Example 1:

Input: arr = [3,2,4,1]
Output: [4,2,4,3]

Explanation: 
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: arr = [3, 2, 4, 1]
- After 1st flip (k = 4): arr = [1, 4, 2, 3]
- After 2nd flip (k = 2): arr = [4, 1, 2, 3]
- After 3rd flip (k = 4): arr = [3, 2, 1, 4]
- After 4th flip (k = 3): arr = [1, 2, 3, 4], which is sorted.
- Example 2:

Input: arr = [1,2,3]
Output: []

Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
 


```python
def pancakeSorting(arr):
    def reverse(nums, end_index):
        start_index=0
        while start_index < end_index:
            nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
            start_index += 1
            end_index -= 1
    
    arr_len = len(arr)
    result = []
    for i in range(arr_len-1, 0, -1):
        target_val = i+1
        target_pos = i
        while target_pos > 0 and arr[target_pos] != target_val:
            target_pos -= 1
        if target_pos < i:
            if target_pos > 0:
                result.append(target_pos+1)
                reverse(arr, target_pos)
            result.append(i+1)
            reverse(arr, i)
    return result
    
```


```python
arr = [3,2,4,1]
pancakeSorting(arr)
```




    [3, 4, 2, 3, 2]




```python
arr = [1,2,3]
pancakeSorting(arr)
```




    []



# Leetcode 41. First Missing Positive (Hard)

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

- Example 1:

Input: nums = [1,2,0]
Output: 3

Explanation: The numbers in the range [1,2] are all in the array.

- Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Explanation: 1 is in the array but 2 is missing.

- Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

Explanation: The smallest positive integer 1 is missing.


```python

```

# Leetcode 296. Best Meeting Point (Hard)
A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.


- Example:

Input:
```
1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
```
Output: 6

Explanation: Given three people living at (0,0), (0,4), and (2,2):
             The point (0,2) is an ideal meeting point, as the total travel distance
             of 2+2+2=6 is minimal. So return 6.


```python

```

# Leetcode 327. Count of Range Sum (Hard)

Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

- Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
- Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1


```python

```

# Leetcode 493. Reverse Pairs (Hard)

Given an integer array nums, return the number of reverse pairs in the array.
A reverse pair is a pair (i, j) where:

0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
 
- Example 1:

Input: nums = [1,3,2,3,1]
Output: 2

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1
- Example 2:

Input: nums = [2,4,3,5,1]
Output: 3

Explanation: The reverse pairs are:
(1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
(2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
(3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1


```python

```
