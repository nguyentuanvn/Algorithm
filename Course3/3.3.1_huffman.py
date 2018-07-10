"""
Coursera Algorithm Programming Assignemnt 3.3.1 and 3.3.2:
Maximum and minimum length of a codeword in Huffman Code
@author: Tuan M. Nguyen
"""

from heapq import heappush,heappop

def merge(S,rank,maxmin):
    a = heappop(S)
    b = heappop(S)
    curRank = max(rank[a],rank[b]) + 1 if maxmin == 1 else min(rank[a],rank[b]) + 1
    if len(S) == 0:
        return curRank
    else:
        heappush(S,a+b)
        rank[a+b] = curRank
        return merge(S,rank,maxmin)
        
def main():
    file = open("3.3.1_huffman.txt","r")
    num = int(next(file))
    S = []
    rank = {}
    for line in file:
        num = int(line)
        heappush(S,num)
        rank[num] = 0   
    file.close()
    S1 = S.copy()
    rank1 = rank.copy()

    print(merge(S,rank,1))
    print(merge(S1,rank1,0))
#    expected result: 19 9

if __name__ == "__main__":
    main()
    
    