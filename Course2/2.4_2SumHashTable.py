"""
Coursera Algorithm Programming Assignemnt 2.4:
Implement 2Sum problem using hash table solution
Very slow for O(n*m) operation with n is the number 
of elements, m is the range of sum t
@author: Tuan M. Nguyen
"""
from collections import defaultdict

def findElement(bucket,element):
    try:
        return bucket.index(element)
    except ValueError:
        return -1

def main():
    numBucket = 100003
    file = open("2.4_2Sum.txt","r")
    line_list = file.readlines()
    file.close
    A = defaultdict(list)
    count = 0
#    Insert elements into hash table
    for line in line_list:
        bucket = int(line) % numBucket
        if findElement(A[bucket],int(line)) == -1:
            A[bucket].append(int(line))
    for t in range (-10000,10001):
        for line in line_list:
            y = t - int(line)
            if y != int(line):
                if findElement(A[y % numBucket],y) != -1:
                    count += 1
                    break     
    print(count)
#    expected answer: 427

if __name__ == "__main__":
    main()