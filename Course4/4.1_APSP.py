"""
Coursera Algorithm Programming Assignemnt 4.1:
All pairs shortest path implement with 
1. Floyd-Warshal Algorithm
2. Johnson's Algorithm using reweighting edges
3. Optimized Johnson Algorithm
For optimized Johnson Algorithm, stop after running Bellman-Ford on graph with 
extra vertex s.The minimum among shortest paths from s to every other vertices 
is the apsp. Proof by contradiction: name the minimum shortest path from s smin,
if there is other minimum shortest path, namely a < smin which is from x to y. 
Then in the last iteration of Bellman-Ford, path from s to y is: s -> x + x -> y 
= 0 + a >= smin. Contradiction.  
@author: Tuan M. Nguyen
"""

# Floyd-Warshal Algorithm
def apspFW(filename):
    file = open(filename,"r")
    ver,edge = [int(x) for x in next(file).split()]
    A = {}
    for line in file:
        tail,head,cost = [int(x) for x in line.split()]
        if A.get((tail,head,0)) is None:
            A[tail,head,0] = cost
        else:
            A[tail,head,0] = min(A[tail,head,0],cost)
    file.close()
    
    for tail in range(1,ver+1):
        for head in range(1,ver+1):
            if A.get((tail,head,0)) is None:
                A[tail,head,0] = float('inf')
        if A.get((tail,tail,0)) == float('inf'):
            A[tail,tail,0] = 0
    shortest = float('inf')
    
    for k in range (1,ver+1):
        for i in range (1,ver+1):
            for j in range (1,ver+1):
                A[i,j,k] = min(A[i,j,k-1],A[i,k,k-1]+A[k,j,k-1])
                if k == ver:
                    if A[i,j,k] < shortest:
                        shortest = A[i,j,k]
    for i in range(1,ver+1):
        if A[i,i,ver] < 0:
            return "NULL"
    return shortest

# Johnson's Algorithm
from heapq import heappush,heappop,heapify
    
def dijkstra_Heap(A,G,ver,source):
    unvisited = []
    for index in range(1,ver+1):
        if index != source:
            heappush(unvisited,(float('inf'),index))
    heappush(unvisited,(0,source))

    visited = []
    distance = {}
    while unvisited:
        minHeap,addver = heappop(unvisited)
        visited.append(addver)
        distance[addver] = minHeap
        for dest in G[addver]:
            if dest not in visited:
                for (key_temp,temp) in unvisited:
                    if temp == dest:
                        unvisited.remove((key_temp,temp))
                        break;
                newKey = distance[addver]+G[addver][dest]
                heappush(unvisited,(min(key_temp,newKey),dest))
                heapify(unvisited)
    return distance
                
def readfile(filename):
    file = open(filename,"r")
    ver,edge = [int(x) for x in next(file).split()]
    Heads = {h:{} for h in range(1,ver+1)}
    Tails = {h:{} for h in range(1,ver+1)}
    for line in file:
        tail,head,cost = [int(x) for x in line.split()]
        if Heads[head].get(tail) is None:
            Heads[head][tail] = cost
        else:
            Heads[head][tail] = min(Heads[head][tail],cost)
        if Tails[tail].get(head) is None:
            Tails[tail][head] = cost
        else:
            Tails[tail][head] = min(Tails[tail][head],cost)
    file.close()
    return Tails,Heads,ver

def BellmanFord(ver,source,Heads):
    A = {}
    for v in range(1,ver+1):
        A[0,v] = float('inf')
    A[0,source] = 0
    stop = 0
    for i in range(1,ver):
        stop = 1
        for v in range(1,ver+1):
            min2 = float('inf')
            for w in Heads[v]:
                min2 = min(min2,A[i-1,w]+Heads[v][w])
            A[i,v] = min(A[i-1,v],min2)
            if A[i,v] != A[i-1,v]:
                stop = 0
        if stop == 1:
            break
    apsp = float('inf')
    for v in range(1,ver+1):
        apsp = min(A[i,v],apsp)
    if stop == 0:
        for v in range(1,ver+1):
            if A[ver-2,v] != A[ver-1,v]:
                return "NULL","NULL","NULL"
    return A,i,apsp

def apspJohnson(Tails,Heads,ver):
    for v in range(1,ver+1):
        Heads[v][ver+1] = 0
    Heads[ver+1] = {}
    A,laststep,apsp = BellmanFord(ver+1,ver+1,Heads)
    if A == "NULL":
        return "NULL"
    else:
        return apsp
# optimized Johnson's Algorithm stops here. Below is the original Johnson's Algorithm    
    for u in range(1,ver+1):
        for v in Tails[u]:
            Tails[u][v] = Tails[u][v] + A[laststep-1,u] - A[laststep-1,v]  
    minpair = float('inf')
    for u in range(1,ver+1):
        distance = dijkstra_Heap(A,Tails,ver,u)
        for v in distance:
            minpair = min(minpair,distance[v] - A[laststep-1,u] + A[laststep-1,v])  
    return minpair    

def main():
    Tails,Heads,ver = readfile("g1.txt")
    print(apspJohnson(Tails,Heads,ver))
    Tails,Heads,ver = readfile("g2.txt")
    print(apspJohnson(Tails,Heads,ver))
    Tails,Heads,ver = readfile("g3.txt")
    print(apspJohnson(Tails,Heads,ver))
#    expected result: NULL,NULL,-19
if __name__ == "__main__":
    main()