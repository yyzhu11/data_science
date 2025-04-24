# sort algorithm
#1. Bubble sort
# nlist = [7, 3, 5, 1, 9, 4]
#########################################################################################
def bubbleSort(nlist):
    n = len(nlist)
    for i in range(1,n):
        for j in range(0,n-i):
            if nlist[j] > nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
    return nlist



#print(bubbleSort([7, 3, 5, 1, 9, 4]))
#########################################################################################
'''
selection sort
1. first smallest number in the array starting 0
put in array[0]

2. find the smallest number in the array starting 1
put in array[1]
....

'''

def selectionSort(nlist):
    n = len(nlist)
    for i in range(n):
        minNum = nlist[i]
        minIndex = i
        for j in range(i+1, n):
            if nlist[j] < minNum:
                minIndex = j
                minNum = nlist[j]
        nlist[i], nlist[minIndex] = nlist[minIndex], nlist[i]

    return nlist

#print(selectionSort([7, 3, 5, 1, 9, 4]))





#########################################################################################
#insertion sort
'''

poker, 

'''

def insertionSort(nlist):
    n = len(nlist)

    for right in range(1,n):
        target = nlist[right]
        for left in range(0, right):
            if target < nlist[left]:
                nlist[left+1:right+1] = nlist[left:right]
                nlist[left] = target
                break
    return nlist


#print(insertionSort([7, 3, 5, 1, 9, 4]))


#########################################################################################
#merge sort

'''
divide into two array, until len = 1, then merge them one level by one level

'''

def mergeSort(nlist):
    n = len(nlist)
    if n <= 1:
        return nlist
    mid = n //2
    return mergeList(mergeSort(nlist[0:mid]), mergeSort(nlist[mid:]))


def mergeList(left, right):
    mlist = []
    while left and right:
        if left[0] < right[0]:
            mlist.append(left.pop(0))
        else:
            mlist.append(right.pop(0))
    if left:
        mlist.extend(left)
    if right:
        mlist.extend(right)


print(mergeSort([7, 3, 5, 1, 9, 4]))

#########################################################################################
#quick sort

def quickSort(nlist):

    n = len(nlist)
    if n <= 1:
        return nlist
    left = []
    right = []
    for i in range(1,n):
        if nlist[i] > nlist[0]:
            right.append(nlist[i])
        else:
            left.append(nlist[i])
    return quickSort(left) + [nlist[0]] + quickSort(right)


print(quickSort([7, 3, 5, 1, 9, 4]))


#########################################################################################
#count sort
'''
[7, 3, 5, 1, 9, 4]
dictionary
0 1 2 3 4 5 6 7 8 9
[0 1 0 1 1 1 0 1 0 1]
accumalate it
[0 1 1 2 3 4 4 5 5 6]
left shift 
[0 0 1 1 2 3 4 4 5 5]

'''
def countSort(nlist):
    n = len(nlist)
    rlist = []
    count = dict()
    for i in nlist:
        count[i] = count.get(i,0) + 1
    # add the count
    i = 0
    while n > 0:
        if count.get(i,0) == 0:
            i += 1
        else:
            rlist.append(i)
            count[i] -= 1
            n -= 1
    return rlist

#print(countSort([7, 3, 5, 1, 9, 4]))