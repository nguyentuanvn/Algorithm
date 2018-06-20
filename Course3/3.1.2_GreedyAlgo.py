"""
Coursera Algorithm Programming Assignemnt 3.1.1:
Compute sum of weighted completion time. Schedule jobs in decreasing order
of the ratio (weight/length).   
@author: Tuan M. Nguyen
"""

def merge(array,first,last):
    MIN = -10000
    mid = int((last+first)/2)
    lArray = []
    rArray = []
    for indexL in range(0,mid-first+1):
        lArray.append(array[first+indexL])
    lArray.append([0,0,MIN])
    for indexR in range(0,last-mid):
        rArray.append(array[mid+indexR+1])
    rArray.append([0,0,MIN])
    indexL = 0
    indexR = 0
    for index in range(first,last+1):
        if lArray[indexL][2] > rArray[indexR][2]:
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

def main():
    file = open("3.1.1_jobs.txt","r")
    array = []
    n = int(file.readline())
    for line in file:
        w,l = [int(x) for x in line.split()]
        array.append([w,l,w/l])
    file.close()
    mergeSort(array,0,n-1)
    c = 0
    sum = 0
    for index in range(0,n):
        c += array[index][1]
        sum += array[index][0]*c
    print(sum) 
#    expected result: 67311454237
if __name__ == "__main__":
    main()
    