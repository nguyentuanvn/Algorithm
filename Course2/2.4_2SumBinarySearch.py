"""
Coursera Algorithm Programming Assignemnt 2.4:
Implement 2Sum problem using modified binary search
@author: Tuan M. Nguyen
"""

from collections import defaultdict

def merge(array,first,last):
    MAX = 100000000000
    mid = int((last+first)/2)
    lArray = [MAX]*(mid-first+2)
    rArray = [MAX]*(last-mid+1)
    for indexL in range(0,mid-first+1):
        lArray[indexL] = array[first+indexL]
    for indexR in range(0,last-mid):
        rArray[indexR] = array[mid+indexR+1]    
    indexL = 0
    indexR = 0
    for index in range(first,last+1):
        if lArray[indexL] < rArray[indexR]:
            array[index] = lArray[indexL]
            indexL += 1
        else:
            array[index] = rArray[indexR]
            indexR += 1  

def mergeSort(array,first,last):
    mid = int((last+first)/2)
    if last-1 > first:
        mergeSort(array,first,mid)
        mergeSort(array,mid+1,last)
    merge(array,first,last)

def binarySearch(array,x,first,last):
    if (last > first):
        mid = int((first+last)/2)
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            return binarySearch(array,x,mid+1,last)
        else:  
            return binarySearch(array,x,first,mid-1)  
    else:
        return last

def findElement(bucket,element):
    try:
        return bucket.index(element)
    except ValueError:
        return -1
    
def findRange(array,x,THash):
    numBucket = 1009
    count = 0
    yfirst = binarySearch(array,-10000-x,0,len(array)-1)
    ylast = binarySearch(array,10000-x,0,len(array)-1)
    for y in range(yfirst,ylast+1):
        if array[y] != x:
            t = x + array[y]
            if t > -10000 and t < 10000:
                bucket = t % numBucket
                if findElement(THash[bucket],t) == -1:
                    count += 1  
                    THash[bucket].append(t)
    return count

def main():
    file = open("2.4_2Sum.txt","r")
    THash = defaultdict(list)
    array = []
    line = file.readline()
    while line:
        array.append(int(line))
        line = file.readline()
    mergeSort(array,0,len(array)-1)
#    read all element into a list A then sort    
    count = 0
    for index in range(0,len(array)-1):
        count += findRange(array,array[index],THash)
#    for each element x, find a range [yfirst,ylast] in which y satisfies 
#    -10000 < x + A[y] = t < 10000. Each t is inserted in to hash table THash
#    Add up the number of t in each iteration
    print(count)
#    expected answer: 427

if __name__ == "__main__":
    main()