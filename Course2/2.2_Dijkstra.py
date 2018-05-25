#def dijkstra(G,num):
#    visited = [1]
#    distance = {}
#    path = {int(index+1):[1] for index in range(num)}   
#    distance[1] = 0
#    
#    while (len(visited) != num):
#        min_dist = float('inf')
#        for src in visited:
#            for dest in G[src]:
#                if dest not in visited:
#                    newDist = distance[src] + G[src][dest] 
#                    if newDist < min_dist :
#                        min_dist = newDist
#                        destmin_dist = dest
#        visited.append(destmin_dist)
#        distance[destmin_dist] = min_dist
#        path[destmin_dist].append(destmin_dist)
#        
#    vertices = [7,37,59,82,99,115,133,165,188,197]
#    for index in vertices:
#        print(distance[index])

from heapq import heappush,heappop,heapify
    
def dijkstra_Heap(G,num):
#    create heap of unvisited vertices with key infinity, key[1] = 0
    unvisited = []
    for index in range(num-1):
        heappush(unvisited,(float('inf'),index+2))
    heappush(unvisited,(0,1))
    
    visited = []
    distance = {}
    while unvisited:
        min_dist,vertex = heappop(unvisited)
        visited.append(vertex)
        distance[vertex] = min_dist
        for dest in G[vertex]:
            if dest not in visited:
                for (key_temp,temp) in unvisited:
                    if temp == dest:
                        unvisited.remove((key_temp,temp))
                        break;
                newKey = distance[vertex]+G[vertex][dest]
                heappush(unvisited,(min(key_temp,newKey),dest))
                heapify(unvisited)
                
    vertices = [7,37,59,82,99,115,133,165,188,197]
    for index in vertices:
        print(distance[index])

def main():
#   read input from file    
    f = open("dijkstraData.txt","r")
    line_list = f.readlines()
#   store graph in dictionary G    
    G = {int(line.split()[0]):{(int(tup.split(',')[0])):int(tup.split(',')[1]) 
    for tup in line.split()[1:] if tup} for line in line_list if line}
    f.close()
    
#    dijkstra(G,len(line_list))
    dijkstra_Heap(G,len(line_list))
#    expected result: 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
    
if __name__ == "__main__":
    main()