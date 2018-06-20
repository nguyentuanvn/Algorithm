"""
Coursera Algorithm Programming Assignemnt 3.1.2:
Prim's Minimum Spanning Tree Algorithm. Heap-based implementation by storing 
unprocessed vertices in heap.
@author: Tuan M. Nguyen
"""
from heapq import heappush,heappop,heapify

def MST(G,num):
    unprocessed = []
    processed = []
    for index in range(2,num+1):
        heappush(unprocessed,[float('inf'),index]) 
    heappush(unprocessed,[0,1])
    sum = 0
    while unprocessed:
        cost,vertex = heappop(unprocessed)
        sum += cost
        processed.append(vertex)
        for dest in G[vertex]:
            if dest not in processed:
                for (key,temp) in unprocessed:
                    if temp == dest:
                        unprocessed.remove([key,temp])
                        break;
                newKey = min(key,G[vertex][dest],G[dest][vertex])
                heappush(unprocessed,[newKey,temp])
                heapify(unprocessed)
    print(sum)
    
def main():
    file = open("3.1.3_edges.txt","r")
    v,e = [int(x) for x in next(file).split()]
    G = {ver:{} for ver in range(1,v+1)}
    for line in file:
        ver,dest,cost = [int(x) for x in line.split()]
        try:
            G[ver][dest]
        except: 
            G[ver][dest] = cost
            G[dest][ver] = cost
        else:
            if G[ver][dest] > cost:
                G[ver][dest] = cost
                G[dest][ver] = cost
    file.close()
    MST(G,v)
#    expected result: -3612829
    
if __name__ == "__main__":
    main()
    