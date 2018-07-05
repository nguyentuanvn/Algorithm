"""
Coursera Algorithm Programming Assignemnt 3.2.1:
Find max-spacing 4-clustering. Union by ranks implementation.
@author: Tuan M. Nguyen
"""

from heapq import heappush,heappop

def find(parent,ver):
    while parent[ver] != ver:
        ver = parent[ver]
    return ver

def union(rank,parent,ver1,ver2):
    s1 = find(parent,ver1)
    s2 = find(parent,ver2)
    if rank[s1] < rank[s2]:
        parent[s1] = s2
    elif rank[s1] == rank[s2]:
        parent[s1] = s2
        rank[s2] += 1
    else:
        parent[s2] = s1    
    
def clustering(E,rank,parent,numver):
    while numver > 3:
        cost,ver,dest = heappop(E)
        if find(parent,ver) != find(parent,dest):
            numver -= 1
            union(rank,parent,ver,dest)
            if numver == 3:
                print(cost)
    
def main():
    file = open("3.2_clustering1.txt","r")
    numver = int(next(file))
    parent = {ver:ver for ver in range(1,numver+1)}
    rank = {ver:0 for ver in range(1,numver+1)}
    E = []
    for line in file:
        ver,dest,cost = [int(x) for x in line.split()]
        heappush(E,[cost,ver,dest])
    file.close()
    clustering(E,rank,parent,numver)
#    expected result: 106

if __name__ == "__main__":
    main()
    
    